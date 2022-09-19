import pygame

class Board:
    WHITE = 255, 255, 255
    VEL = 7
    
    def __init__(self, x, y, width, height) -> None:
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height
    
    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.WHITE,(self.x, self.y, self.width, self.height))
        
    def move(self, up = True):
        if up == True:
            self.y -= self.VEL
        else:
            self.y += self.VEL

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y