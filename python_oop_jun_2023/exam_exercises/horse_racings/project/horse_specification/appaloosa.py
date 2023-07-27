from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    max_speed = 120

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self) -> None:
        self.speed = min(Appaloosa.max_speed, self.speed + 2)
