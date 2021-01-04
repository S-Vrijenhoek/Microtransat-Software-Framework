import unittest
from poseidon.computation.pid import PID


class TestPIDMethods(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pid = PID()

    def test(self):
        pass


if __name__ == '__main__':
    unittest.main()
