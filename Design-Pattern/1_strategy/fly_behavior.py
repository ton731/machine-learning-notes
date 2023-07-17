from abc import ABC, abstractmethod


class FlyBehavior(ABC):
    @abstractmethod
    def fly(self) -> None:
        raise NotImplementedError
    

class FlyWithWings(FlyBehavior):
    def fly(self) -> None:
        print("I'm flying!")


class FlyNoWay(FlyBehavior):
    def fly(self) -> None:
        print("I can't fly...")


class FlyRocketPowered(FlyBehavior):
    def fly(self) -> None:
        print("Flying with rocket power!!!")