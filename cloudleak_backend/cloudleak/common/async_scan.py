from re import I
from typing import Dict
from cloudleak.models.objectid import PydanticObjectId

from flask_pymongo import PyMongo

import cloudleak.common.scans as scans
from cloudleak.app import create_celery
from cloudleak.common.buckets_hunter import BucketScan

celery = create_celery()


def initiate_scan(scan_info: Dict):
    target: str = scan_info.get("target", None)
    platform: str = scan_info.get("platform", None)
    if None in (target, platform):
        return None

    scan_id = scans.add_scan(scan_info)
    result = buckets_hunter_scan.apply_async(args=[target, platform, str(scan_id)])

    return scan_id


@celery.task
def buckets_hunter_scan(target: str, platform: str, scan_id: str):
    bucket_scan = BucketScan(target=target, platform=platform)
    bucket_scan.run_buckets_hunter()
    bucket_scan.store_results(scan_id)
