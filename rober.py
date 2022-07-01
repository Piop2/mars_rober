import pygame
import gpiozero

# init pygame
pygame.init()
pygame.joystick.init()

# video system
display = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

# 모터 포트 번호 입력좀;;;
# motor_f1 = gpiozero.Motor(0, 0)
# motor_f2 = gpiozero.Motor(0, 0)
# motor_b1 = gpiozero.Motor(0, 0)
# motor_b2 = gpiozero.Motor(0, 0)

# controller button
controller = None
up = False
down = False
left = False
right = False

running = True
while running:
    clock.tick(60)

    try:
        # set controller
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
            pass

    pygame.display.update()

pygame.quit()
