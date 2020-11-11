import logging


class ModuleException(Exception):
    def __init__(self, message):
        logging.error(message)

    @staticmethod
    def for_missing_module(module_name: str):
        return ModuleException("The module `%s` does not exist in the settings file." % module_name)

    @staticmethod
    def for_module_not_found(arbitration_id: str):
        return ModuleException("The module with an id of `%s` could not be found." % arbitration_id)

    @staticmethod
    def for_duplicate_module(arbitration_id: str):
        return ModuleException("The module with an id of `%s` already exists." % arbitration_id)
