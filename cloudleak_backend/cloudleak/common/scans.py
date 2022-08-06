from datetime import datetime
from cloudleak_backend.cloudleak.app import create_flask_app
from cloudleak_backend.cloudleak.models.target import Scan
from flask_pymongo import PyMongo
from cloudleak_backend.cloudleak.models.objectid import PydanticObjectId

mongo = PyMongo(create_flask_app())
db = mongo.db

def initiate_scan(scan_info):
    # run cli tool (in an async way)
    scan_info["added_ts"] = round(datetime.now().timestamp())
    
    # validate scan user input
    scan = Scan(**scan_info)
    insert_result = db.scans.insert_one(scan.to_bson())
    scan.id = PydanticObjectId(str(insert_result.inserted_id))

    return scan.id


def get_scans(scan_id=None):
    if scan_id:
        return db.scans.find_one({'_id': scan_id})
    
    return db.scans.find({})
