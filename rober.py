import pygame
from gpiozero import Robot

from utils.clip import clip

# init pygame
pygame.init()
pygame.joystick.init()

# video system
display = pygame.display.set_mode((300, 300))
pygame.display.set_caption('controller debug')
clock = pygame.time.Clock()


# button images
def load_button(path):
    images = pygame.image.load(path)
    b_down_img = clip(images, 0, 0, 50, 50)
    b_up_img = clip(images, 55, 0, 50, 50)
    return b_down_img, b_up_img


def blit_button(surface, is_pushed, button_imgs, pos):
    if is_pushed:
        surface.blit(button_imgs[1], pos)
    else:
        surface.blit(button_imgs[0], pos)
    return


button_up = load_button('images/button_up.png')
button_down = load_button('images/button_down.png')
button_left = load_button('images/button_left.png')
button_right = load_button('images/button_right.png')

# plz check dc motor driver port num
dc_motor1 = Robot(left=(0, 0), right=(0, 0))
dc_motor2 = Robot(left=(0, 0), right=(0, 0))

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

    # render
    display.fill((100, 100, 100))
    blit_button(display, up, button_up, (125, 150))
    blit_button(display, down, button_down, (125, 250))
    blit_button(display, left, button_left, (75, 200))
    blit_button(display, right, button_right, (175, 200))

    # move rober
    if up:
        dc_motor1.forward(FORWARD_SPEED)
        dc_motor2.forward(FORWARD_SPEED)
    if down:
        dc_motor1.backward(BACKWARD_SPEED)
        dc_motor2.backward(BACKWARD_SPEED)
    if left:
        dc_motor1.backward(TURN_SPEED)
        dc_motor2.forward(TURN_SPEED)
    if right:
        dc_motor1.forward(TURN_SPEED)
        dc_motor2.backward(TURN_SPEED)

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
            if event.type == pygame.JOYHATMOTION:
                print(event)
                if event.value == (0, 1):
                    up = True
                if event.value == (0, -1):
                    down = True
                if event.value == (1, 0):
                    right = True
                if event.value == (-1, 0):
                    left = True
                if event.value == (0, 0):
                    up = False
                    down = False
                    right = False
                    left = False

        # keyboard event
        if event.type == pygame.KEYDOWN:
            print(event)
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                up = True
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                down = True
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                left = True
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                right = True

        if event.type == pygame.KEYUP:
            print(event)
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                up = False
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                down = False
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                left = False
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                right = False

    pygame.display.update()

pygame.quit()
