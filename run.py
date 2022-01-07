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
snake_position = (0, 0)
snake_colour = (0, 159, 0)
snake_size = 1
snake_score = 0
snake_speed = 10

# Apple
apple_position = (0, 0)
apple_colour = (200, 0, 0)
 
game_over_font = pygame.font.SysFont("helvetica", 12)
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
 
def snake(game_board):
        pygame.draw.rect(game_board, snake_colour, [200, 200, 20, 20])
        pygame.draw.rect(game_board, white, [200, 200, 20, 20], 1)

def message(msg, color):
    """
  Creates the message after the snake has crashed into the wall or into it's self.
  """
    mesg = game_over_font.render(msg, True, white)
    game_board.blit(mesg, [screen_width/2, screen_height/2]) 

def gameLoop():
    """
  Game loop based on the game_over and game_end variables inside while and if loops.
  """
    game_over = False
    game_end = False
 
    snake_x = screen_width / 2
    snake_y = screen_height / 2
    snake_score = 0
    move_horizontal = 0
    move_vertical = 0

    apple_x = round(random.randrange(0, screen_width - snake_size) / grid_size) * grid_size
    apple_y = round(random.randrange(0, screen_height - snake_size) / grid_size) * grid_size

    while not game_over:
        while game_end == True:
            game_board.fill(black)
            message("You lost!\n Press Enter to Play Again\n Press Q to Quit", white)

            pygame.display.update()
  
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_end = False
                    if event.key == pygame.K_RETURN:
                        gameLoop()
 
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
        snake_score = 0
        background(game_board)
        font_score = pygame.font.SysFont("Courier", 16)
        scoreboard = font_score.render("Score "+str(snake_score), 1, (white))
        game_board.blit(scoreboard, (5, 10))

        

        pygame.draw.rect(game_board, apple_colour, [apple_x, apple_y, 20, 20])
        pygame.draw.rect(game_board, white, [apple_x, apple_y, 20, 20],1)
        
        pygame.draw.rect(game_board, snake_colour, [snake_x, snake_y, 20, 20])
        pygame.draw.rect(game_board, white, [snake_x, snake_y, 20, 20], 1)
        pygame.display.update()
 
        if snake_x == apple_x and snake_y == apple_y:
            print("Snake ate the apple")
            snake_score += 1
            apple_x = round(random.randrange(0, screen_width - snake_size) / grid_size) * grid_size
            apple_y = round(random.randrange(0, screen_height - snake_size) / grid_size) * grid_size

        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()