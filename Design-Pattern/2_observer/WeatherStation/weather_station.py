from weather_data import WeatherData
from display import CurrentConditionsDisplay, StatisticsDisplay, ForecastDisplay


class WeatherStation:

    @staticmethod
    def main():

        weather_data = WeatherData()
        current_display = CurrentConditionsDisplay(weather_data)
        statistics_display = StatisticsDisplay(weather_data)
        forecast_display = ForecastDisplay(weather_data)

        weather_data.set_measurements(80, 65, 30.4)
        weather_data.set_measurements(82, 70, 29.2)
        weather_data.set_measurements(78, 90, 29.2)

        weather_data.remove_observer(forecast_display)
        weather_data.set_measurements(90, 80, 30.0)


if __name__ == "__main__":
    WeatherStation.main()
