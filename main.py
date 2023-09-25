import pygame
pygame.init()

#Creating the Window screen
WIDTH, HEIGHT = 800, 600
Screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Invaders Game')
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

#Creating the game loop
run = True
while run:
    
    #Creating the event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
pygame.quit()