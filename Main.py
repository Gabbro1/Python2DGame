import pygame, sys, time, random, colorsys, math







red = (250, 0, 0)



# class Player:
#     def __init__(self,vel,x,y):
#         self.vel = vel
#         self.vel_y = 16
#         self.x = x
#         self.y = y
#         self.jump = False

#     def move(self):
#         k = pygame.key.get_pressed()
#         if k[pygame.K_LEFT]:
#             self.x -= self.vel
#         if k[pygame.K_RIGHT]:
#             self.x += self.vel
#         if k[pygame.K_UP] and self.vel_y == 16:
#             self.jump = True
#         if self.jump:
#             pass
#             if self.vel_y >= -16:
#                 self.y -= self.vel_y
#                 self.vel_y -= 1
#             else:
#                 self.jump = False
#                 self.vel_y = 16

#     def draw(self):
#         pygame.draw.rect(screen,(255,255,255),(self.x,self.y,50,100))

#     def do(self):
#         self.move()
#         self.draw()



#Initialize the window
pygame.init()

#Create a screen
window = pygame.display.set_mode((800, 600))

pygame.display.set_caption("PLACEHOLDER")

#player
playerImg = pygame.image.load('images/playerProt.png')
playerPosX = 25
playerPosY = 550

def player(PosX, PosY):
    window.blit(playerImg, (PosX, PosY))
     


color = red

# Changing surface color
window.fill(color)
pygame.display.update()

running = True

#Game Loop
while running:

    window.fill((250, 250, 250))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False   
        if event.type==pygame.KEYDOWN and event.key== pygame.K_w:
            playerPosY -= 10
        if event.type==pygame.KEYDOWN and event.key== pygame.K_a:
            playerPosX -= 10
        if event.type==pygame.KEYDOWN and event.key== pygame.K_s:
            playerPosY += 10
        if event.type==pygame.KEYDOWN and event.key== pygame.K_d:
            playerPosX += 10   
       

    player(playerPosX, playerPosY)
    pygame.display.update()