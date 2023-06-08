from flask import Flask
import os

from routes import ingest, stations


app = Flask(__name__)

if os.environ.get("FLASK_ENV") == "dev":
    app.logger.info(os.environ.get("FLASK_ENV"))
    app.config.from_object("app_config.Development")

elif os.environ.get("FLASK_ENV") == "test":
    app.logger.info(os.environ.get("FLASK_ENV"))
    app.config.from_object("app_config.Testing")

else:
    app.logger.info(os.environ.get("FLASK_ENV"))
    app.config.from_object("app_config.Production")


app.register_blueprint(ingest.ingest_bp)
app.register_blueprint(stations.station_bp)

if __name__ == "__main__":
    app.run(host=app.config["HOST"], port=app.config["PORT"])
