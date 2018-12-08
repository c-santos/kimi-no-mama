def lulu(a, b):
    return a + b

class Add:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = self.a + self.b
    def addition(self):
        return lulu(self.a, self.b)
    def lul(self):
        return self.a + self.c

class Another_Add:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        c = Add(self.a, self.b).addition()
        return c

some_variable = Add(3, 4).addition()
some_variablex = Add(3, 4).lul()
some_variables = Another_Add(3,3).addition()
print (some_variablex)
print (some_variables)

dictionary = {'Scene1': 'dark_background', 'Scene2': 'placeholder_bg1', 'Scene3': 'placeholder_green', 'Scene4': 'placeholder_red', 'Scene5': 'placeholder_blue', 'Scene6': 'placeholder_purple'}

a = dictionary.get('Scene4')
print (a)

import pygame, sys
from pygame.locals import *
 
pygame.init()
 
pygame.display.set_caption('font example')
size = [640, 480]
screen = pygame.display.set_mode(size)
 
clock = pygame.time.Clock()
 
basicfont = pygame.font.SysFont(None, 48)
text = basicfont.render('Hello World!', True, (255, 0, 0), (255, 255, 255))
textrect = text.get_rect()
textrect.centerx = screen.get_rect().centerx
textrect.centery = screen.get_rect().centery
 
screen.fill((255, 255, 255))
screen.blit(text, textrect)
 
pygame.display.update()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
    clock.tick(20)

