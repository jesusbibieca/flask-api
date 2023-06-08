import sys
import requests

from controllers.ingest import insert_station_information, insert_station_status


def process_ingest(url):
    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        print("Error: ", response.status_code, file=sys.stderr)
        return

    json_response = response.json()

    feeds = json_response["data"]["en"]["feeds"]
    print("feeds: ", feeds, file=sys.stderr)

    station_information_url = None
    station_status_url = None

    for feed in feeds:
        if feed["name"] == "station_information":
            station_information_url = feed["url"]
        elif feed["name"] == "station_status":
            station_status_url = feed["url"]

    process_station_information(station_information_url)
    process_station_status(station_status_url)

    return json_response


def process_station_information(url):
    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        print("Error: ", response.status_code, file=sys.stderr)
        return

    json_response = response.json()

    station_information = json_response["data"]["stations"]

    insert_station_information(station_information)


def process_station_status(url):
    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        print("Error: ", response.status_code, file=sys.stderr)
        return

    json_response = response.json()

    station_status = json_response["data"]["stations"]

    insert_station_status(station_status)
