import subprocess
from os import mkdir
from time import time

from .scans import save_bucket


class BucketScan:
    def __init__(self, target: str, platform: str) -> None:
        self.target = target
        self.platform = platform
        self.results_dir = "/home/tesla-1661797169"
        self.full_path = f"{self.results_dir}/scan_results.json"

    def run_buckets_hunter(self):
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

    def store_results(self):
        """Save the scan results on db"""
        with open(self.full_path, "r") as results_file:
            for bucket in results_file:
                save_bucket(bucket)
