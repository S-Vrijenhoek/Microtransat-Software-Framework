from poseidon.module.module import Module


class WriteableModule(Module):

    def __init__(self, arbitration_id: str):
        super().__init__(arbitration_id)
        self._instructions = []

    @property
    def instructions(self) -> list:
        return self._instructions

    @instructions.setter
    def instructions(self, value: list):
        self._instructions = value
