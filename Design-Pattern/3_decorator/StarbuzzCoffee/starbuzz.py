from beverage import Beverage, Espresso, DarkRoast, HouseBlend
from condiment_decorator import Mocha, Whip, Soy, Milk

class Starbuzz:

    @staticmethod
    def main():

        beverage: Beverage = Espresso()
        print(beverage.get_description() + " $" + str(beverage.cost()))

        beverage2: Beverage = DarkRoast()
        beverage2 = Mocha(beverage2)
        beverage2 = Mocha(beverage2)
        beverage2 = Whip(beverage2)
        print(beverage2.get_description() + " $" + str(beverage2.cost()))

        beverage3: Beverage = HouseBlend()
        beverage3 = Soy(beverage3)
        beverage3 = Milk(beverage3)
        beverage3 = Whip(beverage3)
        print(beverage3.get_description() + " $" + str(beverage3.cost()))
    

if __name__ == "__main__":
    Starbuzz.main()
