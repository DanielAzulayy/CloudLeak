from cloudleak.models.objectid import PydanticObjectId
from cloudleak.models.target import Scan
from cloudleak.app import create_app
from flask_pymongo import PyMongo

app = create_app(register_blueprints=False)
mongo_client = PyMongo(app, uri=app.config['MONGO_URI'])
db = mongo_client.db

def add_scan(scan_info):
    scan = Scan(**scan_info)
    insert_result = db.scans.insert_one(scan.to_bson())
    scan.id = PydanticObjectId(str(insert_result.inserted_id))

    return scan.id


def get_scans(scan_id=None):
    if scan_id:
        return db.scans.find({"_id": scan_id})

    s = db.scans.find({})
    return Scan(**s).to_json()
