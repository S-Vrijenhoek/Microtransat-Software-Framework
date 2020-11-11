import logging
import ruamel.yaml
from poseidon.module_factory.module_factory_base import ModuleFactoryBase
from poseidon.module.sensor import Sensor
from poseidon.module.actuator import Actuator
from poseidon.exception.settings_exception import SettingsException
from poseidon.exception.module_exception import ModuleException


def load_settings_modules(settings_location: str) -> list:
    with open(settings_location) as fp:
        data = ruamel.yaml.safe_load(fp)

        try:
            if data['modules']:
                return data['modules']
        except (KeyError, TypeError):
            raise SettingsException.for_missing_modules()


class ModuleFactory(ModuleFactoryBase):

    @staticmethod
    def create_modules(settings_location) -> list:
        created_modules = []
        used_ids = []

        logging.info('Loading all modules ...')
        for module in load_settings_modules(settings_location):
            module_id = module['id']
            module_type = module['type']

            if module_id in used_ids:
                raise ModuleException.for_duplicate_module(module_id)

            if module_type == 'sensor':
                created_modules.append(Sensor(module_id))
            elif module_type == 'actuator':
                created_modules.append(Actuator(module_id))
            else:
                raise ModuleException.for_missing_module(module_type)

            used_ids.append(module_id)
            logging.info('Detected %s with an id of "%s"', module_type, module_id)

        logging.info('Finished loading all modules.')
        return created_modules
