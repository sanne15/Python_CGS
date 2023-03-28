#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pygame

# initialize
pygame.init()
screen_width, screen_height = 320, 320
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Drawing shapes")

# draw shapes
def drawShapes():
    screen.fill(pygame.Color('white'))
    pygame.draw.rect(screen, pygame.Color('black'), ((100, 100), (200, 200)))
    pygame.draw.lines(screen, pygame.Color('blue'), True, ((80, 80), (240, 80), (240, 240)), 3)
    pygame.draw.circle(screen, pygame.Color('purple'), (60, 60), 40)
    
# Run until the user asks to quit
running = True
while running:
    # Main Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If user clicked close button
            running = False
        
    drawShapes() # draw
    
    # Update the screen
    pygame.display.flip()

pygame.quit()

