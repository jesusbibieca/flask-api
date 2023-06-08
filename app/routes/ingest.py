from flask import Blueprint, request

from utils.process_ingest import process_ingest


ingest_bp = Blueprint("ingest", __name__)


@ingest_bp.route("/ingest", methods=["POST"])
def ingest():
    content_type = request.headers.get("Content-Type")
    if content_type == "application/json":
        json = request.get_json()
        url = json["gbfs_url"]
        if url:
            process_ingest(url)
        return "created", 201
    return "Content-Type not supported!"
