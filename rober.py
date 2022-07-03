import pygame
import gpiozero

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

# motor 모터 포트 번호 입력좀;;;
# motor_f1 = gpiozero.Motor(0, 0)
# motor_f2 = gpiozero.Motor(0, 0)
# motor_b1 = gpiozero.Motor(0, 0)
# motor_b2 = gpiozero.Motor(0, 0)

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
    # if up:
    #     motor_f1.forward(FORWARD_SPEED)
    #     motor_f2.forward(FORWARD_SPEED)
    #     motor_b1.forward(FORWARD_SPEED)
    #     motor_b2.forward(FORWARD_SPEED)
    # if down:
    #     motor_f1.backward(BACKWARD_SPEED)
    #     motor_f2.backward(BACKWARD_SPEED)
    #     motor_b1.backward(BACKWARD_SPEED)
    #     motor_b2.backward(BACKWARD_SPEED)
    # if left:
    #     motor_f1.backward(TURN_SPEED)
    #     motor_f2.backward(TURN_SPEED)
    #     motor_b1.forward(TURN_SPEED)
    #     motor_b2.forward(TURN_SPEED)
    # if right:
    #     motor_f1.forward(TURN_SPEED)
    #     motor_f2.forward(TURN_SPEED)
    #     motor_b1.backward(TURN_SPEED)
    #     motor_b2.backward(TURN_SPEED)

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

        # keyboard event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                up = True
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                down = True
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                left = True
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up = False
            if event.key == pygame.K_DOWN:
                down = False
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_RIGHT:
                right = False

    pygame.display.update()

pygame.quit()
