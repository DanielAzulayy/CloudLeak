from typing import List

from cloudleak.app import create_app
from cloudleak.models.objectid import PydanticObjectId
from cloudleak.models.target import Scan
from flask_pymongo import PyMongo

from ..models.scan_status import ScanStatus

app = create_app(register_blueprints=False)
mongo_client = PyMongo(app, uri=app.config["MONGO_URI"])
db = mongo_client.db


def add_scan(scan_info):
    scan = Scan(**scan_info)
    insert_result = db.scans.insert_one(scan.to_bson())
    scan.id = PydanticObjectId(str(insert_result.inserted_id))
    return scan.id


def get_scan(scan_id=None) -> List:
    if scan_id is not None:
        cursor = db.scans.find({"_id": scan_id})
    else:
        cursor = db.scans.find()

    if not cursor:
        return []

    found_docs = []
    for doc in cursor:
        json_doc = Scan(**doc).to_json()
        json_doc["status"] = ScanStatus(json_doc["status"]).name
        found_docs.append(json_doc)

    return found_docs


def save_bucket(scan_id, buckets_results):
    db.scans.update_one(
        {"_id": PydanticObjectId(scan_id)}, {"$set": {"buckets": buckets_results}}
    )
