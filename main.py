import pygame

pygame.init()

#Creating the Window screen
WIDTH, HEIGHT = 800, 600
Screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Invaders Game')
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

#Creating our player
class Player():

    def __init__(self, x, y, name, x_vel):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        Screen.blit(pygame.image.load(name),(x, y))
        self.loop()
    
    def move(self, dx):
        self.x += dx


    def loop(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move(-0.1)
                if event.key == pygame.K_RIGHT:
                    self.move(0.1)
                else:
                    self.move(0)
            pygame.display.update()



#Creating the game loop
run = True
while run:
    
    #Creating the event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    Screen.fill((0,0,0))

    player = Player(368, 500,'player1.png', 0)
    

    pygame.display.update()
pygame.quit()