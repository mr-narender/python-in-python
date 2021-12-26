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
down = (0,1)
left = (-1,0)
right = (1,0)

class Snake():
    def __init__(snake):
      """
      Game loads with the "snake" in a random postion and direction. Starting with one block.
      """
      snake.length = 1
      snake.position = [((screen_width / 2), (screen_height / 2))]
      snake.direction = random.choice([up, down, left, right])
      snake.color = (48, 109, 223)
      snake.score = 0

    def snake_direction(snake):
        return snake.positions[0]

    def turn(snake, point):
        if snake.length > 1 and (point[0]*-1, point[1]*-1) == snake.direction:
            return
        else:
            snake.direction = point

    def move(snake):
        current_position = snake.snake_direction()
        x,y = snake.direction
        new_position = (((current_position[0]+(x*gridsize))%screen_width), (current_position[1]+(y*gridsize))%screen_height)
        if len(snake.positions) > 2 and new_position in snake.positions[2:]:
            snake.reset()
        else:
            snake.positions.insert(0,new_position)
            if len(snake.positions) > snake.length:
                snake.positions.pop()