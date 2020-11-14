.DEFAULT_GOAL:=	all

all: coverage

coverage:
	coverage run -m pytest
	coverage report -m

test:
	pytest

lint:
	pylint src tests
