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

    @staticmethod
    def add_to_list(element, lst) -> None:
        if element not in lst:
            lst.append(element)

    def add_customer(self, customer: Customer) -> None:
        return self.add_to_list(customer, self.customers)

    def add_trainer(self, trainer: Trainer) -> None:
        return self.add_to_list(trainer, self.trainers)

    def add_equipment(self, equipment: Equipment) -> None:
        return self.add_to_list(equipment, self.equipment)

    def add_plan(self, plan: ExercisePlan) -> None:
        return self.add_to_list(plan, self.plans)

    def add_subscription(self, subscription: Subscription) -> None:
        return self.add_to_list(subscription, self.subscriptions)

    def subscription_info(self, subscription_id: int):
        try:
            c_subscription = next(filter(lambda x: x.id == subscription_id, self.subscriptions))
        except StopIteration:
            return "No such subscription id"

        current_id = c_subscription.id

        result = [
            [subscription for subscription in self.subscriptions if subscription.id == current_id],
            [customer for customer in self.customers if customer.id == current_id],
            [trainer for trainer in self.trainers if trainer.id == current_id],
            [equipment for equipment in self.equipment if equipment.id == current_id],
            [plan for plan in self.plans if plan.id == current_id],
        ]

        return "\n".join(''.join(map(str, el)) for el in result)



