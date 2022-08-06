from cloudleak_backend.cloudleak.common import scans
from flask import Blueprint, abort, jsonify, request
from loguru import logger

scans_api = Blueprint("scans_api", __name__)

mongo = PyMongo(create_flask_app())

@scans_api.route("/api/scans", methods=["POST"])
def start_buckets_scan():
    """API for bucket scanning.

    params:
        target: string
            target to scan.
        platform: string
            platform for scanning, can either be 'all',
            or specific platform ('azure', 'aws', 'gcp').
    responses:
        200:
            description: Started scan successfully.
        500:
            description: Server error, scan failed.
    """
    user_scan_info = request.get_json(silent=True)
    if not user_scan_info:
        abort(400, description="Scan info missing")

    try:
        scan_id = scans.initiate_scan(user_scan_info)
        scan = scans.get_scans(scan_id=scan_id)
    except Exception as e:
        logger.exception(e)
        abort(500, description="Failed to start scan")

    return jsonify(results=scan)

@scans_api.route("/api/scans", methods=["GET"])
def get_scans():
    """Getting all valid scans.
    responses:
        200:
            description: all found scans from DB.
        500:
            description: Server error.
    """
    found_scans = None
    try:
        found_scans = scans.get_scans()
    except Exception as e:
        logger.exception(e)
        abort(500)

    return jsonify(results=found_scans)
