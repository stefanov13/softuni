from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: int, budget: int, animal_capacity: int, worker_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = worker_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price: float):
        if self.__budget - price < 0:
            return "Not enough budget"

        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"

        self.animals.append(animal)
        self.__budget -= price

        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
    
    def hire_worker(self, worker: Worker):
        if self.__workers_capacity == len(self.workers):
            return "Not enough space for worker"
        
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str):
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        
        return f"{worker_name} fired successfully"
        
    def pay_workers(self):
        salaries_sum = sum(worker.salary for worker in self.workers)
        if self.__budget - salaries_sum < 0:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= salaries_sum

        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        animal_care_sum = sum(animal.money_for_care for animal in self.animals)
        if self.__budget - animal_care_sum < 0:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= animal_care_sum

        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        lions = list(filter(lambda w: w.__class__.__name__ == "Lion", self.animals))
        tigers = list(filter(lambda w: w.__class__.__name__ == "Tiger", self.animals))
        cheetahs = list(filter(lambda w: w.__class__.__name__ == "Cheetah", self.animals))

        animal_output = [
            f"You have {len(self.animals)} animals",
            f"----- {len(lions)} Lions:"
        ]    
        animal_output.extend(lions)
        
        animal_output.append(f"----- {len(tigers)} Tigers:")
        animal_output.extend(tigers)
        
        animal_output.append(f"----- {len(cheetahs)} Cheetahs:")
        animal_output.extend(cheetahs)

        return "\n".join(str(a_o) for a_o in animal_output)

    def workers_status(self):
        workers_info = {"Keeper": [], "Caretaker": [], "Vet": []}
        [workers_info[x.__class__.__name__].append(str(x)) for x in self.workers]

        workers_output = [
            f"You have {len(self.workers)} workers",
            f"----- {len(workers_info['Keeper'])} Keepers:",
            *workers_info['Keeper'],
            f"----- {len(workers_info['Caretaker'])} Caretakers:",
            *workers_info["Caretaker"],
            f"----- {len(workers_info['Vet'])} Vets:",
            *workers_info["Vet"],
        ]

        return "\n".join(workers_output)
