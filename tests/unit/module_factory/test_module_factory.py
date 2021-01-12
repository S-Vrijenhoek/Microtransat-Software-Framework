import unittest
from poseidon.module.module_factory import load_settings_modules, ModuleFactory
from poseidon.module.static_module import StaticModule
from poseidon.exception.settings_exception import SettingsException
from poseidon.exception.module_exception import ModuleException


class TestModuleFactoryMethods(unittest.TestCase):

    def test_load_settings_modules_correctly_loads_modules(self):
        expected_result = [
            {'id': '1', 'type': 'static_module'},
            {'id': '2', 'type': 'static_module'}
        ]

        result = load_settings_modules('tests/unit/module_factory/test_settings.yaml')
        self.assertEqual(result, expected_result)

    def test_load_settings_modules_raises_exception_on_missing_module(self):
        self.assertRaises(SettingsException,
                          load_settings_modules,
                          'tests/unit/module_factory/test_settings_without_modules.yaml')

    def test_create_modules_correctly_creates_modules(self):
        expected_result = [
            StaticModule('1'),
            StaticModule('2')
        ]

        result = ModuleFactory.create_modules('tests/unit/module_factory/test_settings.yaml')
        self.assertListEqual(result, expected_result)

    def test_create_modules_raises_exception_on_missing_module(self):
        self.assertRaises(ModuleException,
                          ModuleFactory.create_modules,
                          'tests/unit/module_factory/test_settings_with_missing_module.yaml')

    def test_create_modules_raises_exception_on_duplicate_module(self):
        self.assertRaises(ModuleException,
                          ModuleFactory.create_modules,
                          'tests/unit/module_factory/test_settings_with_duplicate_module.yaml')


if __name__ == '__main__':
    unittest.main()
