# Snake Game
# Code created by sabrinaamorimdecastro

#Library
import pygame
from pygame.locals import *
from sys import exit
from pygame import mixer
from random import randint

# Start the game
pygame.init()


# Screen size
width = 640
height = 480

# Snake home position 
x_snake = int(width/2) 
y_snake = int(height/2)

speed = 10
x_control = speed
y_control = 0

# Limits to appear the apple
x_apple = randint(40, 600)
y_apple = randint(50, 430)

points = 0

font = pygame.font.SysFont('arial', 40, bold=True, italic=True)

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Snake x Apple')

# Frame for second
watch = pygame.time.Clock()

list_snake = []

initial_length = 5

dead = False


# Increase snake
def increase_snake(list_snake):

    for XeY in list_snake:
        pygame.draw.rect(screen, (0,199,0), (XeY[0], XeY[1], 20, 20))

# Restart game
def restart_game():

    global points, initial_length, x_snake, y_snake, list_snake, list_head, x_apple, y_apple, dead

    points = 0

    initial_length = 5

    x_snake = int(width/2) 
    y_snake = int(height/2)

    list_snake = []
    list_head = []

    x_apple = randint(40, 600)
    y_apple = randint(50, 430)

    dead = False


while True:

    watch.tick(30)

    screen.fill((255,255,255))

    message = f'Score: {points}'

    text_format = font.render(message, True, (255,140,0))

    # Capture pressed keys
    for event in pygame.event.get():

        # Check if it was an event to finish 
        if event.type == QUIT:
            pygame.quit()
            exit()

        # Keys to move snake
        if event.type == KEYDOWN:

            if event.key == K_a:
                if x_control == speed:
                    pass
                else:
                    x_control = -speed
                    y_control = 0

            if event.key == K_d:
                if x_control == -speed:
                    pass
                else:
                    x_control = speed
                    y_control = 0

            if event.key == K_w:
                if y_control == speed:
                    pass
                else:
                    y_control = -speed
                    x_control = 0

            if event.key == K_s:
                if y_control == -speed:
                    pass
                else:
                    y_control = speed
                    x_control = 0


    x_snake = x_snake + x_control
    y_snake = y_snake + y_control

    # Size and color Snake  
    snake = pygame.draw.rect(screen, (0,255,0), (x_snake,y_snake,20,20))
    
    # Size and color apple
    apple = pygame.draw.rect(screen, (255,0,0), (x_apple,y_apple,20,20))

    # Snake eat apple
    if snake.colliderect(apple):
        x_apple = randint(40, 600)
        y_apple = randint(50, 430)
        points += 1
        initial_length = initial_length + 1

    # Increase snake
    list_head = []
    list_head.append(x_snake)
    list_head.append(y_snake)
    list_snake.append(list_head)


    # Game over
    if list_snake.count(list_head) > 1:

        font2 = pygame.font.SysFont('arial', 30, True, True)

        message = 'GAME OVER! Press R to restart'

        text_format = font2.render(message, True, (255,0,0))

        text_ret = text_format.get_rect()

        dead = True


        # Exit game or restart
        while dead:

            screen.fill((255,255,255))

            for event in pygame.event.get():

                if event.type == QUIT:
                    pygame.quit()
                    exit()

                if event.type == KEYDOWN:

                    if event.key == K_r:
                        restart_game()


            text_ret.center = (width//2, height//2) 

            screen.blit(text_format, text_ret)

            pygame.display.update()


    if x_snake > width:
        x_snake = 0

    if x_snake < 0:
        x_snake = width

    if y_snake < 0:
        y_snake = height

    if y_snake > height:
        y_snake = 0

    # Start snake with initial_lenght
    if len(list_snake) > initial_length:
        del list_snake[0]

    increase_snake(list_snake)

    screen.blit(text_format, (450,40))

    pygame.display.update()