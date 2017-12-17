# Installation

Make sure you have `pipenv` installed. Pipenv is a packaging tool for Python.

```$ pip install pipenv```

Set the environment variable `FLASK_APP` to `server_py`:

```$ export FLASK_APP=server.py```

Edit `api_keys.py` and replace the values of Google Maps and Dark Sky API keys.

Start the webserver:

```$ pipenv run python -m flask run```