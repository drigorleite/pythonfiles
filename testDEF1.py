import pygame
import time
import random

# Constants for colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (213, 50, 80)

# Constants for directions
LEFT = (-10, 0)
RIGHT = (10, 0)
UP = (0, -10)
DOWN = (0, 10)

# Constants for display dimensions
DIS_WIDTH = 800
DIS_HEIGHT = 600

# Initialize Pygame
pygame.init()

# Set up the display
dis = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
pygame.display.set_caption('Snake Game')

# Set up the clock
clock = pygame.time.Clock()

# Set up the font
font_style = pygame.font.SysFont(None, 50)


def your_score(score):
    value = font_style.render("Your Score: " + str(score), True, WHITE)
    dis.blit(value, [10, 10])


def our_snake(snake_block, snake_list):
    for segment in snake_list:
        pygame.draw.rect(dis, GREEN, [segment[0], segment[1], snake_block, snake_block])


def game_intro():
    intro = True
    while intro:
        dis.fill(BLACK)
        message("Welcome to Snake Game", WHITE, -50)
        message("Press C to play or Q to quit", WHITE, 50)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    intro = False


def message(msg, color, y_displace=0):
    text = font_style.render(msg, True, color)
    text_rect = text.get_rect()
    text_rect.center = (DIS_WIDTH / 2, DIS_HEIGHT / 2 + y_displace)
    dis.blit(text, text_rect)


def game_loop():
    game_over = False
    game_close = False

    x1, y1 = DIS_WIDTH / 2, DIS_HEIGHT / 2
    x1_change, y1_change = 0, 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, DIS_WIDTH - 10) / 10.0) * 10.0
    foody = round(random.randrange(0, DIS_HEIGHT - 10) / 10.0) * 10.0

    while not game_over:

        while game_close:
            dis.fill(BLACK)
            message("Game Over", RED, -50)
            your_score(length_of_snake - 1)
            message("Press C to play again or Q to quit", WHITE, 50)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change, y1_change = LEFT
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change, y1_change = RIGHT
                elif event.key == pygame.K_UP and y1_change == 0:
                    x1_change, y1_change = UP
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    x1_change, y1_change = DOWN

        if x1 >= DIS_WIDTH or x1 < 0 or y1 >= DIS_HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(BLACK)
        pygame.draw.rect(dis, YELLOW, [foodx, foody, 10, 10])
        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        our_snake(10, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, DIS_WIDTH - 10) / 10.0) * 10.0
            foody = round(random.randrange(0, DIS_HEIGHT - 10) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(15)

    pygame.quit()
    quit()


game_intro()
game_loop()
