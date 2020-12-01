.DEFAULT_GOAL:=	all

PYLINT_DIRS?= src tests
AUTOPEP8_DIRS?= src tests migrations

all: coverage

coverage-run:
	coverage run -m pytest

coverage-report:
	coverage report -m

coverage: coverage-run coverage-report

test:
	pytest

autopep8-diff-experimental:
	@for d in $(AUTOPEP8_DIRS); do \
		autopep8 -vvvrd --exit-code --experimental --select E501 $$d; \
	done

autopep8-diff: autopep8-diff-experimental
	@for d in $(AUTOPEP8_DIRS); do \
		autopep8 -vvvrd --exit-code $$d; \
	done

autopep8-fix-experimental:
	@for d in $(AUTOPEP8_DIRS); do \
		autopep8 -ri --experimental --select E501 $$d; \
	done

autopep8-fix: autopep8-fix-experimental
	@for d in $(AUTOPEP8_DIRS); do \
		autopep8 -ri $$d; \
	done

autopep8:	autopep8-diff

lint:
	@for d in $(PYLINT_DIRS); do \
		pylint $$d; \
	done
