import pygame
from settings import radius,friction,width,margin,height
from math import cos,sin,radians


class Ball:
    def __init__(self, x, y, colors,speed,angle):
        self.x = x + radius
        self.y = y + radius
        self.colors = colors
        self.speed = speed
        self.angle = angle
        self.display = pygame.display.get_surface()
    
    def draw(self, x, y):
        pygame.draw.ellipse(self.display, self.colors, (x - radius, y - radius, radius*2, radius*2))

        # Moves the Ball around the Screen
    def move(self):
        self.speed -= friction
        if self.speed <= 0:
            self.speed = 0
        self.x = self.x + self.speed*cos(radians(self.angle))
        self.y = self.y + self.speed*sin(radians(self.angle))

        if not (self.x < width - radius - margin):
            self.x = width - radius - margin
            self.angle = 180 - self.angle
        if not(radius + margin < self.x):
            self.x = radius + margin
            self.angle = 180 - self.angle
        if not (self.y < height - radius - margin):
            self.y = height - radius - margin
            self.angle = 360 - self.angle
        if not(radius + margin < self.y):
            self.y = radius + margin
            self.angle = 360 - self.angle