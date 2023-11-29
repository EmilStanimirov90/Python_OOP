from typing import List, Union
from project import Animal
from project import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int):
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        if self.__budget < price:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = 0
        for worker in self.workers:
            total_salaries += worker.salary
        # total_salaries = sum([w.salary for w in self.workers])
        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_cost_for_animals = 0
        for animal in self.animals:
            total_cost_for_animals += animal.money_money_for_care
        if self.__budget >= total_cost_for_animals:
            self.__budget -= total_cost_for_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount) -> None:
        self.__budget += amount

    def animals_status(self):
        return self.__print_status(self.animals, "Lion", "Tiger", "Cheetah")
        # lions = []
        # tigers = []
        # cheetahs = []
        # for animal in self.animals:
        #     if animal.__class__.__name__ == "Lion":
        #         lions.append(repr(animal))
        #     elif animal.__class__.__name__ == "Tiger":
        #         tigers.append(repr(animal))
        #     elif animal.__class__.__name__ == "Cheetah":
        #         cheetahs.append(repr(animal))
        #
        # result = [f"You have {len(self.animals)} animals", f"----- {len(lions)} Lions:"]
        # result.extend(lions)
        # result.append(f"----- {len(tigers)} Tigers:")
        # result.extend(tigers)
        # result.append(f"----- {len(cheetahs)} Cheetahs:")
        # result.extend(cheetahs)
        #
        # return '\n'.join(result)

    def workers_status(self):
        return self.__print_status(self.workers, "Keeper", "Caretaker", "Vet")

        # keepers = []
        # caretakers = []
        # vets = []
        # for worker in self.workers:
        #     if worker.__class__.__name__ == "Keeper":
        #         keepers.append(repr(worker))
        #     elif worker.__class__.__name__ == "Caretaker":
        #         caretakers.append(repr(worker))
        #     elif worker.__class__.__name__ == "Vet":
        #         vets.append(repr(worker))
        #
        # result = [f"You have {len(self.workers)} workers", f"----- {len(keepers)} Keepers:"]
        # result.extend(keepers)
        # result.append(f"----- {len(caretakers)} Caretakers:")
        # result.extend(caretakers)
        # result.append(f"----- {len(vets)} Vets:")
        # result.extend(vets)
        #
        # return '\n'.join(result)

    @staticmethod
    def __print_status(category: List[Union[Animal, Worker]], *args):
        elements = {arg: [] for arg in args}
        for element in category:
            elements[element.__class__.__name__].append(repr(element))

        result = [f"You have {len(category)} {str(category[0].__class__.__base__[0].__name__).lower()}s"]
        for key, value in elements.items():
            result.append(f"----- {len(value)} {key}:")
            result.extend(value)
        return "\n".join(result)
