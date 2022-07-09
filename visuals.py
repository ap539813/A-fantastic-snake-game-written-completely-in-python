import pygame
from paths import game_background
from important_variables import eye_color

def plot_snake(gameWindow, head, snake_width, color, snake_len, snake_mv):
    pygame.draw.circle(gameWindow, color, [head[-1][0] + snake_width//2, head[-1][1] + snake_width//2], snake_width//2 + 1)
    if snake_len//3 < snake_width//2:
        for i in range(0, len(head)//3):
            pygame.draw.circle(gameWindow, color, [head[i][0] + snake_width//2, head[i][1] + snake_width//2], snake_width//2 + i - snake_len//3)
        for i in head[len(head)//3:-1]:
            pygame.draw.circle(gameWindow, color, [i[0] + snake_width//2, i[1] + snake_width//2], snake_width//2)
    else:
        for i in range(0, snake_width//2):
            pygame.draw.circle(gameWindow, color, [head[i][0] + snake_width//2, head[i][1] + snake_width//2], snake_width//2 - snake_width//2 + i)
        for i in head[snake_width//2:-1]:
            pygame.draw.circle(gameWindow, color, [i[0] + snake_width//2, i[1] + snake_width//2], snake_width//2)
    if snake_mv == 'u' or snake_mv == 'd':
        pygame.draw.circle(gameWindow, eye_color, [head[-1][0] + snake_width//2 + 3, head[-1][1] + snake_width//2], 3)
        pygame.draw.circle(gameWindow, eye_color, [head[-1][0] + snake_width//2 - 3, head[-1][1] + snake_width//2], 3)
    else:
        pygame.draw.circle(gameWindow, eye_color, [head[-1][0] + snake_width//2, head[-1][1] + snake_width//2 - 3], 3)
        pygame.draw.circle(gameWindow, eye_color, [head[-1][0] + snake_width//2, head[-1][1] + snake_width//2 + 3], 3)


def put_text(text, color, x, y, font, gameWindow):
    text_screen = font.render(text, True, color)
    gameWindow.blit(text_screen, [x, y])


def draw_background(gameWindow):
    # bg = pygame.image.load(game_background)
    # gameWindow.blit(bg, (0, 60))
    gameWindow.fill((255, 255, 255))