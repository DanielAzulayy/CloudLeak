import subprocess
from os import mkdir
from time import time

import ujson
from cloudleak.models.objectid import PydanticObjectId

from .scans import save_bucket


class BucketScan:
    def __init__(self, target: str, platform: str) -> None:
        self.target = target
        self.platform = platform

        self.results_dir = f"/home/{self.target}-{int(time())}"
        mkdir(self.results_dir)
        self.full_path = f"{self.results_dir}/scan_results.json"

    def run_buckets_hunter(self):
        """Run: https://github.com/DanielAzulayy/BucketsHunter"""
        subprocess.call(
            [
                "buckets-hunter",
                "-k",
                self.target,
                "-p",
                self.platform,
                "-o",
                self.full_path,
            ]
        )

    def store_results(self, scan_id: str):
        """Save the scan results on db"""
        found_buckets = None
        with open(self.full_path, "r") as results_file:
            found_buckets = ujson.load(results_file)

        if not found_buckets:
            return None

        save_bucket(scan_id, found_buckets)
