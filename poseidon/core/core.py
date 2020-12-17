import logging
from poseidon.core.core_base import CoreBase
from poseidon.module_factory.module_factory import ModuleFactory
from poseidon.computation.computation import Computation
from poseidon.module.module import Module
from poseidon.exception.module_exception import ModuleException


class Core(CoreBase):

    def __init__(self, settings_location='poseidon/settings.yaml'):
        # logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',
        #                     filename='poseidon/debug.log',
        #                     level=logging.DEBUG)
        logging.disable()
        logging.info('Booting up the system ...')
        self._modules = ModuleFactory.create_modules(settings_location)
        self._computation = Computation()
        logging.info('Finished booting up the system.')

    def get_optimal_saling_angle(self) -> float:
        return self._computation.compute_optimal_saling_angle(
            self._get_module('sailboat_rotation').data[0],
            self._get_module('wind_direction').data[0]
        )

    def set_module_data(self, arbitration_id: str, data: list) -> None:
        target_module_index = self._find_module_index(arbitration_id)
        self._modules[target_module_index].data = data

    def _get_module(self, arbitration_id: str) -> Module:
        target_module_index = self._find_module_index(arbitration_id)
        return self._modules[target_module_index]

    def _find_module_index(self, arbitration_id: str) -> int:
        i = 0

        for module in self._modules:
            if module.arbitration_id == arbitration_id:
                return i
            i += 1

        raise ModuleException.for_module_not_found(arbitration_id)
