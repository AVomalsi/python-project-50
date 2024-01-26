install:
	poetry install

build:
	poetry build

gendiff:
	poetry run brain-games

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest -s

test-coverage:
	poetry run pytest --cov

selfcheck:
	poetry check

check: selfcheck test lint

.PHONY: install test lint selfcheck check build