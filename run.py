import pygame
import sys
import random

# Title on game window
pygame.display.set_caption('Python in Python')

# Sets screen width
screen_width = 400
screen_height = 400

# Sets grid size
gridsize = 20
# Produces a 20 x 20 grid
grid_width = screen_width/gridsize
grid_height = screen_height/gridsize

# Using a Y and X axis, keydown actions create the below movements.
up = (0,-1)
right = (1,0)
down = (0,1)
left = (-1,0)

# Colours
lighter_square = (38,52,69)
darker_square = (32,41,55)
snake = (0, 159, 0)
apple = (200, 0, 0)
white = (255, 255, 255)

snake_score = 0

def snake_grid(surface):
  """
  Creates the chequered grid for the game based on if the grid number is disable by two or not. If it is apply the darker colour if not, apply the lighter colour.
  """
  for y in range(0, int(grid_height)):
    for x in range(0, int(grid_width)):
      if (x+y)%2 == 0:
          light_square = pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
          pygame.draw.rect(surface,(38,52,69), light_square)
      else:
        dark_square = pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
        pygame.draw.rect(surface, (32,41,55), dark_square)

class Snake():
  def __init__(snake):
      """
      Game loads with the "snake" moving from left to right in centre of the grid. Starting with one block.
      """
      snake.size = 1
      snake.position = ([((screen_width / 2), (screen_height / 2))])
      snake.direction = right
      snake.color = (48, 109, 223)
      snake.score = 0
  
  def snake_direction(snake):
      """
      Front square denotes the head of the snake, 
      """
      return snake.position[0]

  def turn(snake, point):
        if snake.size > 1 and (point[0] * -1,
                                 point[1] * -1) == snake.direction:
            return
        else:
            snake.direction = point

  def move(snake):
        current_position = snake.snake_direction()
        x,y = snake.direction
        new_position = (((current_position[0]+(x*gridsize))%screen_width), (current_position[1]+(y*gridsize))%screen_height)
        if len(snake.position) > 2 and new_position in snake.position[2:]:
            snake.restart()
        else:
            snake.position.insert(0,new_position)
            if len(snake.position) > snake.size:
                snake.position.pop()

  def restart(snake):
    """
    When the snake hits itself the game restarts from the beginning with the snake back to one square and the score on zero
    """
    snake.size = 1
    snake.position = [((screen_width/2), (screen_height/2))]
    snake.direction = right
    snake.score = 0

  def draw(snake,surface):
        for p in snake.position:
            r = pygame.Rect((p[0], p[1]), (gridsize,gridsize))
            pygame.draw.rect(surface, snake.color, r)
            pygame.draw.rect(surface, (255, 255, 255), r, 1)





class Apple():
  def __init__(apple):

      apple.position = (0,0)
      apple.color = (200, 0, 0)
      apple.random_position()

  def random_position(apple):
        apple.position = (random.randint(0, grid_width-1)*gridsize, random.randint(0, grid_height-1)*gridsize)

  def draw(apple, surface):
        r = pygame.Rect((apple.position[0], apple.position[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, apple.color, r)
        pygame.draw.rect(surface, (255, 255, 255), r, 1)




def main():
  pygame.init()


main()
