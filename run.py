import pygame
import sys
import random

class Snake():
    def __init__(snake):
        snake.length = 1
        snake.positions = [((screen_width/2), (screen_height/2))]
        snake.direction = random.choice([up, down, left, right])
        snake.color = (48, 109, 223)
        snake.score = 0

    def get_head_position(snake):
        return snake.positions[0]

    def turn(snake, point):
        if snake.length > 1 and (point[0]*-1, point[1]*-1) == snake.direction:
            return
        else:
            snake.direction = point

    def move(snake):
        current_position = snake.get_head_position()
        x,y = snake.direction
        new_position = (((current_position[0]+(x*gridsize))%screen_width), (current_position[1]+(y*gridsize))%screen_height)
        if len(snake.positions) > 2 and new_position in snake.positions[2:]:
            snake.reset()
        else:
            snake.positions.insert(0,new_position)
            if len(snake.positions) > snake.length:
                snake.positions.pop()