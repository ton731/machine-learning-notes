from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def update() -> None:
        raise NotImplementedError