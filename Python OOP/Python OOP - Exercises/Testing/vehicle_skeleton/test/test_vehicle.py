from unittest import TestCase, main
from project.vehicle import Vehicle



class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(7.8, 101.1)

    def test_args_are_correct_value_types(self):
        self.assertIs(float, type(self.vehicle.DEFAULT_FUEL_CONSUMPTION))
        self.assertIs(float, type(self.vehicle.fuel_consumption))
        self.assertIs(float, type(self.vehicle.fuel))
        self.assertIs(float, type(self.vehicle.capacity))
        self.assertIs(float, type(self.vehicle.horse_power))

    def test_initialising_values_correctly_set(self):
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)
        self.assertEqual(7.8, self.vehicle.fuel)
        self.assertEqual(101.1, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.capacity, self.vehicle.fuel)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_for_reise_exception_if_not_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(10)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_with_enough_fuel_expect_fuel_reduce_with_consumption(self):
        self.vehicle.fuel = 20
        self.vehicle.drive(8)
        result = self.vehicle.fuel
        expected_result = 10
        self.assertEqual(expected_result, result)

    def test_refuel_with_fuel_quantity_more_than_tank_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_with_quantity_less_than_tank_capacity(self):
        self.vehicle.fuel = 5
        self.vehicle.refuel(2.8)
        result = self.vehicle.fuel
        expected_result = 7.8
        self.assertEqual(expected_result, result)

    def test_string_represent_for_correct_mesage(self):
        result = str(self.vehicle)
        expected_result = "The vehicle has 101.1 " \
               "horse power with 7.8 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()
