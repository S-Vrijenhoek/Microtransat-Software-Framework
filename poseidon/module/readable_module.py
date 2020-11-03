from poseidon.module.module import Module


class ReadableModule(Module):

    def __init__(self, arbitration_id: str):
        super().__init__(arbitration_id)
        self._data = []

    @property
    def data(self) -> list:
        return self._data

    @data.setter
    def data(self, value: list):
        self._data = value
