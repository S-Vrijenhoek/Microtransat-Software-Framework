from poseidon.helper import Helper


def calculate_error(current_heading, desired_heading) -> int:
    phi = abs(current_heading - desired_heading) % 360
    distance = 360 - phi if phi > 180 else phi

    if Helper.is_between_angles(current_heading, (current_heading - 180) % 360, desired_heading):
        return distance
    else:
        return -distance


def clamp_error(error: float, clamp: float) -> float:
    if error < -clamp:
        return -clamp
    else:
        return clamp


class PID:
    def __init__(self):
        self.error_integral = 0
        self.kp = 0.5
        self.ki = 0.02
        self.kd = 0.0005

    def control(self, desired_heading, current_heading, dt):
        error = calculate_error(current_heading, desired_heading)
        clamped_error = clamp_error(error, 5)

        is_clamped = False
        if error != clamped_error:
            is_clamped = True

        output_p = self.calculate_proportional(error)
        output_i = self.calculate_intergrational(dt, error)
        output_d = self.calculate_differentional(current_heading, dt, clamped_error)
        output = output_p + output_i + output_d

        is_integrator = False
        if (error > 0 and output > 0) or (error < 0 and output < 0):
            is_integrator = True

        if is_clamped and is_integrator:
            self.error_integral = 0

        return 0.5 * output

    def calculate_proportional(self, error):
        return self.kp * error

    def calculate_intergrational(self, dt, error):
        self.error_integral += self.ki * error * dt

        return self.error_integral

    def calculate_differentional(self, current_input, dt, error):
        if error < 0:
            return -self.kd * ((current_input + error) / dt)
        else:
            return self.kd * ((current_input - error) / dt)
