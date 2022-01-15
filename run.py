import pygame
import random
pygame.init()
# Screen dimensions
screen_x = 400
screen_y = 400
# Game window
game_board = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("Python in Python")
clock = pygame.time.Clock()
# Colours
white = (255, 255, 255)
black = (0, 0, 0)
light_sq = (38, 52, 69)
dark_sq = (32, 41, 55)
# Grid dimensions
grid_sq = 20
# Produces a 20 x 20 grid
grid_width = 20
grid_height = 20
# Snake
snake_position = (0, 0)
snake_colour = (0, 159, 0)
snake_x = screen_x / 2
snake_y = screen_y / 2
snake_size = 20
snake_score = 0
snake_speed = 5
# Apple
apple_position = (0, 0)
apple_colour = (200, 0, 0)
apple_x = round(random.randrange(0, screen_x - snake_size) / grid_sq) * grid_sq
apple_y = round(random.randrange(0, screen_y - snake_size) / grid_sq) * grid_sq
# Fonts
game_over_font = pygame.font.SysFont("helvetica", 12)
score_font = pygame.font.SysFont("Courier", 16)


def background(game_board):
    """
  Creates the chequered grid for the game based on
  if the grid number is disable by two or not.
  If it is apply the dark colour if not, apply the light colour.
  """
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if (x + y) % 2 == 0:
                sq_one = pygame.Rect((x * grid_sq, y * grid_sq), (grid_sq, grid_sq))
                pygame.draw.rect(game_board, (light_sq), sq_one)
            else:
                sq_two = pygame.Rect((x * grid_sq, y * grid_sq), (grid_sq, grid_sq))
                pygame.draw.rect(game_board, (dark_sq), sq_two)


def snake(game_board):
    """
  Creates and draws the snake using the variables and coordinates
  """
    for x, y in snake_list:
        pygame.draw.rect(game_board, snake_colour, [x, y, 20, 20])
        pygame.draw.rect(game_board, white, [x, y, 20, 20], 1)


def apple(game_board):
    """
  Creates and draws the apple using the variables and coordinates
  """
    pygame.draw.rect(game_board, apple_colour, [apple_x, apple_y, 20, 20])
    pygame.draw.rect(game_board, white, [apple_x, apple_y, 20, 20], 1)


def level_up():
    """
  Increases speed, score and snake length.
  """
    global snake_score
    global snake_speed
    global snake_length

    snake_score += 10
    snake_speed += 0.5
    snake_length += 1

    return snake_speed


def apple_eaten(snake_x, apple_x, snake_y, apple_y):
    """
  Detects whether the apple has been eaten and updates
  the scores, speed and apple postition accordingly.
  """
    if snake_x == apple_x and snake_y == apple_y:
        level_up()
        print("Snake ate the apple")
        apple_x = round(random.randrange(0, screen_x - grid_sq) / grid_sq) * grid_sq
        apple_y = round(random.randrange(0, screen_y - grid_sq) / grid_sq) * grid_sq
    return snake_x, apple_x, snake_y, apple_y, snake_speed


def message(msg, color):
    """
  Creates the message after the snake has crashed
  into the wall or into it's self.
  """
    mesg = game_over_font.render(msg, True, white)
    game_board.blit(mesg, [screen_x/3.5, screen_y/2])


def keyboard_commands(move_x, move_y):
    """
  Uses the keyboard commands from the direction
  arrows to move the snake around the grid.
  """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_x = -20
                move_y = 0
            elif event.key == pygame.K_RIGHT:
                move_x = 20
                move_y = 0
            elif event.key == pygame.K_UP:
                move_y = -20
                move_x = 0
            elif event.key == pygame.K_DOWN:
                move_y = 20
                move_x = 0
    return move_x, move_y


def show_score():
    """
  Creates and displays the live updating score as the game is played.
  """
    font_score = pygame.font.SysFont("Courier", 16)
    scoreboard = font_score.render("Score: "+str(snake_score), True, (white))
    game_board.blit(scoreboard, (5, 10))


def game_loop():
    """
  Game loop based on the game_over
  variables inside while and if loops.
  """
    game_over = False
    global snake_score
    global snake_speed
    global snake_length
    global apple_x
    global apple_y
    global snake_list
    global snake_head

    snake_x = screen_x / 2
    snake_y = screen_y / 2
    snake_score = 0
    snake_length = 1
    snake_list = []
    snake_speed = 5
    move_x = 0
    move_y = 0

    while game_over == False:
        move_x, move_y = keyboard_commands(move_x, move_y)
        snake_x += move_x
        snake_y += move_y
        background(game_board)
        apple(game_board)
        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True

        snake(game_board)
        scoreboard = show_score()
        pygame.display.update()
        snake_x, apple_x, snake_y, apple_y, snake_speed = apple_eaten(snake_x, apple_x, snake_y, apple_y)
        clock.tick(snake_speed)

        if snake_x >= screen_x or snake_x < 0 or snake_y >= screen_y or snake_y < 0:
            game_over = True

        while game_over == True:
            game_board.fill(black)
            message("You Lost! Press Enter to play again", white)
            show_score()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()

            pygame.display.update()
game_loop()
