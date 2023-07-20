from observer import Observer
from display_element import DisplayElement
from weather_data import WeatherData


class CurrentConditionsDisplay(Observer, DisplayElement):

    __temperature: float
    __humidity: float
    __weather_data: WeatherData

    def __init__(self, weather_data: WeatherData):
        self.__weather_data = weather_data
        self.__weather_data.register_observer(self)

    def update(self) -> None:
        self.__temperature = self.__weather_data.get_temperature()
        self.__humidity = self.__weather_data.get_humidity()
        self.display()

    def display(self) -> None:
        print(f"Current conditions: {self.__temperature:.1f}F degrees and {self.__humidity:.1f}%")



class StatisticsDisplay(Observer, DisplayElement):

    __max_temperature: float = 0.0
    __min_temperature: float = 500.0
    __sum_temperature: float = 0.0
    __num_record: int = 0
    __weather_data: WeatherData

    def __init__(self, weather_data: WeatherData):
        self.__weather_data = weather_data
        self.__weather_data.register_observer(self)

    def update(self) -> None:
        temperature = self.__weather_data.get_temperature()
        if temperature > self.__max_temperature:
            self.__max_temperature = temperature
        if temperature < self.__min_temperature:
            self.__min_temperature = temperature
        self.__sum_temperature += temperature
        self.__num_record += 1
        self.display()

    def display(self) -> None:
        print(f"Avg/Max/Min temperature = {self.__sum_temperature / self.__num_record:.1f}/{self.__max_temperature:.1f}/{self.__min_temperature:.1f}")

    

class ForecastDisplay(Observer, DisplayElement):

    __last_pressure: float
    __current_pressure: float = 29.0
    __weather_data: WeatherData

    def __init__(self, weather_data: WeatherData):
        self.__weather_data = weather_data
        self.__weather_data.register_observer(self)

    def update(self) -> None:
        self.__last_pressure = self.__current_pressure
        self.__current_pressure = self.__weather_data.get_pressure()
        self.display()

    def display(self) -> None:
        print("Forecast: ", end="")
        if self.__current_pressure > self.__last_pressure:
            print("Improving weather on the way!")
        elif self.__current_pressure == self.__last_pressure:
            print("More of the same")
        elif self.__current_pressure < self.__last_pressure:
            print("Watch out for cooler, rainy weather")