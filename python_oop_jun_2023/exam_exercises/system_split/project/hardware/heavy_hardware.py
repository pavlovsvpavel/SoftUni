from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    __CAPACITY = 2
    __MEMORY = 0.75
    __TYPE = "Heavy"

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, HeavyHardware.__TYPE, capacity * HeavyHardware.__CAPACITY,
                         int(memory * HeavyHardware.__MEMORY))
