import random
import sys
import time

import pygame

pygame.init()
# Screen Dimensions
screen_width = 400
screen_height = 400
# Game Window
game_board = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Python in Python")
clock = pygame.time.Clock()
# Colours
white = (255, 255, 255)
black = (0, 0, 0)
lighter_square = (38, 52, 69)
darker_square = (32, 41, 55)
# Grid dimensions
grid_size = 20
# Produces a 20 x 20 grid
grid_width = 20
grid_height = 20
# Snake
snake_position = (0, 0)
snake_colour = (0, 159, 0)
snake_x = screen_width / 2
snake_y = screen_height / 2
snake_size = 20
current_score = 0
snake_speed = 5
# Apple
apple_position = (0, 0)
apple_colour = (200, 0, 0)
apple_x = round(random.randrange(0, screen_width - snake_size) / grid_size) * grid_size
apple_y = round(random.randrange(0, screen_height - snake_size) / grid_size) * grid_size
# Fonts
game_quit_font = pygame.font.SysFont("helvetica", 12)
score_font = pygame.font.SysFont("Courier", 16)
# Other
game_quit = True
game_over = True


IS_APPLE_SHOWN = False
apple_x, apple_y = [0, 0]
snake_head = []
snake_list = [[snake_x, snake_y]]
snake_length = 1
move_horizontal, move_vertical = [0, 0]
GAME_PLAY_ON = False


def render_background():
    """
    Creates the chequered grid for the game based on if the grid number is disable by two or not. If it is apply the darker colour if not, apply the lighter colour.
    """
    global game_board
    for y in range(int(grid_height)):
        for x in range(int(grid_width)):
            if (x + y) % 2 == 0:
                square_one = pygame.Rect(
                    (x * grid_size, y * grid_size), (grid_size, grid_size)
                )
                pygame.draw.rect(game_board, (lighter_square), square_one)
            else:
                square_two = pygame.Rect(
                    (x * grid_size, y * grid_size), (grid_size, grid_size)
                )
                pygame.draw.rect(game_board, (darker_square), square_two)
    pygame.display.update()


def show_score():
    """
    Creates and displays the live updating score as the game is played.
    """
    global current_score
    font_score = pygame.font.SysFont("Courier", 26)
    scoreboard = font_score.render("Score: " + str(current_score), True, (white))
    game_board.blit(scoreboard, (5, 10))
    pygame.display.update()


# def high_score():
#     high_score = current_score
#     font_score = pygame.font.SysFont("Courier", 16)
#     scoreboard = font_score.render("High Score: "+str(current_score), True, (white))
#     game_board.blit(scoreboard, (245, 10))


def draw_snake():
    """
    Creates and draws the snake using the variables and coordinates
    """
    global game_board, snake_list
    for x, y in snake_list:
        print(snake_list)
        pygame.draw.rect(game_board, snake_colour, [x, y, 20, 20])
        pygame.draw.rect(game_board, white, [x, y, 20, 20], 1)
    pygame.display.update()


def render_new_apple():
    """
    Creates and draws the apple using the variables and coordinates
    """
    global game_board, IS_APPLE_SHOWN, apple_x, apple_y
    if not IS_APPLE_SHOWN:
        apple_x = (
            round(random.randrange(0, screen_width - grid_size) / grid_size) * grid_size
        )
        apple_y = (
            round(random.randrange(0, screen_height - grid_size) / grid_size)
            * grid_size
        )
    pygame.draw.rect(game_board, apple_colour, [apple_x, apple_y, 20, 20])
    pygame.draw.rect(game_board, white, [apple_x, apple_y, 20, 20], 1)
    IS_APPLE_SHOWN = True
    pygame.display.update()
    return True


def is_apple_eaten():
    """
    Detects whether the apple has been eaten and updates the scores, speed and apple postition accordingly.
    """
    global IS_APPLE_SHOWN, snake_x, apple_x, snake_y, apple_y
    if snake_x == apple_x and snake_y == apple_y:
        print("Snake ate the apple")
        IS_APPLE_SHOWN = False

        return True
    return False


def update_game_data():
    global current_score, snake_speed, snake_length
    current_score += 10
    snake_speed += 0.5
    snake_length += 1
    show_score()


def message(msg, color):
    """
    Creates the message after the snake has crashed into the wall or into it's self.
    """
    mesg = game_quit_font.render(msg, True, white)
    game_board.blit(mesg, [screen_width / 5, screen_height / 2])


def keyboard_commands():
    """
    Uses the keyboard commands from the direction arrows to move the snake around the grid.
    """
    global move_horizontal, move_vertical
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_quit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left")
                move_horizontal = -20
                move_vertical = 0
            elif event.key == pygame.K_RIGHT:
                print("Right")
                move_horizontal = 20
                move_vertical = 0
            elif event.key == pygame.K_UP:
                print("Up")
                move_vertical = -20
                move_horizontal = 0
            elif event.key == pygame.K_DOWN:
                print("Down")
                move_vertical = 20
                move_horizontal = 0


def init_game():
    """
    Game loop based on the game_quit and game_over variables inside while and if loops.
    """
    global IS_APPLE_SHOWN, apple_x, apple_y, snake_head, snake_list, move_horizontal, move_vertical, snake_x, snake_y, snake_length, snake_speed, current_score

    while True:
        render_background()
        show_score()
        render_new_apple()

        keyboard_commands()

        snake_x += move_horizontal
        snake_y += move_vertical
        snake_head = [snake_x, snake_y]
        if snake_head not in snake_list:
            snake_list.append(snake_head)
        print(snake_x, snake_y, snake_list)

        if len(snake_list) > snake_length:
            del snake_list[0 : len(snake_list) - snake_length]
            # snake_list = snake_list[:snake_length]

        if len(snake_list) >= 1 and did_snake_hit_itself():
            break

        if is_apple_eaten():
            update_game_data()
            render_new_apple()

        draw_snake()

        clock.tick(snake_speed)

        if did_snake_hit_wall():
            time.sleep(2)
            break


def did_snake_hit_wall():
    """
    Detects whether the snake has hit the wall and if it has, it will end the game.
    """
    global snake_x, snake_y, screen_width, screen_height
    if (
        snake_x >= screen_width
        or snake_x < 0
        or snake_y >= screen_height
        or snake_y < 0
    ):
        print("Snake hit the wall")
        return True
    return False


def did_snake_hit_itself():
    global snake_list, snake_head
    return any(x == snake_head for x in snake_list[:-1])


def reset_game():
    """
    Resets the game to the original state.
    """
    global game_quit, game_over, current_score, snake_speed, snake_length, IS_APPLE_SHOWN
    IS_APPLE_SHOWN = False
    current_score = 0
    snake_speed = 5
    snake_length = 1
    snake_list.clear()


def show_prompt_screen():
    reset_game()
    game_board.fill(black)
    msg_str = "Press Enter key to start"
    message(msg_str, white)
    pygame.display.update()


def load_game_engine():
    """
    Loads the game engine and runs the game loop.
    """
    while True:
        show_prompt_screen()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                init_game()


if __name__ == "__main__":
    load_game_engine()
