from abc import ABC
from car import Car
from datetime import datetime


class CarriganTire(Car, ABC):
    def __init__(self, tire_sensor_data):
        super().__init__(tire_sensor_data)

    def tires_should_be_serviced(self):
        if np.any(i>0.9 for i in tire_sensor_data):
            return True
        else:
            return False