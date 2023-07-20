from abc import ABC, abstractmethod
from fly_behavior import FlyBehavior, FlyWithWings, FlyNoWay
from quack_behavior import QuackBehavior, Quack, MuteQuack, Squeak


class Duck(ABC):

    fly_behavior: FlyBehavior
    quack_behavior: QuackBehavior

    def perform_fly(self) -> None:
        self.fly_behavior.fly()
    
    def perform_quack(self) -> None:
        self.quack_behavior.quack()
    
    def set_fly_behavior(self, fb: FlyBehavior) -> None:
        self.fly_behavior = fb
    
    def set_quack_behavior(self, qb: QuackBehavior) -> None:
        self.quack_behavior = qb
    
    def swim(self) -> None:
        print("All ducks float, even decoys!")
    
    @abstractmethod
    def display(self) -> None:
        raise NotImplementedError


class RubberDuck(Duck):
    def __init__(self) -> None:
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Squeak()

    def display(self) -> None:
        print("I'm a rubber duck!")


class RedHeadDuck(Duck):
    def __init__(self) -> None:
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()
    
    def display(self) -> None:
        print("I'm a red head duck!")


class DecoyDuck(Duck):
    def __init__(self) -> None:
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = MuteQuack()
    
    def display(self) -> None:
        print("I'm a duck decoy!")

