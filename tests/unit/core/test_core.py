import unittest
from poseidon.core.core import Core
from poseidon.exception.module_exception import ModuleException


class TestCoreMethods(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.core = Core('tests/unit/core/test_settings.yaml')

    def test_set_module_data_raises_exception_on_missing_module(self):
        self.assertRaises(ModuleException,
                          self.core.set_module_data,
                          'baz',
                          ['bar', 'baz'])

    def test_get_optimal_saling_angle_correctly_returns_sailing_angle(self):
        self.core.set_module_data('sailboat_rotation', 180)
        self.core.set_module_data('wind_direction', 90)
        self.core.get_optimal_saling_angle()


if __name__ == '__main__':
    unittest.main()
