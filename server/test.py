import gpiozero

motor = gpiozero.Robot(left=(17, 27), right=(5, 6))

while True:
    motor.forward(1)


