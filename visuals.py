import pygame
from paths import game_background, score_board
from important_variables import eye_color
from assets import snake_head

def plot_snake(gameWindow, head, snake_width, color, snake_len, snake_mv):
    # pygame.draw.circle(gameWindow, color, [head[-1][0] + snake_width//2, head[-1][1] + snake_width//2], snake_width//2 + 1)

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
    if snake_mv == 'd':
        gameWindow.blit(snake_head, (head[-1][0] - (30 - snake_width)//2, head[-1][1]))
    elif snake_mv == 'u':
        snake_head_up = pygame.transform.flip(snake_head, False, True)
        gameWindow.blit(snake_head_up, (head[-1][0] - (30 - snake_width)//2, head[-1][1] - (30 - snake_width)))
    elif snake_mv == 'l':
        snake_head_left = pygame.transform.rotate(snake_head, -90)
        gameWindow.blit(snake_head_left, (head[-1][0] - (30 - snake_width), head[-1][1] - (30 - snake_width)//2))
    else:
        snake_head_right = pygame.transform.rotate(snake_head, 90)
        gameWindow.blit(snake_head_right, (head[-1][0], head[-1][1] - (30 - snake_width)//2))
    # if snake_mv == 'd':
    #     gameWindow.blit(snake_head, [head[-1][0] + snake_width//2, head[-1][1] + snake_width//2])
    # elif snake_mv == 'd':
    #     snake_head = pygame.transform.flip(snake_head, True, False)
    #     gameWindow.blit(snake_head, [head[-1][0] + snake_width//2, head[-1][1] + snake_width//2])
    # else:
    #     pygame.draw.circle(gameWindow, eye_color, [head[-1][0] + snake_width//2, head[-1][1] + snake_width//2 - 3], 3)
    #     pygame.draw.circle(gameWindow, eye_color, [head[-1][0] + snake_width//2, head[-1][1] + snake_width//2 + 3], 3)


def put_text(text, color, x, y, font, gameWindow):
    text_screen = font.render(text, True, color)
    gameWindow.blit(text_screen, [x, y])


def draw_background(gameWindow):
    sg = pygame.image.load(score_board)
    gameWindow.blit(sg, (0, 0))
    bg = pygame.image.load(game_background)
    gameWindow.blit(bg, (0, 60))

def game_over_page(gameWindow):
    sg = pygame.image.load(score_board)
    gameWindow.blit(sg, (0, 0))