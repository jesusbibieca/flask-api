from database.db import get_db_connection


def all_stations():
    """Queries all the stations.

    Returns:
        list: A list of dictionaries containing the stations.
    """
    conn = get_db_connection()

    sql = "SELECT station_id, name, address, latitude, longitude FROM stations;"

    stations = conn.get_json_response(sql)

    return stations


def get_station_by_station_id(station_id):
    """Queries a single station.

    Args:
        station_id (str): The station id.

    Returns:
        dict: A dictionary containing the station.
    """
    conn = get_db_connection()

    sql = f"SELECT\
        station_id,\
        is_returning,\
        is_renting,\
        is_installed,\
        num_docks_available,\
        num_bikes_available,\
        EXTRACT(EPOCH FROM last_reported)::int as last_reported\
        FROM stations WHERE station_id = '{station_id}';"

    station = conn.get_json_response(sql)

    return station
