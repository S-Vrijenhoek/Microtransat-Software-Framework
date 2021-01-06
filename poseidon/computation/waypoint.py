class Waypoint:
    def __init__(self, coordinate_x, coordinate_y):
        self._coordinate_x = coordinate_x
        self._coordinate_y = coordinate_y

    @property
    def coordinate_x(self):
        return self._coordinate_x

    @property
    def coordinate_y(self):
        return self._coordinate_y
