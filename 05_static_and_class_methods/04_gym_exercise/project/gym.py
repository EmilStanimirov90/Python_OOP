from typing import List

from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = self.__find_obj(subscription_id, self.subscriptions)
        customer = next((c for c in self.customers if c.id == subscription.customer_id), None)
        trainer = next((t for t in self.trainers if t.id == subscription.trainer_id), None)
        # trainer = self.__find_obj(subscription_id, self.trainers)
        plan = next((p for p in self.plans if p.id == subscription.exercise_id), None)
        equipment = next((e for e in self.equipment if e.id == plan.equipment_id), None)
        return '\n'.join([subscription.__repr__(),
                          customer.__repr__(),
                          trainer.__repr__(),
                          equipment.__repr__(),
                          plan.__repr__(),
                          ])

    @staticmethod
    def __find_obj(obj_id, obj_collection):
        return next((o for o in obj_collection if o.id == obj_id), None)
