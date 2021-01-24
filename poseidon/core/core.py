import logging
from poseidon.core.core_base import CoreBase
from poseidon.waypoint.waypoint_factory import WaypointFactory
from poseidon.module.module_factory import ModuleFactory
from poseidon.computation.computation import Computation
from poseidon.module.static_module import StaticModule
from poseidon.exception.module_exception import ModuleException


class Core(CoreBase):

    def __init__(self, settings_location='poseidon/settings.yaml'):
        # TODO: Make use of logging
        # logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',
        #                     filename='poseidon/debug.log',
        #                     level=logging.DEBUG)
        logging.disable()
        logging.info('Booting up the system ...')
        self._modules = ModuleFactory.create_modules(settings_location)
        self._module_indices = dict()
        self._register_module_indices()
        self._computation = Computation(WaypointFactory.create_waypoints(settings_location))
        logging.info('Finished booting up the system.')

    def get_optimal_sailing_angle(self) -> float:
        return self._computation.compute_optimal_sailing_angle(
            self._get_module('sailboat_rotation').data,
            self._get_module('wind_direction').data
        )

    def get_optimal_rudder_angle(self) -> float:
        return self._computation.compute_optimal_rudder_angle(
            [self._get_module('sailboat_position_x').data, self._get_module('sailboat_position_y').data],
            self._get_module('sailboat_rotation').data,
            self._get_module('rudder_rotation').data,
            self._get_module('wind_direction').data
        )

    def set_module_data(self, arbitration_id: str, data: float) -> None:
        try:
            target_module_index = self._module_indices[arbitration_id]
            self._modules[target_module_index].data = data
        except KeyError:
            raise ModuleException.for_module_not_found(arbitration_id)

    # TODO: Make this work for every module type (don't always return a StaticModule)
    def _get_module(self, arbitration_id: str) -> StaticModule:
        try:
            target_module_index = self._module_indices[arbitration_id]
            return self._modules[target_module_index]
        except KeyError:
            raise ModuleException.for_module_not_found(arbitration_id)

    def _register_module_indices(self):
        i = 0
        for module in self._modules:
            self._module_indices[module.arbitration_id] = i
            i += 1
