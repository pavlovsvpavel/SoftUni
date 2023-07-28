from typing import List
from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    VALID_CAR_TYPES = {
        "MuscleCar": MuscleCar,
        "SportsCar": SportsCar
    }

    def __init__(self):
        self.cars: List[Car] = []
        self.drivers: List[Driver] = []
        self.races: List[Race] = []

    def __find_valid_driver(self, name):
        for driver in self.drivers:
            if driver.name == name:
                return driver

        raise Exception(f"Driver {name} could not be found!")

    def __find_valid_race(self, name):
        for race in self.races:
            if race.name == name:
                return race

        raise Exception(f"Race {name} could not be found!")

    def create_car(self, car_type: str, model: str, speed_limit: int) -> str:

        for car in self.cars:
            if car.model == model:
                raise Exception(f"Car {model} is already created!")

        if car_type in Controller.VALID_CAR_TYPES:
            current_car = Controller.VALID_CAR_TYPES[car_type](model, speed_limit)
            self.cars.append(current_car)

            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str) -> str:
        for driver in self.drivers:
            if driver.name == driver_name:
                raise Exception(f"Driver {driver_name} is already created!")

        current_driver = Driver(driver_name)

        self.drivers.append(current_driver)

        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str) -> str:
        for race in self.races:
            if race.name == race_name:
                raise Exception(f"Race {race_name} is already created!")

        current_race = Race(race_name)

        self.races.append(current_race)

        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str) -> str:
        current_driver = self.__find_valid_driver(driver_name)

        try:
            current_car = [car for car in self.cars
                           if car.__class__.__name__ == car_type
                           and not car.is_taken][-1]
        except IndexError:
            raise Exception(f"Car {car_type} could not be found!")

        if current_driver.car:
            old_model = current_driver.car.model
            current_driver.car.is_taken = not current_driver.car.is_taken

            new_model = current_car.model
            current_driver.car = current_car
            current_car.is_taken = not current_car.is_taken

            return f"Driver {driver_name} changed his car from {old_model} to {new_model}."

        current_driver.car = current_car
        current_driver.car.is_taken = not current_driver.car.is_taken

        return f"Driver {driver_name} chose the car {current_car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str) -> str:
        current_race = self.__find_valid_race(race_name)
        current_driver = self.__find_valid_driver(driver_name)

        if not current_driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        for driver in current_race.drivers:
            if driver.name == driver_name:
                return f"Driver {driver_name} is already added in {race_name} race."

        current_race.drivers.append(current_driver)

        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str) -> str:
        current_race = self.__find_valid_race(race_name)

        if len(current_race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        top_three_cars = sorted(self.cars, key=lambda x: -x.speed_limit)

        result = []

        for car in top_three_cars[:3]:
            for driver in self.drivers:
                if driver.car == car:
                    driver.number_of_wins += 1
                    result.append(f"Driver {driver.name} wins the {race_name} race with a speed of {car.speed_limit}.")

        return "\n".join(result)
