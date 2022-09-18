import pygame

pygame.init()


window_width = 900
window_height = 500
        
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Pong!')


BACKGROUND_COLOR = 0, 20, 33
WHITE = 255, 255, 255

FPS = 60

def draw_window():
    window.fill(BACKGROUND_COLOR)

    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    
        draw_window()
    
    pygame.quit()


if __name__ == "__main__":
    main()
