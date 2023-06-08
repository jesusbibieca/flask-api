# Flask API

This project is intended to be a simple API using Flask and CockroachDB.

## Before you start

Create a `.env` file in the root directory and add the following:

```
FLASK_ENV=<ENV_KEY_HERE>
DB_URI=postgresql://root@db:26257/defaultdb?sslmode=disable&options=--cluster%3Droach1
```

Use the following keys (`<ENV_KEY_HERE>`) for the different environments:
`dev` for development
`test` for testing
`<EMPTY>` for production

## Install dependencies

```
pip install -r requirements.txt
```

## Run the app

First you will need to create the database:
Go to your `.env` file and change the `DB_URI` to the following:

```
DB_URI=postgresql://root@localhost:26257/defaultdb?sslmode=disable&options=--cluster%3Droach1
```

Then run the following command:

```
python app/database/init_db.py
```

And revert the `DB_URI` to the original value.

Then you can run the app with docker-compose:

```
docker-compose up
```

Now the app should be running on `http://localhost:8000/`

You have the following endpoints:

```
GET   /stations
GET   /stations/<id>/status
POST  /ingest
```

Things to consider, the `POST /ingest` endpoint expects a JSON body with the following format:

```
{
  "gbfs_url": "string"
}
```
