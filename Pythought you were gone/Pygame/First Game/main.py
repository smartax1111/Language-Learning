# icons used from flaticon.com

import pygame


# init
pygame.init()

# window
screen = pygame.display.set_mode((800, 600))


# Title and Icon
pygame.display.set_caption("Space Encroachers")
icon = pygame.image.load('C:/Users/TJ/Desktop/GitHub/Language-Learning/Pythought you were gone/Pygame/First Game/ufo.png')
pygame.display.set_icon(icon)
# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    pygame.display.update()