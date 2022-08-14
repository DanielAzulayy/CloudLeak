
import subprocess


class BucketScan:
    def __init__(self, target: str, platform: str) -> None:
        self.target = target
        self.platform = platform
    
    def run_buckets_hunter(self):
        subprocess.call([
            'bucketshunter',
            '-k',
            self.target,
            '-p',
            self.platform,
            '-o',
            'output.json'
        ])
    
