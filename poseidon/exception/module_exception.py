class ModuleException(Exception):
    def __init__(self, message):
        print(message)

    @staticmethod
    def for_missing_module(module_name):
        return ModuleException("The module `%s` does not exist." % module_name)
