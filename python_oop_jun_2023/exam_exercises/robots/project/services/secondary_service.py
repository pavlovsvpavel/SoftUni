from project.services.base_service import BaseService


class SecondaryService(BaseService):

    def __init__(self, name: str):
        super().__init__(name, 15)

    def details(self):
        result = [f"{self.name} Secondary Service:"]
        robots = ["Robots:"]

        if self.robots:
            for robot in self.robots:
                robots.append(robot.name)

        else:
            robots.append("none")

        result.append(" ".join(robots))

        return "\n".join(result)
