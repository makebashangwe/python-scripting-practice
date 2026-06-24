class DriveManager:
    def __init__(self, drive_pool):
        self.drive_pool = drive_pool

    def run_diagnostics(self):
        for drive in self.drive_pool:
            print(drive.get_telemetry())


class StorageDrive:
    def __init__(self, serial_number: str, capacity_tb: int):
        self.serial_number = serial_number
        self.capacity_tb = capacity_tb

    def get_telemetry(self):
        return "Generic Drive OK"


class SSD(StorageDrive):
    def __init__(self, serial_number: str, capacity_tb: int, nvme_version: str):
        super().__init__(serial_number, capacity_tb)
        self.nvme_version = nvme_version

    def get_telemetry(self):
        return f"SSD : {self.serial_number} - NVMe Version: {self.nvme_version} - Wear Level: Nominal"


class HDD(StorageDrive):
    def __init__(self, serial_number: str, capacity_tb: int, rpm_speed: int):
        super().__init__(serial_number, capacity_tb)
        self.rpm_speed = rpm_speed

    def get_telemetry(self):
        return f"HDD : {self.serial_number} - RPM Speed: {self.rpm_speed} - Spindle Vibration: Normal"


nvme_drive = SSD("SN-A1B2", 2, "PCIe 4.0")
spindle_drive = HDD("SN-X9Y8", 16, 7200)
drive_pool = nvme_drive, spindle_drive
manager = DriveManager(drive_pool)
manager.run_diagnostics()

