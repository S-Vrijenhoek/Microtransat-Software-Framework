from abc import ABC, abstractmethod


class ComputationBase(ABC):

    # TODO: Implement algorithm
    @abstractmethod
    def compute_optimal_saling_angle(self, sailboat_rotation: float, wind_direction: float):
        pass
