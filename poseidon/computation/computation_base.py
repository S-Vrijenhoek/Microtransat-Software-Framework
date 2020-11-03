from abc import ABC, abstractmethod


class ComputationBase(ABC):

    @abstractmethod
    def interpret_input_modules(self, modules: list):
        pass
