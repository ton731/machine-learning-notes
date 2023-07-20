from typing import List

from subject import Subject
from observer import Observer


class WeatherData(Subject):

    __observers: List[Observer]
    __temperature: float
    __humidity: float
    __pressure: float

    def __init__(self):
        self.__observers = []

    def register_observer(self, o: Observer) -> None:
        self.__observers.append(o)
    
    def remove_observer(self, o: Observer) -> None:
        self.__observers.remove(o)
    
    def notify_observers(self) -> None:
        for observer in self.__observers:
            observer.update()
    
    def measurements_changed(self) -> None:
        self.notify_observers()

    def set_measurements(self, temperature: float, humidity: float, pressure: float) -> None:
        self.__temperature = temperature
        self.__humidity = humidity
        self.__pressure = pressure
        self.measurements_changed()

    def get_temperature(self) -> float:
        return self.__temperature
    
    def get_humidity(self) -> float:
        return self.__humidity
    
    def get_pressure(self) -> float:
        return self.__pressure
