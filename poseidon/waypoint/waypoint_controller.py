import math
from poseidon.waypoint.waypoint import Waypoint


class WaypointController:
    def __init__(self, waypoints: list):
        self._waypoints = waypoints
        self._index = 0
        self._current_waypoint = self._waypoints[0]

    @property
    def current_waypoint(self) -> Waypoint:
        return self._current_waypoint

    def next_waypoint(self) -> None:
        if (self._index + 1) < len(self._waypoints):
            self._index += 1
        else:
            self._index = 0
        self._current_waypoint = self._waypoints[self._index]

    # TODO: Check if better implementation is possible
    def angle_to_current_waypoint(self, sailboat_coordinates: list) -> float:
        delta_x = self.current_waypoint.coordinate_x - sailboat_coordinates[0]
        delta_y = self.current_waypoint.coordinate_y - sailboat_coordinates[1]
        rad = math.atan2(delta_y, delta_x)
        deg = rad * (180 / math.pi)
        return deg % 360

    def distance_to_waypoint(self, sailboat_coordinates: list) -> float:
        return math.sqrt(
            math.pow(self.current_waypoint.coordinate_x - sailboat_coordinates[0], 2) +
            math.pow(self.current_waypoint.coordinate_y - sailboat_coordinates[1], 2))
