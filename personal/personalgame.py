import pygame

pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Robert's Game")
red = (255, 0, 0)
black = (0, 0, 0)
gray60 = (153, 153, 153)
blue = (50, 109, 255)
lime = (0,255,0)
collisioncount = 0


class rects(pygame.Rect):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x2 = x + width
        self.y2 = y + height
        self.jumpcount = 10
        self.jumping = False
        self.running = True
        self.velocity = 5

    def create_character(self):
        pygame.draw.rect(window, lime, (self.x, self.y, self.width, self.height))

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
square_one = rects(90, 440, 15, 30)
square_two = rects(120, 290, 15, 30)
square_three = rects(150, 150, 15, 30)
prize = rects(250, 0, 80, 40)
ground = rects(0, 580, 600, 20)


def draw():

    pygame.time.delay(40)
    window.fill(black)
    character.create_character()
    square_one.create()
    square_two.create()
    square_three.create()
    prize.create_prize()
    ground.create_ground()
    pygame.display.update()


# Main Game Loop
while character.running:
    # Quit Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            character.running = False

    keys = pygame.key.get_pressed()


    if keys[pygame.K_LEFT] and character.x > 0 or keys[pygame.K_a] and character.x > 0:
        if character.top == square_one.bottom:
            character.velocity == 0
        else:
            character.x -= character.velocity
            character.x2 -= character.velocity
    if keys[pygame.K_RIGHT] and character.x < 600 or keys[pygame.K_d] and character.x < 600 - character.width:
    
            character.x += character.velocity
            character.x2 += character.velocity
    if not(character.jumping):

        if keys[pygame.K_DOWN] and character.y < 600 or keys[pygame.K_s] and character.y < 600 - character.height - ground.height:
        
                character.y += character.velocity
                character.y2 += character.velocity
        if keys[pygame.K_UP] and character.y > 0 or keys[pygame.K_w] and character.y > 0:
        
                character.y -= character.velocity
                character.y2 -= character.velocity
        if keys[pygame.K_SPACE]:
        
                character.jumping = True
    # Jump loop
    else:
        if character.jumpcount >= -10:
            neg = 1
            if character.jumpcount <= 0:
                neg = -1
            character.y -= (character.jumpcount ** 2) * 0.5 * neg
            character.y2 -= (character.jumpcount ** 2) * 0.5 * neg
            character.jumpcount -= 1

        else:
            character.jumping = False
            character.jumpcount = 10

    # Collision logic

    if character.x2 > square_one.x and character.x < square_one.x2:
        if character.y in range(square_one.y, square_one.y2):

            print('bottomx1')

    if character.x2 > square_one.x and character.x < square_one.x2:
        if character.y2 in range(square_one.y, square_one.y2):
            print('topx1')
    if character.y2 > square_one.y and character.y < square_one.y2:
        if character.x in range(square_one.x, square_one.x2):
            print('rightx1')
    if character.y2 > square_one.y and character.y < square_one.y2:
        if character.x2 in range(square_one.x, square_one.x2):
            print('leftx1')

    if character.x2 > square_two.x and character.x < square_two.x2:
        if character.y in range(square_two.y, square_two.y2):
            print('bottomx2')
    if character.x2 > square_two.x and character.x < square_two.x2:
        if character.y2 in range(square_two.y, square_two.y2):
            print('topx2')
    if character.y2 > square_two.y and character.y < square_two.y2:
        if character.x in range(square_two.x, square_two.x2):
            print('rightx1')
    if character.y2 > square_two.y and character.y < square_two.y2:
        if character.x2 in range(square_two.x, square_two.x2):
            print('leftx1')

    if character.x2 > square_three.x and character.x < square_three.x2:
        if character.y in range(square_three.y, square_three.y2):
            print('bottomx2')
    if character.x2 > square_three.x and character.x < square_three.x2:
        if character.y2 in range(square_three.y, square_three.y2):
            print('topx2')
    if character.y2 > square_three.y and character.y < square_three.y2:
        if character.x in range(square_three.x, square_three.x2):
            print('rightx1')
    if character.y2 > square_three.y and character.y < square_three.y2:
        if character.x2 in range(square_three.x, square_three.x2):
            print('leftx1')

    if character.x2 > prize.x and character.x < prize.x2:
        if character.y in range(prize.y, prize.y2):
            print('top')
    if character.x2 > prize.x and character.x < prize.x2:
        if character.y2 in range(prize.y, prize.y2):
            print('bottom')
    if character.y2 > prize.y and character.y < prize.y2:
        if character.x in range(prize.x, prize.x2):
            print('left')
    if character.y2 > prize.y and character.y < prize.y2:
        if character.x2 in range(prize.x, prize.x2):
            print('right')

    draw()


pygame.quit()
