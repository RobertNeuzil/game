import pygame, sys
pygame.init()
win = pygame.display.set_mode((500, 480))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

class player:
    def __init__(self):
        self.run = True
        self.width = 64
        self.height = 64
        self.x = 50
        self.y = 400
        self.vel = 5
        self.red = (255, 0, 0)
        self.black = (0, 0, 0)
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
man = player()


def reDrawGameWindow():
    win.blit(bg, (0,0))
    
    if man.walkCount + 1 >= 27:
        man.walkCount = 0
    if man.left:
        win.blit(walkLeft[man.walkCount // 3], (man.x, man.y))
        man.walkCount += 1
    if man.right:
        win.blit(walkRight[man.walkCount // 3], (man.x, man.y))
        man.walkCount += 1
    else:
        win.blit(char, (man.x, man.y))
    pygame.display.update()
    




walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), 
pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), 
pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')


while man.run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            man.run = False
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_RIGHT] and man.x < (500 - man.width):
        man.x += man.vel
        man.right = True
        man.left = False
    if keys[pygame.K_LEFT] and man.x > 0:
        man.x -= man.vel
        man.left = True
        man.right = False
    else:
        man.right = False
        man.left = False
        man.walkCount = 0
    
    if not(man.isJump):
        if keys[pygame.K_SPACE]:
            man.isJump = True
    else:
        if man.jumpCount >= -10:
            man.neg = 1
            if man.jumpCount < 0:
                man.neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * man.neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    reDrawGameWindow()


pygame.quit()
