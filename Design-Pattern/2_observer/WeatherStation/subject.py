from abc import ABC, abstractmethod
from observer import Observer


class Subject(ABC):

    @abstractmethod
    def register_observer(self, o: Observer) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def remove_observer(self, o: Observer) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def notify_observers(self) -> None:
        raise NotImplemented

