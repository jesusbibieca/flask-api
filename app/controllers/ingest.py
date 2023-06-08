from datetime import datetime
from database.db import get_db_connection


def insert_station_information(station_information):
    """Upserts station information into the database.

    Args:
        station_information (list): A list of dictionaries containing the station information.
    """
    conn = get_db_connection()

    sql = "INSERT INTO stations (station_id, name, address, latitude, longitude) VALUES %s \
        ON CONFLICT (station_id) DO UPDATE SET name = EXCLUDED.name, address = EXCLUDED.address,\
        latitude = EXCLUDED.latitude, longitude = EXCLUDED.longitude;"

    data = [
        (
            station["station_id"],
            station["name"],
            station["address"],
            station["lat"],
            station["lon"],
        )
        for station in station_information
    ]

    conn.insert_many(sql, data)


def insert_station_status(station_status):
    """Updates station status into the database.

    Args:
        station_status (list): A list of dictionaries containing the station status.
    """
    conn = get_db_connection()

    sql = "UPDATE stations SET is_returning = s.is_returning, is_renting = s.is_renting, is_installed = s.is_installed, \
        num_docks_available = s.num_docks_available, num_bikes_available = s.num_bikes_available, last_reported = s.last_reported \
        FROM (VALUES %s) as s (is_returning, is_renting, is_installed, num_docks_available, num_bikes_available, last_reported, station_id)\
        WHERE stations.station_id = s.station_id;"

    data = [
        (
            bool(station["is_returning"]),
            bool(station["is_renting"]),
            bool(station["is_installed"]),
            station["num_docks_available"],
            station["num_bikes_available"],
            datetime.fromtimestamp(station["last_reported"]),
            station["station_id"],
        )
        for station in station_status
    ]

    conn.insert_many(sql, data)
