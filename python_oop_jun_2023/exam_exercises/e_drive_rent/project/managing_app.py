from typing import List
from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    _VALID_VEHICLES = {
        "PassengerCar": PassengerCar,
        "CargoVan": CargoVan
    }

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def __check_for_existing_driving_license(self, driving_license_num):
        for user in self.users:
            if user.driving_license_number == driving_license_num:
                return True

        return False

    def __check_for_existing_license_plate(self, vehicle: BaseVehicle):
        for v in self.vehicles:
            if v.license_plate_number == vehicle.license_plate_number:
                return True

        return False

    def __check_for_existing_route_length(self, start, end, length):
        for r in self.routes:
            if r.start_point == start and r.end_point == end:
                if r.length < length:
                    return f"{start}/{end} shorter route had already been added to our platform."

                if r.length == length:
                    return f"{start}/{end} - {length} km had already been added to our platform."

                r.is_locked = True

        return False

    def register_user(self, first_name: str, last_name: str, driving_license_number: str) -> str:
        if self.__check_for_existing_driving_license(driving_license_number):
            return f"{driving_license_number} has already been registered to our platform."

        new_user = User(first_name, last_name, driving_license_number)
        self.users.append(new_user)

        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str) -> str:
        try:
            vehicle = ManagingApp._VALID_VEHICLES[vehicle_type](brand, model, license_plate_number)
        except KeyError:
            return f"Vehicle type {vehicle_type} is inaccessible."

        if self.__check_for_existing_license_plate(vehicle):
            return f"{license_plate_number} belongs to another vehicle."

        else:
            self.vehicles.append(vehicle)
            return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float) -> str:
        current_route_id = len(self.routes) + 1

        current_route = Route(start_point, end_point, length, current_route_id)

        message = self.__check_for_existing_route_length(start_point, end_point, length)

        if not message:
            self.routes.append(current_route)

            return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

        return message

    def __user_as_object(self, driving_license) -> User:
        for user in self.users:
            if user.driving_license_number == driving_license:
                return user

    def __vehicle_as_object(self, license_plate) -> BaseVehicle:
        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate:
                return vehicle

    def __route_as_object(self, route_id) -> Route:
        for route in self.routes:
            if route.route_id == route_id:
                return route

    def make_trip(self, driving_license_number: str, license_plate_number: str,
                  route_id: int, is_accident_happened: bool) -> str:

        current_user = self.__user_as_object(driving_license_number)
        current_vehicle = self.__vehicle_as_object(license_plate_number)
        current_route = self.__route_as_object(route_id)

        if current_user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if current_vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if current_route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        current_vehicle.drive(current_route.length)

        if is_accident_happened:
            current_vehicle.change_status()
            current_user.decrease_rating()

        else:
            current_user.increase_rating()

        return f"{current_vehicle.__str__()}"

    def repair_vehicles(self, count: int) -> str:
        sorted_vehicles = sorted(self.vehicles, key=lambda x: (x.brand, x.model))
        vehicles_for_repair = []

        for vehicle in sorted_vehicles:
            if vehicle.is_damaged and len(vehicles_for_repair) < count:
                vehicles_for_repair.append(vehicle)
                vehicle.change_status()
                vehicle.recharge()

        return f"{len(vehicles_for_repair)} vehicles were successfully repaired!"

    def users_report(self) -> str:
        result = ["*** E-Drive-Rent ***",
                  '\n'.join(user.__str__() for user in sorted(self.users, key=lambda x: (-x.rating)))]

        return '\n'.join(result)
