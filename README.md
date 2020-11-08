# Moonnymathics API

API for Moonshot Jam 2020 project.

See https://itch.io/jam/game-off-2020 and https://github.com/geka32team/moonshot-jam-2020-front


## Install

### clone the repository

    $ git clone https://github.com/geka32team/moonshot-jam-2020-back
    $ cd moonshot-jam-2020-back

### Create a virtualenv and activate it

    $ python3 -m venv .venv
    $ . .venv/bin/activate

Or on Windows cmd:

    > py -3 -m venv venv
    > .venv\Scripts\activate.bat

### Install requirements

    $ pip install -r requirements.txt


## Run

### On local machine

    $ export FLASK_APP=src
    $ export FLASK_ENV=development
    $ flask init-db
    $ flask run

Or on Windows cmd:

    > set FLASK_APP=src
    > set FLASK_ENV=development
    > flask init-db
    > flask run

Open http://127.0.0.1:5000 in a browser.
