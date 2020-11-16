.DEFAULT_GOAL:=	all

all: coverage

coverage-run:
	coverage run -m pytest

coverage-report:
	coverage report -m

coverage: coverage-run coverage-report

test:
	pytest

autopep8-diff-experimental:
	autopep8 -vvvrd --exit-code --experimental --select E501 src
	autopep8 -vvvrd --exit-code --experimental --select E501 tests

autopep8-diff: autopep8-diff-experimental
	autopep8 -vvvrd --exit-code src
	autopep8 -vvvrd --exit-code tests

autopep8-fix-experimental:
	autopep8 -ri --experimental --select E501 src
	autopep8 -ri --experimental --select E501 tests

autopep8-fix: autopep8-fix-experimental
	autopep8 -ri src
	autopep8 -ri tests

autopep8:	autopep8-diff autopep8-fix

lint:
	pylint src tests
