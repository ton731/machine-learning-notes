from abc import ABC, abstractmethod
from beverage import Beverage


class CondimentDecorator(Beverage):

    beverage: Beverage

    @abstractmethod
    def get_description(self) -> str:
        raise NotImplementedError


class Mocha(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage
    
    def get_description(self) -> str:
        return self.beverage.get_description() + ", Mocha"

    def cost(self) -> float:
        return self.beverage.cost() + 0.2
    

class Milk(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage
    
    def get_description(self) -> str:
        return self.beverage.get_description() + ", Milk"

    def cost(self) -> float:
        return self.beverage.cost() + 0.1


class Soy(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage
    
    def get_description(self) -> str:
        return self.beverage.get_description() + ", Soy"

    def cost(self) -> float:
        return self.beverage.cost() + 0.15


class Whip(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage
    
    def get_description(self) -> str:
        return self.beverage.get_description() + ", Whip"

    def cost(self) -> float:
        return self.beverage.cost() + 0.1
