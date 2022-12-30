from abc import ABC, abstractmethod
from project.food import Food

class Animal(ABC):
    EATEN_FOOD = 0

    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = Animal.EATEN_FOOD

    @abstractmethod
    def make_sound(self):
        ...

    def feed(self, food: Food):
        eated_foods = {
            "Hen": ("Vegetable", "Fruit", "Meat", "Seed"),
            "Mouse": ("Vegetable", "Fruit"),
            "Cat": ("Vegetable", "Meat"),
            "Tiger": "Meat",
            "Dog": "Meat",
            "Owl": "Meat"
        }

        current_food_type = food.__class__.__name__
        current_animal = self.__class__.__name__

        if not current_food_type in eated_foods[current_animal]:
            return f"{current_animal} does not eat {current_food_type}!"

        self.weight += self.increase_animals_weight(current_animal) * food.quantity
        self.food_eaten += food.quantity

    def increase_animals_weight(self, animal_type: str):
        increase_per_piece = {
            "Hen": 0.35,
            "Mouse": 0.10,
            "Cat": 0.30,
            "Tiger": 1.00,
            "Dog": 0.40,
            "Owl": 0.25
        }

        return increase_per_piece[animal_type]      


class Bird(Animal, ABC):

    @abstractmethod
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    
    @abstractmethod
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
