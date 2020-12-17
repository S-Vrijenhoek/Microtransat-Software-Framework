from poseidon.computation.computation_base import ComputationBase


def is_between_angles(n, alpha, beta) -> float:
    if alpha < beta:
        return alpha <= n <= beta
    return alpha <= n or n <= beta


def distance_between_angles(alpha, beta) -> float:
    phi = abs(beta - alpha) % 360
    distance = (180 - phi) % 360 if phi > 90 else phi
    return distance


class Computation(ComputationBase):

    def compute_optimal_saling_angle(self,
                                     sailboat_rotation: float,
                                     wind_direction: float) -> float:
        distance = distance_between_angles((sailboat_rotation + 180) % 360, wind_direction)

        if distance > 180:
            distance = (360 - distance) % 360

        # If wind blows from starboard
        if is_between_angles((sailboat_rotation - 180) % 360,
                             sailboat_rotation,
                             wind_direction):
            distance = -distance

        return distance / 2
