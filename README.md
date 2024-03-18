# Foxy-reminder: The Reminders App
A simple reminder app for the foxy.

* [Python](https://www.python.org/) as the main programming language
* [FastAPI](https://fastapi.tiangolo.com/) for the backend
* [HTMX](https://htmx.org/) 1.8.6 for handling dynamic interactions (instead of raw JavaScript)
* [Jinja templates](https://jinja.palletsprojects.com/en/3.1.x/) with HTML and CSS for the frontend
* [TinyDB](https://tinydb.readthedocs.io/en/latest/index.html) for the database
* [Playwright](https://playwright.dev/python/) and [pytest](https://docs.pytest.org/) for testing

<img width="1393" alt="Screenshot of Arc at Mar 18, 2024 1_12_14 PM" src="https://github.com/szto/foxy-reminder/assets/19988590/331f47b6-b9d5-47d3-919c-c199a6d744c2">

## Install

To install project dependencies:
```bash
# uv
uv pip install -r requirements.txt

# pip
pip intstall -r requirements.txt
```

## Run

To run the app:

```bash
uvicorn app.main:app --reload
```

To load the app, open your browser to ["http://127.0.0.1:8000/login"](http://127.0.0.1:8000/login)

## Logging into the app

The [`config.json`](config.json) file declares the users for the app.
You may use any configured user credentials, or change them to your liking.

## Setting the database path

The app uses TinyDB, which stores the database as a JSON file.
The default database filepath is `reminder_db.json`.

## Credits

- This project is inspired by [Bulldoggy-reminder-app](https://github.com/AutomationPanda/bulldoggy-reminders-app) AutomationPanda.

