import pygame
import gpiozero

# init pygame
pygame.init()
pygame.joystick.init()

# video system
display = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

# motor 모터 포트 번호 입력좀;;;
motor_f1 = gpiozero.Motor(0, 0)
motor_f2 = gpiozero.Motor(0, 0)
motor_b1 = gpiozero.Motor(0, 0)
motor_b2 = gpiozero.Motor(0, 0)

# motor speed
FORWARD_SPEED = 1
BACKWARD_SPEED = 1
TURN_SPEED = 1

# controller button
controller = None
up = False
down = False
left = False
right = False

running = True
while running:
    clock.tick(60)

    # move rober
    if up:
        motor_f1.forward(FORWARD_SPEED)
        motor_f2.forward(FORWARD_SPEED)
        motor_b1.forward(FORWARD_SPEED)
        motor_b2.forward(FORWARD_SPEED)
    if down:
        motor_f1.backward(BACKWARD_SPEED)
        motor_f2.backward(BACKWARD_SPEED)
        motor_b1.backward(BACKWARD_SPEED)
        motor_b2.backward(BACKWARD_SPEED)
    if left:
        motor_f1.backward(TURN_SPEED)
        motor_f2.backward(TURN_SPEED)
        motor_b1.forward(TURN_SPEED)
        motor_b2.forward(TURN_SPEED)
    if right:
        motor_f1.forward(TURN_SPEED)
        motor_f2.forward(TURN_SPEED)
        motor_b1.backward(TURN_SPEED)
        motor_b2.backward(TURN_SPEED)

    # set controller
    try:
        controller = pygame.joystick.Joystick(0)
    except RuntimeError:
        controller = None
        pass

    # event
    for event in pygame.event.get():
        # quit
        if event.type == pygame.QUIT:
            running = False

        # controller event
        if controller is not None:
            if pygame.event == pygame.CONTROLLERAXISMOTION:
                pass

    pygame.display.update()

pygame.quit()
