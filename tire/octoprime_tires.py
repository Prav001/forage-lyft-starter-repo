from abc import ABC
from car import Car
from datetime import datetime


class OctoprimeTire(Car, ABC):
    def __init__(self, tire_sensor_data):
        super().__init__(tire_sensor_data)

    def tires_should_be_serviced(self):
        if np.sum(tire_sensor_data)>=3:
            return True
        else:
            return False

