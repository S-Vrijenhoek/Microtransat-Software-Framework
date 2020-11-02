import ruamel.yaml
from poseidon.module_factory.module_factory_base import ModuleFactoryBase
from poseidon.exception.settings_exception import SettingsException


def load_settings_modules(settings_location: str) -> list:
    with open(settings_location) as fp:
        data = ruamel.yaml.safe_load(fp)

        try:
            if data['modules']:
                return data['modules']
        except (KeyError, TypeError):
            raise SettingsException.for_missing_modules()


class ModuleFactory(ModuleFactoryBase):

    def create_modules(self) -> list:
        created_modules = []

        for module in load_settings_modules('./settings.yaml'):
            module_type = module['type']

            # TODO: class initialization
            if module_type == 'sensor':
                created_modules.append('s')
            elif module_type == 'actuator':
                created_modules.append('s')
            else:
                # TODO: error handling
                print('error')

        return created_modules
