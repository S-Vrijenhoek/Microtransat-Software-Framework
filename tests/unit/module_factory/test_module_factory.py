import unittest
from poseidon.module_factory.module_factory import load_settings_modules, ModuleFactory
from poseidon.module.sensor import Sensor
from poseidon.module.actuator import Actuator
from poseidon.exception.settings_exception import SettingsException
from poseidon.exception.module_exception import ModuleException


class TestModuleFactoryMethods(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.module_factory = ModuleFactory()

    def test_load_settings_modules_correctly_loads_modules(self):
        expected_result = [
            {'id': '1', 'type': 'sensor'},
            {'id': '2', 'type': 'actuator'}
        ]

        result = load_settings_modules('tests/unit/module_factory/test_settings.yaml')
        self.assertEqual(result, expected_result)

    def test_load_settings_modules_raises_exception_on_missing_module(self):
        self.assertRaises(SettingsException,
                          load_settings_modules,
                          'tests/unit/module_factory/test_settings_without_modules.yaml')

    def test_create_modules_correctly_creates_modules(self):
        expected_result = [
            Sensor('1'),
            Actuator('2')
        ]

        result = self.module_factory.create_modules('tests/unit/module_factory/test_settings.yaml')
        self.assertListEqual(result, expected_result)

    def test_create_modules_raises_exception_on_missing_module(self):
        self.assertRaises(ModuleException,
                          self.module_factory.create_modules,
                          'tests/unit/module_factory/test_settings_with_missing_module.yaml')


if __name__ == '__main__':
    unittest.main()
