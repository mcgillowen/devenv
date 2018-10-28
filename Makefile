.PHONY: test clean

test:
	poetry run pytest --cov=devenv tests

clean:
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

install:
	poetry install

install_poetry: install
	curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
