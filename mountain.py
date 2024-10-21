import pygame
from pygame.draw import *
from random import randint


pygame.init()

FPS = 30
screen = pygame.display.set_mode((950, 900))
color = (200, 40, 50)

# drawing objects
def draw_sky(surface, x, y, width, height):
    """
    Draws a sky on the screen.
  surface - pygame.Surface object, on which to draw
  x, y - upper left hand corner coords 
  width, height - sizes of the drawn object
  color -  pygame.Color code of the drawn object
    """
    
    color = (235,185,100) #более песочный
    rect(surface, color, (x, y, width, height // 3))
    rect(surface, color, (x, y + 2 * (height // 3), width, height // 3))
    color = (250,128,114) #персиковый
    rect(surface, color, (x, y + (height // 3), width, height // 3))


def draw_sun(surface, x, y, size):
    """
    Draws a sun on the screen.
  surface - pygame.Surface object, on which to draw
  x, y - upper left hand corner coords 
  width, height - sizes of the drawn object
  color -  pygame.Color code of the drawn object
    """
    color = (250, 250, 0)
    circle(surface, color, (x, y), size)


def draw_back_mountain(surface):
    """
    Draws a back mountain on the screen.
  surface - pygame.Surface object, on which to draw
  x, y - upper left hand corner coords 
  width, height - sizes of the drawn object
  color -  pygame.Color code of the drawn object
    """
    
    color = (178,34,30)
    polygon(surface, color, [[100, 400], [25, 270], [-10, 400]])
    polygon(surface, color, [[200, 400], [100, 210], [10, 400]])
    polygon(surface, color, [[500, 400], [200, 300], [110, 400]])
    polygon(surface, color, [[700, 400], [400, 180], [310, 400]])
    polygon(surface, color, [[800, 400], [520, 230], [290, 400]])
    polygon(surface, color, [[900, 400], [670, 100], [610, 400]])
    polygon(surface, color, [[1000, 400], [800, 200], [710, 400]])


def draw_forward_mountain(surface):
    """
    Draws a forward mountain on the screen.
  surface - pygame.Surface object, on which to draw
  x, y - upper left hand corner coords 
  width, height - sizes of the drawn object
  color -  pygame.Color code of the drawn object
    """
    color = (255,140,0)
    hight = 560
    h = 130
    polygon(surface, color, [[100, hight], [25 + randint(-20, 20), 270 + h  + randint(-20, 20)], [-10, hight]])
    polygon(surface, color, [[200, hight], [100 + randint(-20, 20), 210 + h  + randint(-20, 20)], [10, hight]])
    polygon(surface, color, [[500, hight], [200 + randint(-20, 20), 300 + h  + randint(-20, 20)], [110, hight]])
    polygon(surface, color, [[700, hight], [400 + randint(-20, 20), 180 + h  + randint(-20, 20)], [310, hight]])
    polygon(surface, color, [[800, hight], [520 + randint(-20, 20), 230 + h  + randint(-20, 20)], [290, hight]])
    polygon(surface, color, [[900, hight], [670 + randint(-20, 20), 100 + h  + randint(-20, 20)], [610, hight]])
    polygon(surface, color, [[1000,hight], [800 + randint(-20, 20), 200 + h  + randint(-20, 20)], [710, hight]])


def draw_earth(surface):
    """
    Draws an earth on the screen.
  surface - pygame.Surface object, on which to draw
  x, y - upper left hand corner coords 
  width, height - sizes of the drawn object
  color -  pygame.Color code of the drawn object
    """
    color = (221,180,221)
    hight = 200
    rect(surface, color, (0, 500, 950, hight))




def draw_peyzag(surface, x, y, width, height):
    """
    Draws a peyzag on the screen.
    surface - pygame.Surface object, on which to draw
    x, y - upper left hand corner coords 
    width, height - sizes of the drawn object
    color -  pygame.Color code of the drawn object
    """
    sky_x = 0
    sky_y = 0
    draw_sky(surface, sky_x, sky_y, width, height)

    size = height
    sun_x = 160
    sun_y = 160
    draw_sun(surface, sun_x, sun_y, size // 7)

    draw_back_mountain(surface)

    draw_forward_mountain(surface)

    draw_earth(surface)



draw_peyzag(screen, 150, 150, 1000, 700)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()