.DEFAULT_GOAL := all

PYLINT_DIRS ?= src tests

AUTOPEP8_EXPERIMENTAL_DIRS ?= src tests
AUTOPEP8_MIGRATIONS_DIR ?= migrations
AUTOPEP8_DIRS ?= $(AUTOPEP8_EXPERIMENTAL_DIRS) $(AUTOPEP8_MIGRATIONS_DIR)

all: coverage

coverage-run:
	coverage run -m pytest

coverage-report:
	coverage report -m

coverage: coverage-run coverage-report

test:
	pytest

autopep8-diff-experimental:
	@for d in $(AUTOPEP8_EXPERIMENTAL_DIRS); do \
		autopep8 -vvvrd --exit-code --experimental --select E501 $$d; \
	done

autopep8-diff-regular:
	@for d in $(AUTOPEP8_DIRS); do \
		autopep8 -vvvrd --exit-code $$d; \
	done

autopep8-diff: autopep8-diff-regular autopep8-diff-experimental

autopep8-fix-experimental:
	@for d in $(AUTOPEP8_EXPERIMENTAL_DIRS); do \
		autopep8 -ri --experimental --select E501 $$d; \
	done

autopep8-fix-regular:
	@for d in $(AUTOPEP8_DIRS); do \
		autopep8 -ri $$d; \
	done

autopep8-fix: autopep8-fix-regular autopep8-fix-experimental

autopep8:	autopep8-diff

lint:
	@for d in $(PYLINT_DIRS); do \
		pylint $$d; \
	done
