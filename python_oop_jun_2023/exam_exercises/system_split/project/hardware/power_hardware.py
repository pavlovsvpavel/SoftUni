from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    __CAPACITY = 0.25
    __MEMORY = 1.75
    __TYPE = "Power"

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, PowerHardware.__TYPE, int(capacity * PowerHardware.__CAPACITY),
                         int(memory * PowerHardware.__MEMORY))
