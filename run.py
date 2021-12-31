import pygame
import sys
import random

# Title on game window
pygame.display.set_caption('Python in Python')

# Screen dimensions
screen_width = 400
screen_height = 400

# Grid dimensions
grid_size = 20
# Produces a 20 x 20 grid
grid_width = 20
grid_height = 20

# Using a Y and X axis, keydown actions create the below movements.
up = (0, -1)
right = (1, 0)
down = (0, 1)
left = (-1, 0)

# Colours
lighter_square = (38, 52, 69)
darker_square = (32, 41, 55)
white = (255, 255, 255)

# Snake
snake_position = (200, 200)
snake_head_colour = (0, 159, 0)
snake_body_colour = (0, 0, 159)
snake_size = 1
snake_score = 0
snake_speed = 10

# Apple
apple_position = (200, 0)
apple_colour = (200, 0, 0)


def background(surface):
    """
  Creates the chequered grid for the game based on if the grid number is disable by two or not. If it is apply the darker colour if not, apply the lighter colour.
  """
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if (x + y) % 2 == 0:
                square_one = pygame.Rect((x * grid_size, y * grid_size),
                                         (grid_size, grid_size))
                pygame.draw.rect(surface, (lighter_square), square_one)
            else:
                square_two = pygame.Rect((x * grid_size, y * grid_size),
                                         (grid_size, grid_size))
                pygame.draw.rect(surface, (darker_square), square_two)


def snake(surface):
    """
  Creates the snake using the pygame.rect, loads the snake in the given position via the variable snake_position and coloured in snake_colour. A further white square has been used for a border.
  """
    snake_square = pygame.Rect((snake_position[0], snake_position[1]),
                               (grid_size, grid_size))
    pygame.draw.rect(surface, snake_head_colour, snake_square)
    pygame.draw.rect(surface, (white), snake_square, 1)


def snake_direction(snake):
    """
  Front square denotes the head of the snake,
  """
    return snake.head[0]


def random_position(apple):
    """
  Randomise the position of the apple on the game load.
  """
    apple.position = (random.randint(0, grid_width - 1) * grid_size,
                      random.randint(0, grid_height - 1) * grid_size)


class Apple():
    def __init__(apple):

        apple.position = (0, 0)
        apple.color = (200, 0, 0)
        apple.random_position()

    def random_position(apple):
        apple.position = (random.randint(0, grid_width - 1) * grid_size,
                          random.randint(0, grid_height - 1) * grid_size)

    def create_apple(apple, surface):
      """
      Creates the apple using the pygame.rect, loads the apple in the given position via the variable apple_position and coloured in apple_colour. A further white square has been used for a border.
      """
      apple_square = pygame.Rect((apple.position[0], apple.position[1]),
                                   (grid_size, grid_size))
      pygame.draw.rect(surface, apple.color, apple_square)
      pygame.draw.rect(surface, (white), apple_square, 1)


# def create_apple(apple, surface):
#     """
#   Creates the apple using the pygame.rect, loads the apple in the given position via the variable apple_position and coloured in apple_colour. A further white square has been used for a border.
#   """
#     apple_square = pygame.Rect((apple.position[0], apple.position[1]),
#                                (grid_size, grid_size))
#     pygame.draw.rect(surface, apple_colour, apple_square)
#     pygame.draw.rect(surface, (white), apple_square, 1)


def press_keyboard(snake):
    """
  Event listener to move the snake based on which direction key is pressed 
  """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.turn(up)
            elif event.key == pygame.K_DOWN:
                snake.turn(down)
            elif event.key == pygame.K_LEFT:
                snake.turn(left)
            elif event.key == pygame.K_RIGHT:
                snake.turn(right)


def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    surface = pygame.Surface(screen.get_size())
    background(surface)
    snake(surface)
    apple = Apple()
    apple.create_apple(surface)

    font_score = pygame.font.SysFont("Courier", 16)
    text = font_score.render("Score {0}".format(snake_score), 1, (white))

    screen.blit(surface, (0, 0))
    screen.blit(text, (5, 10))
    pygame.display.update()

    # while (True):
    #   apple.random_position()


main()
