.DEFAULT_GOAL:=	all

all: coverage

coverage:
	coverage run -m pytest
	coverage report -m

test:
	pytest

autopep8-fix:
	autopep8 -ri src tests

autopep8:	autopep8-fix
	autopep8 -ri --select=E501 src tests

lint:
	pylint src tests
