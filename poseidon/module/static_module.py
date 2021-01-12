from poseidon.module.module import Module


class StaticModule(Module):

    def __init__(self, arbitration_id: str):
        super().__init__(arbitration_id)
        self._data = None

    @property
    def data(self) -> float:
        return self._data

    @data.setter
    def data(self, value: float):
        self._data = value
