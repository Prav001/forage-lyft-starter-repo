from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, last_service_date,tire_sensor_data):
        self.last_service_date = last_service_date
        self.tire_sensor_data = tire_sensor_data

    @abstractmethod
    def needs_service(self):
        pass
