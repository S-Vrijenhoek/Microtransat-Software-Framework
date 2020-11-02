class SettingsException(Exception):
    def __init__(self, message):
        print(message)

    @staticmethod
    def for_missing_modules():
        return SettingsException("The settings file is missing it's modules.")
