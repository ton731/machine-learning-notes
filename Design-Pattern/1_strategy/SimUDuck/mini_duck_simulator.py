from duck import RubberDuck, RedHeadDuck, DecoyDuck
from fly_behavior import FlyRocketPowered


class MiniDuckSimulator:
    @staticmethod
    def main(*args):
        
        rubber_duck = RubberDuck()
        red_head_duck = RedHeadDuck()
        decoy_duck = DecoyDuck()

        rubber_duck.perform_quack()
        red_head_duck.perform_quack()
        decoy_duck.perform_quack()

        rubber_duck.perform_fly()
        red_head_duck.perform_fly()
        decoy_duck.perform_fly()
        decoy_duck.set_fly_behavior(FlyRocketPowered())
        decoy_duck.perform_fly()   


if __name__ == "__main__":
    MiniDuckSimulator.main()
