import unittest
from poseidon.module_factory.module_factory import load_settings_modules
from poseidon.exception.settings_exception import SettingsException


class TestModuleFactoryMethods(unittest.TestCase):

    def test_load_settings_modules_correctly_loads_modules(self):
        expected_result = [
            {'id': '1', 'type': 'foo'},
            {'id': '2', 'type': 'bar'},
            {'id': '3', 'type': 'baz'}
        ]

        self.assertEqual(load_settings_modules('tests/unit/test_settings.yaml'),
                         expected_result)

    def test_load_settings_modules_throws_exception_on_missing_module(self):
        self.assertRaises(SettingsException,
                          load_settings_modules,
                          'tests/unit/test_settings_without_modules.yaml')


if __name__ == '__main__':
    unittest.main()
