from flask import Blueprint, jsonify, request, abort

scans_api = Blueprint("scans_api", __name__)


@scans_api.route("/api/scans", methods=["post"])
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
            description: Scan information.
        500:
            description: Generic error.
    """
    scan_input_info = request.get_json(silent=True)
    print(scan_input_info)


# @scans_api.route("/api/scans", methods=["get"])