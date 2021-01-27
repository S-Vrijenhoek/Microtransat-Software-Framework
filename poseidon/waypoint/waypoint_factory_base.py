from abc import ABC, abstractmethod


class WaypointFactoryBase(ABC):

    @staticmethod
    @abstractmethod
    def create_waypoints(settings_location: str) -> list:
        pass
