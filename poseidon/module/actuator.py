from poseidon.module.readable_module import ReadableModule
from poseidon.module.writeable_module import WriteableModule


class Actuator(ReadableModule, WriteableModule):
    def __init__(self, arbitration_id: str):
        super().__init__(arbitration_id)
