from poseidon.core.core_base import CoreBase
from poseidon.module_factory.module_factory import ModuleFactory
from poseidon.exception.module_exception import ModuleException


class Core(CoreBase):

    def __init__(self, settings_location='poseidon/settings.yaml'):
        self._modules = ModuleFactory.create_modules(settings_location)

    def get_instructions(self) -> list:
        pass

    def set_module_data(self, arbitration_id: str, data: list) -> None:
        target_module_index = self._find_module_index(arbitration_id)
        self._modules[target_module_index].data = data

    def _find_module_index(self, arbitration_id: str) -> int:
        i = 0

        for module in self._modules:
            if module.arbitration_id == arbitration_id:
                return i
            i += 1

        raise ModuleException.for_module_not_found(arbitration_id)
