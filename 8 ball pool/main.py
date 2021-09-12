import pygame,sys,random
from settings import width,outerHeight,radius,height,colors,black,margin
from ball import Ball
from pocket import Pockets
from math import cos,radians,sin,degrees,atan

pygame.init()

display = pygame.display.set_mode((width, outerHeight))
clock = pygame.time.Clock()

def collision(ball1, ball2):
    dist = ((ball1.x - ball2.x)**2 + (ball1.y - ball2.y)**2)**0.5
    if dist <= radius*2:
        return True
    else:
        return False


def checkCollision():
    for i in range(len(balls)):
        for j in range(len(balls) - 1, i, -1):
            if collision(balls[i], balls[j]):
                if balls[i].x == balls[j].x:
                    pass
                else:
                    u1 = balls[i].speed
                    u2 = balls[j].speed

                    balls[i].speed = ((u1*cos(radians(balls[i].angle)))**2 + (u2*sin(radians(balls[j].angle)))**2)**0.3
                    balls[j].speed = ((u2*cos(radians(balls[j].angle)))**2 + (u1*sin(radians(balls[i].angle)))**2)**0.3

                    tangent = degrees((atan((balls[i].y - balls[j].y)/(balls[i].x - balls[j].x)))) + 90
                    angle = tangent + 90

                    balls[i].angle = (2*tangent - balls[i].angle)
                    balls[j].angle = (2*tangent - balls[j].angle)

                    balls[i].x += (balls[i].speed)*sin(radians(angle))
                    balls[i].y -= (balls[i].speed)*cos(radians(angle))
                    balls[j].x -= (balls[j].speed)*sin(radians(angle))
                    balls[j].y += (balls[j].speed)*cos(radians(angle))

noBalls = 15
balls = []
for i in range(noBalls):
    newBall = Ball(random.randrange(radius,width - radius),random.randrange(radius,height,radius),random.choice(colors),10,random.randrange(-180,180))
    balls.append(newBall)


noPockets = 6
pockets = []

p1 = Pockets(0, 0, black)
p2 = Pockets(width/2 - p1.r*2, 0, black)
p3 = Pockets(width - p1.r - margin - 5, 0, black)
p4 = Pockets(0, height - margin - 5 - p1.r, black)
p5 = Pockets(width/2 - p1.r*2, height - margin - 5 - p1.r, black)
p6 = Pockets(width - p1.r - margin - 5, height - margin - 5 - p1.r, black)

pockets.append(p1)
pockets.append(p2)
pockets.append(p3)
pockets.append(p4)
pockets.append(p5)
pockets.append(p6)

clock = pygame.time.Clock()
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    display.fill((255,255,255))

    for i in range(len(balls)):
        balls[i].draw(balls[i].x, balls[i].y)

    for i in range(len(balls)):
        balls[i].move()

    for i in range(noPockets):
        pockets[i].draw()

    for i in range(noPockets):
        pockets[i].checkPut(balls)


    checkCollision()

    pygame.display.update()
    clock.tick(60)