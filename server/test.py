import gpiozero

motor1 = gpiozero.Robot(left=(17, 27), right=(5, 6))
motor2 = gpiozero.Robot(left=(23, 24), right=(25, 16))

while True:
    motor1.forward(1)
    motor2.forward(1)


