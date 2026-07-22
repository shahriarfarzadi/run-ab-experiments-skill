.PHONY: validate package clean

validate:
	./scripts/validate.sh

package: validate
	./scripts/package-release.sh

clean:
	rm -rf dist
