import pygame
import os
from ball import Ball
from board import Board


# initialising pygame
pygame.init()
pygame.font.init()

# constants
FPS = 60

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 500

BOARD_WIDTH = 10
BOARD_HEIGHT = 100

BALL_RADIUS = 7

WINNING_SCORE = 10

# colors
WHITE = 255, 255, 255
BACKGROUND_COLOR = 0, 20, 33

# game screen config
pygame.display.set_caption('Pong!')
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# fonts
SCORE_FONT = pygame.font.Font(os.path.join('assets', 'ka1.ttf'), 20)
WINNER_FONT = pygame.font.Font(os.path.join('assets', 'ka1.ttf'), 64)

# updates the elements on the WINDOW on each frame
def draw_WINDOW(WINDOW, boards, ball, left_score, right_score):
    WINDOW.fill(BACKGROUND_COLOR)
    pygame.draw.aaline(WINDOW, WHITE, (WINDOW_WIDTH//2, 0), (WINDOW_WIDTH//2, WINDOW_HEIGHT))
    
    left_score_text = SCORE_FONT.render(str(left_score), 1, WHITE)
    right_score_text = SCORE_FONT.render(str(right_score), 1, WHITE)
    
    WINDOW.blit(left_score_text, (20, 20))
    WINDOW.blit(right_score_text, (WINDOW_WIDTH - right_score_text.get_width() - 20,20))
    
    for board in boards:
        board.draw(WINDOW)

    ball.draw(WINDOW)

    pygame.display.update()

# writes the winner name on the screen
def draw_winner_text(WINDOW, text):
    winner_text = WINNER_FONT.render(text, 1, WHITE)
    sub_text = SCORE_FONT.render('The game will restart in 5s', 1, WHITE)
    WINDOW.blit(winner_text, (WINDOW_WIDTH // 2 - winner_text.get_width() // 2, WINDOW_HEIGHT //2 - winner_text.get_height()//2))
    WINDOW.blit(sub_text, (WINDOW_WIDTH // 2 - sub_text.get_width() // 2,  WINDOW_HEIGHT //2 + winner_text.get_height()//2 + 20))
    pygame.display.update()
    
# handles the movement of left and right boards
def handle_movement(left_board: Board, right_board: Board, keys_pressed):
    if keys_pressed[pygame.K_w] and left_board.y - 10>= 0:
        left_board.move()
    
    if keys_pressed[pygame.K_s] and left_board.y <= WINDOW_HEIGHT- BOARD_HEIGHT -10:
        left_board.move(up=False)
   
    if keys_pressed[pygame.K_UP] and right_board.y - 10 >= 0:
        right_board.move()
    
    if keys_pressed[pygame.K_DOWN] and right_board.y <= WINDOW_HEIGHT- BOARD_HEIGHT -10:
        right_board.move(up=False)


# implements an algoriths to handle collision of the ball with the boards and the edges   
def handle_collisions(ball: Ball, left_board: Board, right_board: Board):
    if ball.y + BALL_RADIUS >= WINDOW_HEIGHT:
        ball.y_vel *= -1
    
    if ball.y - BALL_RADIUS <= 0:
        ball.y_vel *= -1
        
    if ball.x_vel < 0:
        if ball.y >= left_board.y and ball.y <= left_board.y + left_board.height:
            if ball.x - BALL_RADIUS <= left_board.x + left_board.width:
                ball.x_vel *= -1
                middle_y = left_board.y + left_board.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (left_board.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel

                
    else:
        if ball.y >= right_board.y and ball.y <= right_board.y + right_board.height:
            if ball.x + BALL_RADIUS >= right_board.x:
                ball.x_vel *= -1
                middle_y = right_board.y + right_board.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (right_board.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel


def main():
    run = True
    clock = pygame.time.Clock()

    # initialising game objects
    left_board = Board(10, WINDOW_HEIGHT//2 - BOARD_HEIGHT//2, BOARD_WIDTH, BOARD_HEIGHT)
    right_board = Board(WINDOW_WIDTH - 20, WINDOW_HEIGHT//2 - BOARD_HEIGHT//2, BOARD_WIDTH, BOARD_HEIGHT)
    ball = Ball(WINDOW_WIDTH//2-BALL_RADIUS, WINDOW_HEIGHT//2-BALL_RADIUS, BALL_RADIUS)
    
    # score count
    left_score = 0
    right_score = 0
    
    # main game loop
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        ball.move()
        
        # on right point
        if ball.x <= 0:
            ball.reset()
            right_score += 1
            
        # on left point
        if ball.x > WINDOW_WIDTH:
            ball.reset()
            left_score += 1
        
        
        keys_pressed = pygame.key.get_pressed()
        handle_movement(left_board, right_board, keys_pressed)
        
    
        draw_WINDOW(WINDOW, [left_board, right_board], ball, left_score, right_score)
        handle_collisions(ball, left_board, right_board)
        
        
        # when win condition is met
        if left_score == WINNING_SCORE:
            draw_winner_text(WINDOW, 'Left Player Won!')
            pygame.time.delay(5000)
            ball.reset()
            left_board.reset()
            right_board.reset()
            left_score = 0
            right_score = 0

        if right_score == WINNING_SCORE:
            draw_winner_text(WINDOW, 'Right Player Won!')
            pygame.time.delay(5000)
            ball.reset()
            left_board.reset()
            right_board.reset()
            left_score = 0
            right_score = 0
    
    pygame.quit()

if __name__ == "__main__":
    main()