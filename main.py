import pygame
from ball import Ball
from board import Board

pygame.init()


window_width = 900
window_height = 500

board_width = 10
board_height = 100

ball_radius = 7
        
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Pong!')


BACKGROUND_COLOR = 0, 20, 33
WHITE = 255, 255, 255

FPS = 60

def draw_window(boards, ball):
    window.fill(BACKGROUND_COLOR)
    
    pygame.draw.aaline(window, WHITE, (window_width//2, 0), (window_width//2, window_height))
    
    for board in boards:
        board.draw(window)

    ball.draw(window)
    

    pygame.display.update()


def handle_movement(left_board: Board, right_board: Board, keys_pressed):
    if keys_pressed[pygame.K_w] and left_board.y - 10>= 0:
        left_board.move()
    
    if keys_pressed[pygame.K_s] and left_board.y <= window_height- board_height -10:
        left_board.move(up=False)
   
    if keys_pressed[pygame.K_UP] and right_board.y - 10 >= 0:
        right_board.move()
    
    if keys_pressed[pygame.K_DOWN] and right_board.y <= window_height- board_height -10:
        right_board.move(up=False)
    
    

def main():
    run = True
    clock = pygame.time.Clock()
    
    left_board = Board(10, window_height//2 - board_height//2, board_width, board_height)
    right_board = Board(window_width - 20, window_height//2 - board_height//2, board_width, board_height)
    ball = Ball(window_width//2-ball_radius, window_height//2-ball_radius, ball_radius)
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        ball.move()    
        
        keys_pressed = pygame.key.get_pressed()
        handle_movement(left_board, right_board, keys_pressed)
        
    
        draw_window([left_board, right_board], ball)
    
    pygame.quit()


if __name__ == "__main__":
    main()
