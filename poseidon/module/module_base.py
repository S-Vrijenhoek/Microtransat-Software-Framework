class ModuleBase:

    def __init__(self, arbitration_id: str):
        self._arbitration_id = arbitration_id

    @property
    def arbitration_id(self) -> str:
        return self._arbitration_id

    def __eq__(self, other) -> bool:
        if not isinstance(other, ModuleBase):
            return False
        return self.arbitration_id == other.arbitration_id
