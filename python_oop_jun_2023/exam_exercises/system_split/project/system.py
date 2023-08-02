from typing import List
from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.software.software import Software


class System:
    _hardware: List[Hardware] = []
    _software: List[Software] = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        new_hardware = PowerHardware(name, capacity, memory)

        System._hardware.append(new_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        new_hardware = HeavyHardware(name, capacity, memory)

        System._hardware.append(new_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = next(filter(lambda x: x.name == hardware_name, System._hardware))
        except StopIteration:
            return "Hardware does not exist"

        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)

        hardware.install(express_software)
        System._software.append(express_software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = next(filter(lambda x: x.name == hardware_name, System._hardware))
        except StopIteration:
            return "Hardware does not exist"

        light_software = LightSoftware(name, capacity_consumption, memory_consumption)

        hardware.install(light_software)
        System._software.append(light_software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            hardware = next(filter(lambda x: x.name == hardware_name, System._hardware))
            software = next(filter(lambda x: x.name == software_name, System._software))
        except StopIteration:
            return "Some of the components do not exist"

        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():

        result = [
            f"System Analysis",
            f"Hardware Components: {len(System._hardware)}",
            f"Software Components: {len(System._software)}",
            f"Total Operational Memory: {sum([soft.memory_consumption for soft in System._software])} / "
            f"{sum([hard.memory for hard in System._hardware])}",
            f"Total Capacity Taken: {sum([soft.capacity_consumption for soft in System._software])} / "
            f"{sum([hard.capacity for hard in System._hardware])}"
        ]

        return "\n".join(result)

    @staticmethod
    def system_split():
        return "\n".join(str(hard) for hard in System._hardware)
