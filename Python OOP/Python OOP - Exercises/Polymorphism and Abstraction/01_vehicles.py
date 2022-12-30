from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: float):
        ...

    @abstractmethod
    def refuel(self, fuel: float):
        ...


class Car(Vehicle):
    CONDITIONER_USE = 0.9

    def drive(self, distance: float):
        current_trip = (self.fuel_consumption + Car.CONDITIONER_USE) * distance

        if self.fuel_quantity - current_trip >= 0:
            self.fuel_quantity -= current_trip
    
    def refuel(self, fuel: float):
        self.fuel_quantity += fuel
        


class Truck(Vehicle):
    CONDITIONER_USE = 1.6

    def drive(self, distance: float):
        current_trip = (self.fuel_consumption + Truck.CONDITIONER_USE) * distance

        if self.fuel_quantity - current_trip >= 0:
            self.fuel_quantity -= current_trip

    def refuel(self, fuel: float):
        self.fuel_quantity += fuel * 0.95
