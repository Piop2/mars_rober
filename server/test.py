import gpiozero

motor = gpiozero.Robot(left=(16, 17), right=(23, 24))

motor.forward(10)

