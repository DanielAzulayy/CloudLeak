from cloudleak.models.objectid import PydanticObjectId
from cloudleak.models.target import Scan
from cloudleak.app import create_app
from flask_pymongo import PyMongo

app = create_app()
mongo = PyMongo(app)
db = mongo.db


def add_scan(scan_info):
    scan = Scan(**scan_info)
    insert_result = db.scans.insert_one(scan.to_bson())
    scan.id = PydanticObjectId(str(insert_result.inserted_id))

    return scan.id


def get_scans(scan_id=None):
    if scan_id:
        return db.scans.find({"_id": scan_id})

    return db.scans.find({})
