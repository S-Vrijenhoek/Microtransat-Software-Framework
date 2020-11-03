from abc import ABC, abstractmethod


class ModuleBase(ABC):

    @property
    @abstractmethod
    def arbitration_id(self):
        pass
