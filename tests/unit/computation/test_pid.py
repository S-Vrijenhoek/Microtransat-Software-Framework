import unittest
from poseidon.computation.pid import PID


class TestPIDMethods(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pid = PID()
        self.pid.kp = 0.5
        self.pid.ki = 0.2
        self.pid.kd = 0.0005

    def test(self):
        self.pid.control(5, 5, 2)


if __name__ == '__main__':
    unittest.main()
