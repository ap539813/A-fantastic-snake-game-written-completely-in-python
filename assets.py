import pygame
from important_variables import apple_width, screen_width, screen_height

carImg = pygame.image.load('asset/apple.png')
carImg = pygame. transform.scale(carImg, (apple_width, apple_width))
overImg = pygame.image.load('asset/tenor.gif')
welcm = pygame.image.load('asset/welcome_page.png')
welcm = pygame. transform.scale(welcm, (screen_width, screen_height))


