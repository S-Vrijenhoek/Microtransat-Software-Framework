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

    def create_modules(self, settings_location='poseidon/settings.yaml') -> list:
        created_modules = []

        for module in load_settings_modules(settings_location):
            module_id = module['id']
            module_type = module['type']

            if module_type == 'sensor':
                created_modules.append(Sensor(module_id))
            elif module_type == 'actuator':
                created_modules.append(Actuator(module_id))
            else:
                raise ModuleException.for_missing_module(module_type)

        return created_modules
