"""
ROVER APP
"""
from client_socket.client import ClientSocket
from gpio.dc_motor import DCMotor


class Rover:
    def __init__(self):
        self.client = ClientSocket(self)
        self.motor_l = DCMotor((17, 27), (5, 6))
        self.motor_r = DCMotor((23, 24), (15, 16))

    def update(self):
        self.motor_l.go()
        self.motor_r.go()

    def run(self):
        self.client.run()
        while True:
            self.update()


if __name__ == '__main__':
    Rover().run()
