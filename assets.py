import pygame
from important_variables import apple_width, screen_width, screen_height
from paths import apple_path, game_over_image_path, welcome_page_image_path, snake_head as snake_head_path

appleImg = pygame.image.load(apple_path)
appleImg = pygame. transform.scale(appleImg, (apple_width, apple_width))
overImg = pygame.image.load(game_over_image_path)
welcm = pygame.image.load(welcome_page_image_path)
welcm = pygame.transform.scale(welcm, (screen_width, screen_height))

snake_head = pygame.image.load(snake_head_path)

