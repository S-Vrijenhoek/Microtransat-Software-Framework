from abc import ABC, abstractmethod


class ModuleFactoryBase(ABC):

    @abstractmethod
    def create_modules(self, settings_location: str) -> list:
        pass
