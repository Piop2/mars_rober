import gpiozero


class DCMotor:
    def __init__(self, pin1, pin2):
        self.motor = gpiozero.Robot(left=pin1, right=pin2)
        self.motor_speed = 0
        self.mode = "forward"

    @property
    def speed(self):
        return

    @speed.setter
    def speed(self, new_speed):
        self.motor_speed = new_speed
        if new_speed >= 0:
            self.mode = "forward"
        else:
            self.mode = "backward"

    def go(self):
        speed = abs(self.motor_speed)
        if self.mode == "forward":
            self.motor.forward(speed)
        else:
            self.motor.backward(speed)
