"""
ROVER APP
"""
import client_socket
import rasp_gpio


class Rover:
    def __init__(self):
        self.client = client_socket.client.ClientSocket(self)
        self.motor_l = rasp_gpio.dc_motor.DCMotor((17, 27), (5, 6))
        self.motor_r = rasp_gpio.dc_motor.DCMotor((23, 24), (15, 16))

    def update(self):
        self.motor_l.go()
        self.motor_r.go()

    def run(self):
        self.client.run()
        while True:
            self.update()


if __name__ == '__main__':
    Rover().run()
