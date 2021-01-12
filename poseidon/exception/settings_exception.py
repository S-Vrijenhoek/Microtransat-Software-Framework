import logging


class SettingsException(Exception):
    def __init__(self, message):
        logging.error(message)

    @staticmethod
    def for_missing_modules():
        return SettingsException("The settings file is missing its modules.")

    @staticmethod
    def for_missing_waypoints():
        return SettingsException("The settings file is missing its waypoints.")
