import time
from poseidon.computation.computation_base import ComputationBase
from poseidon.computation.pid import PID
from poseidon.waypoint.waypoint_controller import WaypointController
from poseidon.helper import Helper


class Computation(ComputationBase):

    def __init__(self, waypoints: list):
        self._pid = PID()
        self._waypoint_controller = WaypointController(waypoints)
        self._delta_time = time.time()
        self._start_time = time.time()
        self._end_time = 0

    @property
    def delta_time(self):
        self._end_time = time.time()
        self._delta_time += self._end_time - self._start_time
        self._start_time = time.time()

        return self._delta_time

    def compute_optimal_sailing_angle(self, sailboat_rotation: float, wind_direction: float) -> float:
        # If wind is coming straight from behind
        if Helper.is_between_angles((sailboat_rotation + 180) % 360,
                                    (wind_direction - 45) % 360,
                                    (wind_direction + 45) % 360):
            return Helper.distance_between_angles((sailboat_rotation + 90) % 360, wind_direction)
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
                                     rudder_rotation: float,
                                     wind_direction: float) -> float:
        if self._waypoint_controller.distance_to_waypoint(sailboat_position) < 1:
            self._waypoint_controller.next_waypoint()

        angle_to_waypoint = self._waypoint_controller.angle_to_current_waypoint(sailboat_position)

        if Helper.is_between_angles(wind_direction,
                                    (angle_to_waypoint - 45) % 360,
                                    (angle_to_waypoint + 45) % 360):
            angle_to_waypoint = (angle_to_waypoint + 90) % 360

        return rudder_rotation - self._pid.control(angle_to_waypoint, sailboat_rotation, self.delta_time)
