from poseidon.helper import Helper


# calculate the error and returns by how much are we off desired heading
# distance is in this case the amount of angles we are off compared to our desired heading
def calculate_error(current_heading, desired_heading):
    phi = abs(current_heading - desired_heading) % 360
    distance = 360 - phi if phi > 180 else phi

    if Helper.is_between_angles(current_heading, (current_heading - 180) % 360, desired_heading):
        return distance
    else:
        return -distance


def clamp_error(error: float, clamp: float):
    if error < -clamp:
        return -clamp

    if error > clamp:
        return clamp


class PID(object):
    def __init__(self):
        self._integral_error = None
        self._output_limit = None
        self._latest_input = None
        self._desired_heading = None
        self._current_heading = None

        self._dt = None
        self._kp = None
        self._ki = None
        self._kd = None

    @property
    def kp(self):
        return self._kp

    @property
    def ki(self):
        return self._ki

    @property
    def kd(self):
        return self._kd

    @kp.setter
    def kp(self, value):
        self._kp = value

    @ki.setter
    def ki(self, value):
        self._ki = value

    @kd.setter
    def kd(self, value):
        self._kd = value

    def control(self, current_heading: float, desired_heading: float, dt: float):
        error = calculate_error(current_heading, desired_heading)
        errorc = calculate_error(current_heading, desired_heading)
        error = clamp_error(error, 5)

        clamp = False
        if error != errorc:
            clamp = True

        output_p = self.calculate_proportional(error)
        output_i = self.calculate_integrational(error, dt)
        output_d = self.calculate_differential(error, self._dt, current_heading)
        output = output_p + output_i + output_d

        if (error > 0 and output > 0) or (error < 0 and output < 0):
            integrater_status = True
        else:
            integrater_status = False
        if clamp is True and integrater_status is True:
            self._integral_error = 0

        print(error)

    def calculate_proportional(self, error: float):
        return self._kp * error

    def calculate_integrational(self, error: float, dt: float):
        self._integral_error += self._ki * error * dt

        return self._integral_error

    def calculate_differential(self, error: float, dt: float, current_input: float):
        if error < 0:
            return -self._kd * ((current_input + error) / dt)
        else:
            return self._kd * ((current_input - error) / dt)
