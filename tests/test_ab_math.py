from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "skills" / "run-ab-experiments" / "scripts" / "ab_math.py"


def load_module():
    spec = importlib.util.spec_from_file_location("ab_math", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load ab_math.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class AbMathTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()

    def run_cli(self, *arguments: str) -> dict[str, object]:
        result = subprocess.run(
            [sys.executable, str(SCRIPT), *arguments],
            check=True,
            capture_output=True,
            text=True,
        )
        return json.loads(result.stdout)

    def test_balanced_sample_size(self) -> None:
        result = self.run_cli(
            "sample-size",
            "--stddev", "1",
            "--absolute-mde", "0.1",
        )
        self.assertEqual(result["treatment_n"], result["control_n"])
        self.assertGreaterEqual(result["total_n"], 3000)

    def test_mean_effect_direction_and_interval(self) -> None:
        result = self.run_cli(
            "mean-effect",
            "--control-mean", "10",
            "--control-variance", "4",
            "--control-n", "1000",
            "--treatment-mean", "10.5",
            "--treatment-variance", "4",
            "--treatment-n", "1000",
        )
        self.assertAlmostEqual(result["absolute_effect"], 0.5)
        self.assertTrue(result["statistically_significant"])

    def test_srm_detects_large_mismatch(self) -> None:
        result = self.run_cli("srm", "--observed", "9000", "1000")
        self.assertTrue(result["srm_detected"])
        self.assertTrue(str(result["validity_action"]).startswith("STOP"))

    def test_gamma_reference_value(self) -> None:
        value = self.module.regularized_gamma_q(0.5, 1.0)
        self.assertAlmostEqual(value, 0.157299207, places=8)

    def test_invalid_probability_fails(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "sample-size",
                "--stddev", "1",
                "--absolute-mde", "0.1",
                "--alpha", "1",
            ],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("alpha must be between 0 and 1", result.stderr)


if __name__ == "__main__":
    unittest.main()
