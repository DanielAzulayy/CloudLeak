from enum import Enum

class ScanStatus(Enum):
    SCAN_RUNNING = 1
    SCAN_COMPLETED = 2
    SCAN_FAILED = 3
    SCAN_ABORTED = 4
