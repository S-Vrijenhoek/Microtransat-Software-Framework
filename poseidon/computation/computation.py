import time
from poseidon.computation.computation_base import ComputationBase
from poseidon.computation.pid import PID
from poseidon.helper import Helper


class Computation(ComputationBase):

    def __init__(self):
        self._pid = PID()
        self._delta_time = 0
        self._start_time = time.time()
        self._end_time = 0

    @property
    def delta_time(self):
        self._end_time = time.time()
        self._delta_time += self._end_time - self._start_time
        self._start_time = time.time()

        return self._delta_time

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

    def compute_optimal_rudder_angle(self, sailboat_rotation, rudder_rotation) -> float:
        return rudder_rotation - self._pid.control(270, sailboat_rotation, self.delta_time)
