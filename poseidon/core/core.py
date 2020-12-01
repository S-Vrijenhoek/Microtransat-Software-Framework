import logging
from poseidon.core.core_base import CoreBase
from poseidon.module_factory.module_factory import ModuleFactory
from poseidon.exception.module_exception import ModuleException


class Core(CoreBase):

    def __init__(self, settings_location='poseidon/settings.yaml'):
        # logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',
        #                     filename='poseidon/debug.log',
        #                     level=logging.DEBUG)
        logging.disable()
        logging.info('Booting up the system ...')
        self._modules = ModuleFactory.create_modules(settings_location)
        logging.info('Finished booting up the system.')

    def get_course_instructions(self) -> list:
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
