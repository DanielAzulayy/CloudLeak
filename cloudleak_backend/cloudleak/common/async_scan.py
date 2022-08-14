from typing import Dict
import cloudleak.common.scans as scans
from flask_pymongo import PyMongo

from cloudleak.app import create_celery
from cloudleak.common.buckets_hunter import BucketScan

celery = create_celery()


@celery.task
def buckets_scan(target: str, platform: str):
    bucket_scan = BucketScan(target=target, platform=platform)
    bucket_scan.run_buckets_hunter()


def initiate_scan(scan_info: Dict):
    scan_id = scans.add_scan(scan_info)

    target = scan_info["target"]
    platform = scan_info["platform"]
    task = buckets_scan.apply_async(args=[target, platform])

    return scan_id
