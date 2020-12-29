from poseidon.computation.computation_base import ComputationBase
from poseidon.helper import Helper


class Computation(ComputationBase):

    def compute_optimal_saling_angle(self,
                                     sailboat_rotation: float,
                                     wind_direction: float) -> float:
        distance = Helper.distance_between_angles((sailboat_rotation + 180) % 360, wind_direction)

        if distance > 180:
            distance = (360 - distance) % 360

        # If wind blows from starboard
        if Helper.is_between_angles((sailboat_rotation - 180) % 360,
                                    sailboat_rotation,
                                    wind_direction):
            distance = -distance

        return distance / 2
