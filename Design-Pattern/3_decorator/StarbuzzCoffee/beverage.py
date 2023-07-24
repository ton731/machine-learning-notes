from abc import ABC, abstractmethod


class Beverage(ABC):

    description: str = "Unknown beverage..."

    def get_description(self) -> str:
        return self.description
    
    @abstractmethod
    def cost(self) -> float:
        raise NotImplementedError
    


class Espresso(Beverage):
    def __init__(self):
        self.description = "Espresso"
    
    def cost(self) -> float:
        return 1.99


class HouseBlend(Beverage):
    def __init__(self):
        self.description = "House Blend Coffee"
    
    def cost(self) -> float:
        return 0.89


class DarkRoast(Beverage):
    def __init__(self):
        self.description = "Dark Roast Coffee"
    
    def cost(self) -> float:
        return 0.99


class Decaf(Beverage):
    def __init__(self):
        self.description = "Decaf Coffee"
    
    def cost(self) -> float:
        return 1.05
