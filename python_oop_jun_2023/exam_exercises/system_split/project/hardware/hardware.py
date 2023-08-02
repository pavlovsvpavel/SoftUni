from abc import ABC
from typing import List
from project.software.software import Software


class Hardware(ABC):
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components: List[Software] = []

    def install(self, software: Software) -> None or Exception:
        total_memory_consumption = (sum(soft.memory_consumption for soft in self.software_components) +
                                    software.memory_consumption)
        total_capacity_consumption = (sum(soft.capacity_consumption for soft in self.software_components) +
                                      software.capacity_consumption)

        if total_capacity_consumption > self.capacity or total_memory_consumption > self.memory:
            raise Exception("Software cannot be installed")

        self.software_components.append(software)

    def uninstall(self, software: Software) -> None:
        self.software_components.remove(software)

    def __str__(self):
        result = []

        express_software = [soft for soft in self.software_components if soft.software_type == 'Express']
        light_software = [soft for soft in self.software_components if soft.software_type == 'Light']
        software_memory = [soft.memory_consumption for soft in self.software_components]
        software_capacity = [soft.capacity_consumption for soft in self.software_components]
        software_components = [soft.name for soft in self.software_components]

        result.append(
            f"Hardware Component - {self.name}\n"
            f"Express Software Components: {len(express_software)}\n"
            f"Light Software Components: {len(light_software)}\n"
            f"Memory Usage: {sum(software_memory)} / {self.memory}\n"
            f"Capacity Usage: {sum(software_capacity)} / {self.capacity}\n"
            f"Type: {self.hardware_type}\n"
            f"Software Components: {', '.join(software_components) if software_components else 'None'}"
        )

        return "\n".join(result)



