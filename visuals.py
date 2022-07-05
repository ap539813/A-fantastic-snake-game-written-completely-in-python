import pygame

def plot_snake(gameWindow, head, snake_width, green, snake_len, snake_mv):
    pygame.draw.circle(gameWindow, green, [head[-1][0] + snake_width//2, head[-1][1] + snake_width//2], snake_width//2 + 1)
    if snake_len//3 < snake_width//2:
        for i in range(0, len(head)//3):
            pygame.draw.circle(gameWindow, green, [head[i][0] + snake_width//2, head[i][1] + snake_width//2], snake_width//2 + i - snake_len//3)
        for i in head[len(head)//3:-1]:
            pygame.draw.circle(gameWindow, green, [i[0] + snake_width//2, i[1] + snake_width//2], snake_width//2)
    else:
        for i in range(0, snake_width//2):
            pygame.draw.circle(gameWindow, green, [head[i][0] + snake_width//2, head[i][1] + snake_width//2], snake_width//2 - snake_width//2 + i)
        for i in head[snake_width//2:-1]:
            pygame.draw.circle(gameWindow, green, [i[0] + snake_width//2, i[1] + snake_width//2], snake_width//2)
    if snake_mv == 'u' or snake_mv == 'd':
        pygame.draw.circle(gameWindow, (255, 255, 255), [head[-1][0] + snake_width//2 + 3, head[-1][1] + snake_width//2], 2)
        pygame.draw.circle(gameWindow, (255, 255, 255), [head[-1][0] + snake_width//2 - 3, head[-1][1] + snake_width//2], 2)
    else:
        pygame.draw.circle(gameWindow, (255, 255, 255), [head[-1][0] + snake_width//2, head[-1][1] + snake_width//2 - 3], 2)
        pygame.draw.circle(gameWindow, (255, 255, 255), [head[-1][0] + snake_width//2, head[-1][1] + snake_width//2 + 3], 2)


def put_text(text, color, x, y, font, gameWindow):
    text_screen = font.render(text, True, color)
    gameWindow.blit(text_screen, [x, y])