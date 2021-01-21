from abc import ABC, abstractmethod


class CoreBase(ABC):

    @abstractmethod
    def get_optimal_saling_angle(self) -> float:
        pass

    @abstractmethod
    def get_optimal_rudder_angle(self) -> float:
        pass

    @abstractmethod
    def set_module_data(self, arbitration_id: str, data: float):
        pass
