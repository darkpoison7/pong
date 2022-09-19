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
   
def handle_collisions(ball: Ball, left_board: Board, right_board: Board):
    if ball.y + ball_radius >= window_height:
        ball.y_vel *= -1
    
    if ball.y - ball_radius <= 0:
        ball.y_vel *= -1
        
    if ball.x_vel < 0:
        if ball.y >= left_board.y and ball.y <= left_board.y + left_board.height:
            if ball.x - ball_radius <= left_board.x + left_board.width:
                ball.x_vel *= -1
                middle_y = left_board.y + left_board.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (left_board.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel

                
    else:
        if ball.y >= right_board.y and ball.y <= right_board.y + right_board.height:
            if ball.x + ball_radius >= right_board.x:
                ball.x_vel *= -1
                middle_y = right_board.y + right_board.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (right_board.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel



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
        
        if ball.x - ball_radius <= 0: 
            ball.reset()
            
        
        if ball.x + ball_radius > window_width:
            ball.reset()
            

        
        keys_pressed = pygame.key.get_pressed()
        handle_movement(left_board, right_board, keys_pressed)
        
    
        draw_window([left_board, right_board], ball)
        handle_collisions(ball, left_board, right_board)
    
    pygame.quit()


if __name__ == "__main__":
    main()
