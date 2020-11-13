.DEFAULT_GOAL:=	all

all: coverage

requirements:
	pipreqs --clean requirements.txt src
	pipreqs --savepath requirements.txt src

coverage:
	coverage run -m pytest
	coverage report -m

test:
	pytest
