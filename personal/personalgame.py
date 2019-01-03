import pygame

pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Robert's Game")
red = (255, 0, 0)
black = (0, 0, 0)
gray60 = (153, 153, 153)
blue = (50, 109, 255)
collisioncount = 0

class rects():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumpcount = 10
        self.jumping = False
        self.running = True
        self.velocity = 5
        self.x2 = self.x + self.width
        self.y2 = self.y + self.height
        
        
    def create(self):
        pygame.draw.rect(
            window, red, (self.x, self.y, self.width, self.height))

    def create_ground(self):
        pygame.draw.rect(
            window, gray60, (self.x, self.y, self.width, self.height))

    def create_prize(self):
        pygame.draw.rect(
            window, blue, (self.x, self.y, self.width, self.height))




character = rects(50, 540, 40, 40)
square_one = rects(90, 440, 200, 20)
square_two = rects(380, 290, 70, 20)
square_three = rects(200, 150, 120, 20)
prize = rects(250, 0, 80, 40)
ground = rects(0, 580, 600, 20)


def draw():

    pygame.time.delay(40)
    window.fill(black)
    character.create()
    square_one.create()
    square_two.create()
    square_three.create()
    prize.create_prize()
    ground.create_ground()
    pygame.display.update()

# Main Game Loop
while character.running:
    #Quit Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            character.running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and character.x > 0:
        character.x -= character.velocity
    if keys[pygame.K_RIGHT] and character.x < 600 - character.width:
        character.x += character.velocity

    if not(character.jumping):

        if keys[pygame.K_DOWN] and character.y < 600 - character.height - ground.height:
            character.y += character.velocity
        if keys[pygame.K_UP] and character.y > 0:
            character.y -= character.velocity
        if keys[pygame.K_SPACE]:
            character.jumping = True
    # Jump loop        
    else:
        if character.jumpcount >= -10:
            neg = 1
            if character.jumpcount <= 0:
                neg = -1
            character.y -= (character.jumpcount ** 2) * 0.5 * neg
            character.jumpcount -= 1

        else:
            character.jumping = False
            character.jumpcount = 10
    #colission detection
    if square_one.x < character.x and character.x < square_one.x + square_one.width and character.y < square_one.y + square_one.height and character.y > square_one.y:
        collisioncount += 1
        print (f"Colission{collisioncount}")
    
        
    draw()

pygame.quit()
