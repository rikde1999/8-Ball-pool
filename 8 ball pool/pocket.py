import pygame
from settings import radius,margin

class Pockets:
    def __init__(self, x, y, color):
        self.r = margin/2
        self.x = x + self.r + 10
        self.y = y + self.r + 10
        self.color = color
        self.display = pygame.display.get_surface()
        
    def draw(self):
        pygame.draw.ellipse(self.display, self.color, (self.x - self.r, self.y - self.r, self.r*2, self.r*2))

    def checkPut(self,balls):
        ballsCopy = balls[:]
        for i in range(len(balls)):
            dist = ((self.x - balls[i].x)**2 + (self.y - balls[i].y)**2)**0.5
            if dist < self.r + radius:
                if balls[i] in ballsCopy:
                    ballsCopy.remove(balls[i])

        balls = ballsCopy[:]