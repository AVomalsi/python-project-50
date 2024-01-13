install:
	poetry install

gendiff:
	poetry run brain-games

build:
	poetry build

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