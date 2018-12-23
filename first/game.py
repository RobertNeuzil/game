import pygame, sys
pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My Game")

run = True
width = 30
height = 40
x = 50
y = 450
vel = 5
red = (255, 0, 0)
black = (0, 0, 0)

isJump = False
jumpCount = 10

while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and x < (500 - width):
        x += vel
    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    
    if not(isJump):
        if keys[pygame.K_UP] and y > 0:
            y -= vel
        if keys[pygame.K_DOWN] and y < (500 - height):
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1

            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10




    pygame.draw.rect(win, red, (x, y, width, height))
    pygame.display.update()
    win.fill(black)

pygame.quit()
