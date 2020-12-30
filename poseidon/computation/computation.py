from poseidon.computation.computation_base import ComputationBase
from poseidon.computation.pid import PID
from poseidon.helper import Helper


class Computation(ComputationBase):

    def __init__(self):
        self._pid = PID()
        self._pid.kp = 0.5
        self._pid.ki = 0.2
        self._pid.ld = 0.0005

    def compute_optimal_saling_angle(self, sailboat_rotation: float, wind_direction: float) -> float:
        distance = Helper.distance_between_angles((sailboat_rotation + 180) % 360, wind_direction)

        if distance > 180:
            distance = (360 - distance) % 360

        # If wind blows from starboard
        if Helper.is_between_angles((sailboat_rotation - 180) % 360,
                                    sailboat_rotation,
                                    wind_direction):
            distance = -distance

        return distance / 2

    def compute_optimal_rudder_angle(self, current_heading) -> float:
        self._pid.control(current_heading, 100, 2)

        return 0.33
