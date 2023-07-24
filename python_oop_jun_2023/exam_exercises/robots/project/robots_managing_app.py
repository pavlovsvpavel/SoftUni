from typing import List
from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    _VALID_SERVICES = {
        "MainService": MainService,
        "SecondaryService": SecondaryService
    }

    _VALID_ROBOTS = {
        "FemaleRobot": FemaleRobot,
        "MaleRobot": MaleRobot
    }

    _VALID_MATCHES = {
        "MaleRobot": "MainService",
        "FemaleRobot": "SecondaryService"
    }

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def add_service(self, service_type: str, name: str) -> str:
        try:
            service = RobotsManagingApp._VALID_SERVICES[service_type](name)
        except KeyError:
            raise Exception("Invalid service type!")

        self.services.append(service)

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float) -> str:
        try:
            robot = RobotsManagingApp._VALID_ROBOTS[robot_type](name, kind, price)
        except KeyError:
            raise Exception("Invalid robot type!")

        self.robots.append(robot)

        return f"{robot_type} is successfully added."

    def __robot_name_to_object(self, robot_name):
        for robot in self.robots:
            if robot.name == robot_name:
                return robot

    def __service_name_to_object(self, service_name):
        for service in self.services:
            if service.name == service_name:
                return service

    def add_robot_to_service(self, robot_name: str, service_name: str) -> str:
        current_robot = self.__robot_name_to_object(robot_name)
        current_service = self.__service_name_to_object(service_name)

        if current_service.capacity == len(current_service.robots):
            raise Exception("Not enough capacity for this robot!")

        if not RobotsManagingApp._VALID_MATCHES[current_robot.robot_type] == current_service.service_type:
            return "Unsuitable service."

        current_service.robots.append(current_robot)
        self.robots.remove(current_robot)

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str) -> str:
        current_service = self.__service_name_to_object(service_name)

        for robot in current_service.robots:
            if robot.name == robot_name:
                current_service.robots.remove(robot)
                self.robots.append(robot)

                return f"Successfully removed {robot_name} from {service_name}."

        raise Exception("No such robot in this service!")

    def feed_all_robots_from_service(self, service_name: str) -> str:
        current_service = self.__service_name_to_object(service_name)

        for robot in current_service.robots:
            robot.eating()

        return f"Robots fed: {len(current_service.robots)}."

    def service_price(self, service_name: str) -> str:
        current_service = self.__service_name_to_object(service_name)

        total_price = 0
        for robot in current_service.robots:
            total_price += robot.price

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self) -> str:
        return "\n".join(service.details() for service in self.services)
