from flask import Blueprint, jsonify

from controllers.stations import all_stations, get_station_by_station_id


station_bp = Blueprint("stations", __name__)


@station_bp.route("/stations")
def get_stations():
    stations = all_stations()
    return jsonify(stations), 200


@station_bp.route("/stations/<station_id>/status")
def get_station(station_id):
    station = get_station_by_station_id(station_id)
    if not station:
        return jsonify({"error": "Station not found"}), 404
    return jsonify(station), 200
