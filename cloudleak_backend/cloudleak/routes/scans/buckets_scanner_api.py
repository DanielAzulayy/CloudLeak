import json
from time import time

from cloudleak.models.scan_status import ScanStatus
from flask import Blueprint, abort, jsonify, redirect, request
from loguru import logger

scans_api = Blueprint("scans_api", __name__)


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
    scan_info = request.get_json(silent=True)
    if not scan_info:
        abort(400, description="Scan info missing")

    try:
        from cloudleak.common import async_scan, scans
        scan_info["added_ts"] = round(time())
        scan_info["status"] = ScanStatus.SCAN_RUNNING.value
        scan_id = async_scan.initiate_scan(scan_info)
        scan = scans.get_scan(scan_id=scan_id)
    except Exception as e:
        logger.exception(e)
        abort(500, description="Failed to start scan")

    return jsonify(message="Scan started successfully", status=200)


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
        from cloudleak.common import scans

        found_scans = scans.get_scan()
    except Exception as e:
        logger.exception(str(e))
        abort(500, description="Failed to get all scans")

    return jsonify(results=found_scans, status=200)
