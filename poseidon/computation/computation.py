import time
import math
from poseidon.computation.computation_base import ComputationBase
from poseidon.computation.pid import PID
from poseidon.helper import Helper


# WIP
def angle_to_coordinate(coordinate_a: list, coordinate_b: list) -> float:
    delta_x = coordinate_b[0] - coordinate_a[0]
    delta_y = coordinate_b[1] - coordinate_a[1]
    rad = math.atan2(delta_y, delta_x)
    deg = rad * (180 / math.pi)
    return deg % 360


def distance_between_coordinates(coordinate_a: list, coordinate_b: list) -> float:
    return math.sqrt(math.pow(coordinate_b[0] - coordinate_a[0], 2) + math.pow(coordinate_b[1] - coordinate_a[1], 2))


class Computation(ComputationBase):

    def __init__(self):
        self._pid = PID()
        self._delta_time = time.time()
        self._start_time = time.time()
        self._end_time = 0
        self._waypoints = [
            [10, 10],
            [-10, 5]
        ]
        self._current_waypoint = self._waypoints[0]

    @property
    def delta_time(self):
        self._end_time = time.time()
        self._delta_time += self._end_time - self._start_time
        self._start_time = time.time()

        return self._delta_time

    def compute_optimal_saling_angle(self, sailboat_rotation: float, wind_direction: float) -> float:
        # If wind is coming straight from behind
        if Helper.is_between_angles((sailboat_rotation + 180 % 360), wind_direction - 45, wind_direction + 45):
            distance = Helper.distance_between_angles((sailboat_rotation + 90) % 360, wind_direction)

            if Helper.is_between_angles(wind_direction, (sailboat_rotation - 180) % 360, sailboat_rotation):
                distance = -distance

            return distance

        else:
            distance = Helper.distance_between_angles((sailboat_rotation + 180) % 360, wind_direction)

            if distance > 180:
                distance = (360 - distance) % 360

            # If wind blows from starboard
            if Helper.is_between_angles((sailboat_rotation - 180) % 360,
                                        sailboat_rotation,
                                        wind_direction):
                distance = -distance

            return distance / 2

    def compute_optimal_rudder_angle(self, sailboat_position: list,
                                     sailboat_rotation: float,
                                     rudder_rotation: float) -> float:

        if distance_between_coordinates(sailboat_position, self._current_waypoint) < 1:
            self._current_waypoint = self._waypoints[1]

        angle_to_waypoint = angle_to_coordinate(sailboat_position, self._current_waypoint)

        return rudder_rotation - self._pid.control(angle_to_waypoint, sailboat_rotation, self.delta_time)
