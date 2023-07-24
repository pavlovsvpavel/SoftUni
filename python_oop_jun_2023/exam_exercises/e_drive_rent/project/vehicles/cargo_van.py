from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    MAX_MILEAGE = 180.00
    ADDITIONAL_LOAD_BATTERY_DECREASE = 5

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, CargoVan.MAX_MILEAGE)

    def drive(self, mileage: float):
        reduce_percentage = round(mileage / CargoVan.MAX_MILEAGE * 100)

        self.battery_level -= (reduce_percentage + CargoVan.ADDITIONAL_LOAD_BATTERY_DECREASE)
