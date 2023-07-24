from unittest import TestCase, main
from project.robot import Robot


class TestRobot(TestCase):
    def setUp(self) -> None:
        self.robot = Robot("my_id", "Military", 100, 50.5)

    def test_class_attributes(self):
        expected = ['Military', 'Education', 'Entertainment', 'Humanoids']
        self.assertEqual(expected, Robot.ALLOWED_CATEGORIES)

        self.assertEqual(1.5, Robot.PRICE_INCREMENT)

    def test_successful_initialization(self):
        self.assertEqual("my_id", self.robot.robot_id)
        self.assertEqual("Military", self.robot.category)
        self.assertEqual(100, self.robot.available_capacity)
        self.assertEqual(50.5, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_category_not_in_allowed_categories_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Sport"

        expected = f"Category should be one of '{Robot.ALLOWED_CATEGORIES}'"
        self.assertEqual(expected, str(ve.exception))

    def test_negative_price_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -1

        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_upgrade_with_existing_hardware(self):
        self.robot.hardware_upgrades = ["cpu"]
        result = self.robot.upgrade("cpu", 10.5)

        self.assertEqual("Robot my_id was not upgraded.", result)

    def test_upgrade_with_non_existing_hardware(self):
        result = self.robot.upgrade("ram", 5.5)

        self.assertEqual(["ram"], self.robot.hardware_upgrades)
        self.assertEqual(58.75, self.robot.price)

        self.assertEqual("Robot my_id was upgraded with ram.", result)

    def test_update_with_lower_or_equal_software_version(self):
        self.robot.software_updates = [2.0, 3.5, 3.8]
        result = self.robot.update(3.5, 80)

        self.assertEqual("Robot my_id was not updated.", result)

    def test_update_with_less_capacity_than_needed(self):
        result = self.robot.update(1.5, 150)

        self.assertEqual("Robot my_id was not updated.", result)

    def test_successful_update(self):
        result = self.robot.update(2.5, 50)

        self.assertEqual([2.5], self.robot.software_updates)
        self.assertEqual(50, self.robot.available_capacity)

        expected = "Robot my_id was updated to version 2.5."
        self.assertEqual(expected, result)

    def test_gt_method_price_first_robot_is_greater_than_second_robot(self):
        other = Robot("new_id", "Education", 100, 20.5)
        result = self.robot.__gt__(other)

        expected = "Robot with ID my_id is more expensive than Robot with ID new_id."

        self.assertEqual(expected, result)

    def test_gt_method_price_first_robot_is_equal_to_second_robot(self):
        other = Robot("new_id", "Education", 100, 50.5)
        result = self.robot.__gt__(other)

        expected = "Robot with ID my_id costs equal to Robot with ID new_id."

        self.assertEqual(expected, result)

    def test_gt_method_price_first_robot_is_less_than_second_robot(self):
        other = Robot("new_id", "Education", 100, 100.5)
        result = self.robot.__gt__(other)

        expected = "Robot with ID my_id is cheaper than Robot with ID new_id."

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
