import gpiozero

motor = gpiozero.Robot(left=(16, 17), right=(23, 24))

while True:
    motor.forward(1)


