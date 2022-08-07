import cloudleak.common.scans as scans
from flask_pymongo import PyMongo


def initiate_scan(scan_info):
    scan_id = scans.add_scan(scan_info)

    # the actual scan here:

    return scan_id
