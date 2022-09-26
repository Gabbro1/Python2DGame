import pygame

white = (250, 250, 250)
black = (0, 0, 0)
red = (250, 0, 0)

#Initialize the window
pygame.init()

#Create a screen
window = pygame.display.set_mode((800, 600))

pygame.display.set_caption("PLACEHOLDER")

color = red
  
# Changing surface color
window.fill(color)
pygame.display.flip()

running = True

#Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False          