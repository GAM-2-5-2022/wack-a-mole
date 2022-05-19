import pygame
import time

pygame.init()

screen = pygame.display.set_mode([900,1000])

running = True
while running:
    
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
     screen.fill((34,139,34))

     for i in range(2):
         for j in range(3):
             pygame.draw.circle(screen, (0,0,0), (300*j+150, 300*i + 200), 100)
    
             

     
     rect = surf.get_rect()

     pygame.display.flip()

pygame.quit
