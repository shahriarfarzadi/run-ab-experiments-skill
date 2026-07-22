#!/usr/bin/env python3
"""Dependency-free checks for transparent A/B experiment calculations.

This calculator intentionally covers only standard normal-approximation sample
size, independent-arm mean effects, and Pearson chi-square SRM checks. Use a
validated statistics package for sequential, clustered, ratio, percentile,
covariate-adjusted, or other specialized analyses.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from statistics import NormalDist
from typing import Sequence


NORMAL = NormalDist()


def fail(message: str) -> None:
    raise ValueError(message)


def probability(value: float, name: str) -> float:
    if not 0.0 < value < 1.0:
        fail(f"{name} must be between 0 and 1 (exclusive)")
    return value


def positive(value: float, name: str) -> float:
    if not math.isfinite(value) or value <= 0.0:
        fail(f"{name} must be a finite positive number")
    return value


def nonnegative(value: float, name: str) -> float:
    if not math.isfinite(value) or value < 0.0:
        fail(f"{name} must be a finite nonnegative number")
    return value


def regularized_gamma_q(a: float, x: float) -> float:
    """Return Q(a, x), the regularized upper incomplete gamma function."""
    if a <= 0.0 or x < 0.0:
        fail("regularized gamma requires a > 0 and x >= 0")
    if x == 0.0:
        return 1.0

    eps = 3.0e-14
    max_iterations = 10_000
    log_scale = -x + a * math.log(x) - math.lgamma(a)

    if x < a + 1.0:
        term = 1.0 / a
        total = term
        ap = a
        for _ in range(max_iterations):
            ap += 1.0
            term *= x / ap
            total += term
            if abs(term) <= abs(total) * eps:
                p = total * math.exp(log_scale)
                return min(1.0, max(0.0, 1.0 - p))
        fail("lower incomplete-gamma series did not converge")

    tiny = sys.float_info.min / eps
    b = x + 1.0 - a
    c = 1.0 / tiny
    d = 1.0 / max(abs(b), tiny)
    if b < 0.0:
        d = -d
    h = d
    for i in range(1, max_iterations + 1):
        an = -float(i) * (float(i) - a)
        b += 2.0
        d = an * d + b
        if abs(d) < tiny:
            d = tiny
        c = b + an / c
        if abs(c) < tiny:
            c = tiny
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) <= eps:
            q = math.exp(log_scale) * h
            return min(1.0, max(0.0, q))
    fail("upper incomplete-gamma continued fraction did not converge")


def command_sample_size(args: argparse.Namespace) -> dict[str, object]:
    alpha = probability(args.alpha, "alpha")
    power = probability(args.power, "power")
    treatment_share = probability(args.treatment_share, "treatment-share")
    stddev = positive(args.stddev, "stddev")

    if args.absolute_mde is not None:
        absolute_mde = positive(args.absolute_mde, "absolute-mde")
        baseline_mean = args.baseline_mean
        relative_mde = (
            absolute_mde / baseline_mean
            if baseline_mean is not None and baseline_mean != 0.0
            else None
        )
    else:
        if args.relative_mde is None or args.baseline_mean is None:
            fail("relative-mde requires baseline-mean")
        relative_mde = positive(args.relative_mde, "relative-mde")
        baseline_mean = args.baseline_mean
        if not math.isfinite(baseline_mean) or baseline_mean == 0.0:
            fail("baseline-mean must be finite and nonzero for relative MDE")
        absolute_mde = abs(baseline_mean) * relative_mde

    z_alpha = NORMAL.inv_cdf(1.0 - alpha / 2.0)
    z_power = NORMAL.inv_cdf(power)
    if z_power <= 0.0:
        fail("power must be greater than 0.5 for this calculator")

    control_share = 1.0 - treatment_share
    total_unrounded = (
        (z_alpha + z_power) ** 2
        * stddev**2
        * (1.0 / treatment_share + 1.0 / control_share)
        / absolute_mde**2
    )
    total = math.ceil(total_unrounded)
    treatment_n = math.ceil(total * treatment_share)
    control_n = math.ceil(total * control_share)

    return {
        "calculation": "two-sided two-sample normal approximation",
        "alpha": alpha,
        "power": power,
        "stddev": stddev,
        "baseline_mean": baseline_mean,
        "absolute_mde": absolute_mde,
        "relative_mde": relative_mde,
        "treatment_share": treatment_share,
        "control_share": control_share,
        "treatment_n": treatment_n,
        "control_n": control_n,
        "total_n": treatment_n + control_n,
        "warning": (
            "Assumes independent units, equal arm variances, fixed-horizon "
            "inference, and no attrition. Inflate for exclusions and trigger rate."
        ),
    }


def command_mean_effect(args: argparse.Namespace) -> dict[str, object]:
    alpha = probability(args.alpha, "alpha")
    control_variance = nonnegative(args.control_variance, "control-variance")
    treatment_variance = nonnegative(args.treatment_variance, "treatment-variance")
    control_n = positive(args.control_n, "control-n")
    treatment_n = positive(args.treatment_n, "treatment-n")
    for value, name in (
        (args.control_mean, "control-mean"),
        (args.treatment_mean, "treatment-mean"),
    ):
        if not math.isfinite(value):
            fail(f"{name} must be finite")

    delta = args.treatment_mean - args.control_mean
    standard_error = math.sqrt(
        control_variance / control_n + treatment_variance / treatment_n
    )
    z_critical = NORMAL.inv_cdf(1.0 - alpha / 2.0)
    lower = delta - z_critical * standard_error
    upper = delta + z_critical * standard_error
    if standard_error == 0.0:
        z_score = 0.0 if delta == 0.0 else math.copysign(math.inf, delta)
        p_value = 1.0 if delta == 0.0 else 0.0
    else:
        z_score = delta / standard_error
        p_value = math.erfc(abs(z_score) / math.sqrt(2.0))
    relative_delta = (
        delta / args.control_mean if args.control_mean != 0.0 else None
    )

    return {
        "calculation": "independent-arm mean difference, normal approximation",
        "alpha": alpha,
        "control_mean": args.control_mean,
        "treatment_mean": args.treatment_mean,
        "absolute_effect": delta,
        "relative_effect": relative_delta,
        "standard_error": standard_error,
        "confidence_interval": [lower, upper],
        "z_score": z_score,
        "p_value": p_value,
        "statistically_significant": p_value < alpha,
        "warning": (
            "Do not use this calculation for correlated events, ratio metrics, "
            "percentiles, clusters, sequential looks, or covariate adjustment."
        ),
    }


def command_srm(args: argparse.Namespace) -> dict[str, object]:
    observed = args.observed
    if len(observed) < 2:
        fail("observed must contain at least two variant counts")
    if any((not math.isfinite(value) or value < 0.0) for value in observed):
        fail("observed counts must be finite and nonnegative")
    total = sum(observed)
    positive(total, "sum of observed counts")

    if args.expected is None:
        expected_shares = [1.0 / len(observed)] * len(observed)
    else:
        if len(args.expected) != len(observed):
            fail("expected and observed must have the same number of values")
        if any((not math.isfinite(value) or value <= 0.0) for value in args.expected):
            fail("expected shares must be finite and positive")
        expected_total = sum(args.expected)
        expected_shares = [value / expected_total for value in args.expected]

    expected_counts = [total * share for share in expected_shares]
    chi_square = sum(
        (actual - expected) ** 2 / expected
        for actual, expected in zip(observed, expected_counts)
    )
    degrees_of_freedom = len(observed) - 1
    p_value = regularized_gamma_q(degrees_of_freedom / 2.0, chi_square / 2.0)
    threshold = probability(args.threshold, "threshold")

    return {
        "calculation": "Pearson chi-square goodness-of-fit SRM test",
        "observed": observed,
        "expected_shares": expected_shares,
        "expected_counts": expected_counts,
        "chi_square": chi_square,
        "degrees_of_freedom": degrees_of_freedom,
        "p_value": p_value,
        "threshold": threshold,
        "srm_detected": p_value < threshold,
        "validity_action": (
            "STOP: treat outcome metrics as invalid and debug the mismatch."
            if p_value < threshold
            else "SRM check passed at the selected threshold."
        ),
    }


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(
        description="Transparent, dependency-free A/B experiment calculations."
    )
    subparsers = root.add_subparsers(dest="command", required=True)

    size = subparsers.add_parser(
        "sample-size",
        help="Estimate units for a fixed-horizon, two-arm mean comparison.",
    )
    size.add_argument("--stddev", type=float, required=True)
    mde = size.add_mutually_exclusive_group(required=True)
    mde.add_argument("--absolute-mde", type=float)
    mde.add_argument(
        "--relative-mde",
        type=float,
        help="Decimal relative change, for example 0.01 for 1%%.",
    )
    size.add_argument("--baseline-mean", type=float)
    size.add_argument("--alpha", type=float, default=0.05)
    size.add_argument("--power", type=float, default=0.8)
    size.add_argument("--treatment-share", type=float, default=0.5)
    size.set_defaults(function=command_sample_size)

    effect = subparsers.add_parser(
        "mean-effect",
        help="Estimate an independent-arm mean difference and confidence interval.",
    )
    effect.add_argument("--control-mean", type=float, required=True)
    effect.add_argument("--control-variance", type=float, required=True)
    effect.add_argument("--control-n", type=float, required=True)
    effect.add_argument("--treatment-mean", type=float, required=True)
    effect.add_argument("--treatment-variance", type=float, required=True)
    effect.add_argument("--treatment-n", type=float, required=True)
    effect.add_argument("--alpha", type=float, default=0.05)
    effect.set_defaults(function=command_mean_effect)

    srm = subparsers.add_parser(
        "srm", help="Run a Pearson chi-square sample-ratio-mismatch check."
    )
    srm.add_argument("--observed", type=float, nargs="+", required=True)
    srm.add_argument(
        "--expected",
        type=float,
        nargs="+",
        help="Planned positive shares or weights; defaults to equal allocation.",
    )
    srm.add_argument("--threshold", type=float, default=0.001)
    srm.set_defaults(function=command_srm)

    return root


def main(argv: Sequence[str] | None = None) -> int:
    try:
        args = parser().parse_args(argv)
        print(json.dumps(args.function(args), indent=2, sort_keys=True))
    except ValueError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
