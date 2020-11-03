from abc import ABC, abstractmethod


class ModuleFactoryBase(ABC):

    @staticmethod
    @abstractmethod
    def create_modules(settings_location: str) -> list:
        pass
