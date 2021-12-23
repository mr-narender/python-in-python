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