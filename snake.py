import random

try:
    import pygame
except:
    print('Installing Pygame library......')
    import os
    os.system('pip install pygame')

from important_variables import screen_width, screen_height, gameWindow, colour as color, score_board_size, apple_width
from assets import appleImg, overImg, welcm
from paths import score_file, bite_sound, game_over_sound


from visuals import put_text, plot_snake, draw_background

from game import start_game

pygame.init()

pygame.mixer.init()
# creating window


pygame.display.set_caption("Snake Game")


# Game specific variables
start_on = True


exit_game, game_over, snake_x, snake_y, snake_width, FPS, snake_mv, food_pos, head, snake_len, clock, font, font2 = start_game()

with open(score_file, "r") as f:
    high_score = int(f.read())


# Creating a game loop
sound1 = pygame.mixer.Sound(bite_sound)
while not exit_game:
    while start_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start_on = False
        gameWindow.blit(welcm, (0, 0))
        pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake_mv != 'l':
                snake_mv = 'r'
            elif event.key == pygame.K_LEFT and snake_mv != 'r':
                snake_mv = 'l'
            elif event.key == pygame.K_UP and snake_mv != 'd':
                snake_mv = 'u'
            elif event.key == pygame.K_DOWN and snake_mv != 'u':
                snake_mv = 'd'
    if snake_mv == 'r':
        snake_x += 4
    elif snake_mv == 'l':
        snake_x -= 4
    elif snake_mv == 'u':
        snake_y -= 4
    elif snake_mv == 'd':
        snake_y += 4


    if snake_x in range(food_pos[0], food_pos[0] + apple_width) and snake_y in range(food_pos[1], food_pos[1] + apple_width):
        snake_len += 1
        sound1.play()
        head.append([snake_x, snake_y])
        food_pos = (random.randint(1, screen_width-apple_width), random.randint(score_board_size + 10, screen_height-apple_width))
    else:
        # if len(head) > snake_len:
        head.append([snake_x, snake_y])
        del head[0]
    # gameWindow.fill((255, 255, 255))
    draw_background(gameWindow)
    if snake_len - 1 > high_score:
        high_score = snake_len - 1
    if (head[-1][0] >= (screen_width - snake_width)) or (head[-1][0] <= 1) or (head[-1][1] >= screen_height - snake_width) or (head[-1][1] <= score_board_size) or (head[-1] in head[:-1]):
        pygame.mixer.music.load(game_over_sound)
        pygame.mixer.music.play()
        with open(score_file, "w") as f:
            f.write(str(high_score))
        game_over = True
        while game_over == True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        exit_game, game_over, snake_x, snake_y, snake_width, FPS, snake_mv, food_pos, head, snake_len, clock, font, font2 = start_game()
                        # gameWindow.fill((255, 255, 255))
                        draw_background(gameWindow)
                        put_text('score : ' + str(snake_len - 1), color, 10, 10, font, gameWindow)
                        put_text('highest score : ' + str(high_score), color, screen_width//2, 10, font, gameWindow)
                        pygame.draw.line(gameWindow, (0, 0, 0), (0, score_board_size), (screen_width, score_board_size), 5)
                        gameWindow.blit(appleImg, (food_pos[0], food_pos[1]))
                        plot_snake(gameWindow, head, snake_width, color, snake_len, snake_mv)
                        pygame.display.update()
                        clock.tick(FPS)
                        game_over = False
                        continue
                    else:
                        pygame.quit()
                        exit()
            pygame.display.update()
            clock.tick(FPS)
            gameWindow.blit(overImg, ((screen_width - 220)//2, 180))
            put_text('Game over', color, 200, 400, font2, gameWindow)
            put_text('press ENTER to restart or any other key', color, 20, 500, font, gameWindow)
        # break
    put_text('score : ' + str(snake_len - 1), color, 10, 10, font, gameWindow)
    put_text('highest score : ' + str(high_score), color, screen_width//2, 10, font, gameWindow)
    pygame.draw.line(gameWindow, (0, 0, 0), (0, score_board_size), (900, score_board_size), 5)
    gameWindow.blit(appleImg, (food_pos[0], food_pos[1]))
    plot_snake(gameWindow, head, snake_width, color, snake_len, snake_mv)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
exit()
