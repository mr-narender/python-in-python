import pygame
import sys
import random
 
pygame.init()
  
screen_width = 400
screen_height = 400
 
game_board = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Python in Python')
 
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
snake_position = (200, 200)
snake_colour = (0, 159, 0)
snake_size = 20
snake_score = 0
snake_speed = 10

# Apple
apple_position = (200, 0)
apple_colour = (200, 0, 0)
 
lost_font = pygame.font.SysFont("helvetica", 20)
score_font = pygame.font.SysFont("Courier", 16)

def background(game_board):
    """
  Creates the chequered grid for the game based on if the grid number is disable by two or not. If it is apply the darker colour if not, apply the lighter colour.
  """
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if (x + y) % 2 == 0:
                square_one = pygame.Rect((x * grid_size, y * grid_size),
                                         (grid_size, grid_size))
                pygame.draw.rect(game_board, (lighter_square), square_one)
            else:
                square_two = pygame.Rect((x * grid_size, y * grid_size),
                                         (grid_size, grid_size))
                pygame.draw.rect(game_board, (darker_square), square_two)
 
def snake(snake_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_board, snake_colour, [x[0], x[1], snake_size, snake_size])
        pygame.draw.rect(game_board, white, [x[0], x[1], snake_size, snake_size],1)

def snake_score(score):
    value = score_font.render("Score: " + str(score), True, white)
    game_board.blit(value, [5, 10])

def message(msg, color):
    mesg = lost_font.render(msg, True, color)
    game_board.blit(mesg, [100, screen_height / 2]) 

 
def gameloop():
    game_over = False
    game_end = False
 
    snake_x = screen_width / 2
    snake_y = screen_height / 2
 
    move_horizontal = 0
    move_vertical = 0
 
    snake_list = []
    snake_length = 1
 
    apple_x = round(random.randrange(0, screen_width - snake_size) / grid_size) * grid_size
    apple_y = round(random.randrange(0, screen_height - snake_size) / grid_size) * grid_size
 
    while not game_over:
 
        while game_end == True:
            game_board.fill(black)
            message("You lost!\n Press Enter to Play Again\n Press Q to Quit", white)
            snake_score(snake_length - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_end = False
                    if event.key == pygame.K_RETURN:
                        gameloop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_horizontal = -20
                    move_vertical = 0
                elif event.key == pygame.K_RIGHT:
                    move_horizontal = 20
                    move_vertical = 0
                elif event.key == pygame.K_UP:
                    move_vertical = -20
                    move_horizontal = 0
                elif event.key == pygame.K_DOWN:
                    move_vertical = 20
                    move_horizontal = 0
 
        if snake_x >= screen_width or snake_x < 0 or snake_y >= screen_height or snake_y < 0:
            game_end = True
        snake_x += move_horizontal
        snake_y += move_vertical
        background(game_board)
        snake(snake_size, snake_list)

        pygame.draw.rect(game_board, apple_colour, [apple_x, apple_y, grid_size, grid_size])
        pygame.draw.rect(game_board, white, [apple_x, apple_y, grid_size, grid_size],1)
        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]


 
        snake_score(snake_length-1)
 
        pygame.display.update()
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameloop()

