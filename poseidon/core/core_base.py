from abc import ABC, abstractmethod


class CoreBase(ABC):

    @abstractmethod
    def get_instructions(self) -> list:
        pass

    @abstractmethod
    def set_module_data(self, abstraction_id: str, data: list):
        pass
