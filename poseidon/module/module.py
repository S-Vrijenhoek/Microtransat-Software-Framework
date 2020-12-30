from poseidon.module.module_base import ModuleBase


class Module(ModuleBase):

    def __init__(self, arbitration_id: str):
        self._arbitration_id = arbitration_id
        self._data = None

    @property
    def arbitration_id(self) -> str:
        return self._arbitration_id

    def __eq__(self, other) -> bool:
        if not isinstance(other, Module):
            return False
        return self.arbitration_id == other.arbitration_id

    @property
    def data(self) -> float:
        return self._data

    @data.setter
    def data(self, value: list):
        self._data = value
