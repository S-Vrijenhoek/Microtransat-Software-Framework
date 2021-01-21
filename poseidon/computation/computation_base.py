from abc import ABC, abstractmethod


class ComputationBase(ABC):

    @abstractmethod
    def compute_optimal_sailing_angle(self, sailboat_rotation: float, wind_direction: float) -> float:
        pass

    @abstractmethod
    def compute_optimal_rudder_angle(self, sailboat_position: list,
                                     sailboat_rotation: float,
                                     rudder_rotation: float,
                                     wind_direction: float) -> float:
        pass
