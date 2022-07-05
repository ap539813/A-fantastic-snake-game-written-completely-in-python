import pygame
import random

from important_variables import screen_width, screen_height

def start_game():
    pygame.mixer.music.load('media.io_background.wav')
    pygame.mixer.music.play(20)
    exit_game = False
    game_over = False
    snake_x = screen_height//9
    snake_y = screen_width//9
    snake_width = screen_width//45
    FPS = 60
    snake_mv = 'r'
    food_pos = (random.randint(1, screen_height-snake_width), random.randint(70, screen_width-snake_width))
    head = [[snake_x, snake_y]]
    snake_len = 1
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Snake Chan", 29)
    font2 = pygame.font.SysFont("Snake Chan", 45)
    return exit_game, game_over, snake_x, snake_y, snake_width, FPS, snake_mv, food_pos, head, snake_len, clock, font, font2
