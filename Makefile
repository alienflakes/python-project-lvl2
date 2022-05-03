install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

.PHONY: gendiff
gendiff:
	poetry run gendiff

test-coverage:
	coverage run -m pytest --cov=gendiff tests/ --cov-report xml

selfcheck:
	poetry check

check: selfcheck test lint

.PHONY: install test lint selfcheck check build
