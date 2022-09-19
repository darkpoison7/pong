import pygame

class Ball:
    MAX_VEL = 5
    WHITE = 255, 255, 255
    
    def __init__(self, x, y, radius) -> None:
        self.x = x
        self.y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = self.MAX_VEL
    
    def draw(self, screen: pygame.Surface):
        pygame.draw.ellipse(screen, self.WHITE,(self.x, self.y, self.radius * 2, self.radius * 2))
        
    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel