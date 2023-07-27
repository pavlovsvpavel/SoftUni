from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    max_speed = 140

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self) -> None:
        self.speed = min(Thoroughbred.max_speed, self.speed + 3)
