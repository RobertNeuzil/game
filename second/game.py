import pygame


WIDTH = 480
HEIGHT = 500
RUNNING = True
CHARWIDTH = 30
CHARHEIGHT = 30
POSITIONX = 50
POSITIONY = 375
RED = (255, 0, 0)
BLACK = (0, 0, 0)
vel = 5

# create and draw
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Robert's Game")


#game loop
while RUNNING:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and POSITIONX > 0:
        POSITIONX -= vel
    if keys[pygame.K_RIGHT] and POSITIONX < (WIDTH - CHARWIDTH):
        POSITIONX += vel
    if keys[pygame.K_DOWN] and POSITIONY < (HEIGHT - CHARHEIGHT):
        POSITIONY += vel
    if keys[pygame.K_UP] and POSITIONY > 0:
        POSITIONY -= vel
    if keys[pygame.K_SPACE]:
        pass

    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, (POSITIONX, POSITIONY,
                                    CHARHEIGHT, CHARWIDTH) )
    pygame.display.update()




pygame.quit()