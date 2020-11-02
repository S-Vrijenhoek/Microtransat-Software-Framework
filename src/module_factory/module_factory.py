import ruamel.yaml
from .module_factory_base import ModuleFactoryBase


def load_settings_modules() -> list:
    with open("./settings.yaml") as fp:
        data = ruamel.yaml.safe_load(fp)
        return data["modules"]


class ModuleFactory(ModuleFactoryBase):

    def create_modules(self) -> list:

        created_modules = []

        for module in load_settings_modules():
            module_type = module["type"]

            # TODO: class initialization
            if module_type == "sensor":
                created_modules.append("s")
            elif module_type == "actuator":
                created_modules.append("a")
            else:
                # TODO: error handling
                print("error")

        return created_modules
