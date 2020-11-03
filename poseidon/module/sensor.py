from poseidon.module.readable_module import ReadableModule


class Sensor(ReadableModule):
    def __init__(self, arbitration_id: str):
        super().__init__(arbitration_id)
