import pygame, sys
from pygame.locals import *
import time

display_width = 1280
display_height = 720

pygame.init()
gameDisplay = pygame.display.set_mode((display_width,display_height), pygame.FULLSCREEN)
pygame.display.toggle_fullscreen
pygame.display.set_caption('Kimi no Mama')
gameIcon = pygame.image.load('images/images.png')
pygame.display.set_icon(gameIcon)

#colors in a tuple
black = (0, 0, 0)
transparent = (255, 255, 255, 100)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)

clock = pygame.time.Clock()

def button(pos_x, pos_y, image, action = None, text = None):
    mouse = pygame.mouse.get_pos()
    left_click, scroll, right_click = pygame.mouse.get_pressed()
    clicked = False
    button_width = 175 #This may vary based from playtests
    button_height = 50 #This may vary based from playtests
    buttonRect = pygame.draw.rect(gameDisplay,transparent, [pos_x,pos_y, button_width, button_height])

    if buttonRect.collidepoint(mouse):
        renderImage('hover' + image, pos_x, pos_y).coordinates()
        if left_click and action:
            action()

    else:
        renderImage(image, pos_x, pos_y).coordinates()

class renderImage:

    def __init__(self, filename, pos_x = 0, pos_y = 0, path = 'images/', extension = '.png'):
        global display_width
        global display_height
        self.display_width = display_width
        self.display_height = display_height
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.image = pygame.image.load(path+filename+extension)
        self.imageRect = self.image.get_rect()

    def center(self):
        self.imageRect.center = (self.display_width/2, self.display_height/2)
        gameDisplay.blit(self.image, self.imageRect)

    def midtop(self):
        self.imageRect.midtop = (self.display_width/2, self.pos_y)
        gameDisplay.blit(self.image, self.imageRect)

    def midleft(self):
        self.imageRect.midleft = (self.pos_x, self.display_height/2)
        gameDisplay.blit(self.image, self.imageRect)

    def coordinates(self):
        self.imageRect = self.imageRect.move((self.pos_x, self.pos_y))
        gameDisplay.blit(self.image, self.imageRect)

def display_text_passive(text, size, color, pos_x, pos_y):

    font = pygame.font.SysFont('Times New Roman', size)
    textSurface = font.render(text, True, color)
    textRect = textSurface.get_rect()
    textRect.topleft = (pos_x, pos_y)
    gameDisplay.blit(textSurface, textRect)
    pygame.display.update()

def display_text_active(text_list, size, color, pos_x, pos_y):

    string = ''
    left_click, scroll, right_click = pygame.mouse.get_pressed()
    font = pygame.font.SysFont('Times New Roman', size)
    line = 0
    for line in len(text_list):
        for character in line:
            string += text_list[i]
            textSurface = font.render(string, True, color)
            textRect = textSurface.get_rect()
            textRect.topleft = (pos_x, pos_y)
            gameDisplay.blit(textSurface, textRect)
            pygame.display.update()
            clock.tick(60)
            pygame.time.wait(40)
        display_text_passive(text_list, size, color, pos_x, pos_y)
        line += 1
'''
    while left_click and line != 3:
        print ('I did  something but yep')
        display_text_active(text_list, size, color, pos_x, pos_y)
'''

def start():

    gameDisplay.fill(white)
    renderImage('placeholder_bg1').center()
    game_done = False

    while not game_done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        renderImage('mom').center()

        button(100, 450, 'button1', screen1)
        button(500, 450, 'button2', screen2)
        button(100, 510, 'button3', screen3)
        button(500, 510, 'button4', screen4)

        pygame.display.update()

        clock.tick(60)

def screen1():

    gameDisplay.fill(white)
    renderImage('placeholder_green').center()
    game_done = False
    scene_done = False

    while not game_done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        renderImage('mom').center()
        renderImage('panel', 0, 440).midtop()

        button(150, 450, 'button1', screen1)
        button(550, 450, 'button2', screen2)
        button(150, 510, 'button3', screen3)
        button(550, 510, 'button4', screen4)

        #display_text_active('you and me in the moonlight', 45, white, 50, 50)
        
        pygame.display.update()

        clock.tick(60)

def screen2():

    gameDisplay.fill(white)
    renderImage('placeholder_red').center()
    game_done = False

    while not game_done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        renderImage('mom').center()

        button(100, 450, 'button1', screen1)
        button(500, 450, 'button2', screen2)
        button(100, 510, 'button3', screen3)
        button(500, 510, 'button4', screen4)

        pygame.display.update()
        clock.tick(60)

def screen3(): 

    gameDisplay.fill(white)
    game_done = False
    renderImage('placeholder_blue').center()
    while not game_done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        renderImage('mom').center()

        button(100, 450, 'button1', screen1)
        button(500, 450, 'button2', screen2)
        button(100, 510, 'button3', screen3)
        button(500, 510, 'button4', screen4)

        pygame.display.update()
        clock.tick(60)

def screen4():

    gameDisplay.fill(white)
    game_done = False
    renderImage('placeholder_purple').center()

    while not game_done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        renderImage('mom').center()

        button(100, 450, 'button1', screen1)
        button(500, 450, 'button2', screen2)
        button(100, 510, 'button3', screen3)
        button(500, 510, 'button4', screen4)
        pygame.display.update()
        clock.tick(60)

start()
pygame.quit()
quit()

def lulu(a, b):
    return a + b

class Add:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        return lulu(self.a, self.b)

class Another_Add:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        c = Add(self.a, self.b).addition()
        return c

some_variable = Add(3, 4).addition()
some_variables = Another_Add(3,3).addition()
print (some_variable)
print (some_variables)




'''

class Button:

    def __init__(self, filename, pos_x, pos_y, action = None, text = None, extension = '.png', path = 'images/', button_width = 175, button_height = 50):
        global transparent
        self.mouse_position = pygame.mouse.get_pos()
        self.left_click = pygame.mouse.get_pressed()[0]
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.button_width = button_width
        self.button_height = button_height
        self.buttonRect = pygame.draw.rect(gameDisplay, transparent, [self.pos_x, self.pos_y, self.button_width, self.button_height])
        self.imagename_passive = path + filename + extension
        self.imagename_active = path + 'hover' + filename + extension

    def action(self):
        if self.buttonRect.collidepoint(self.mouse_position):
            renderImage()
        else:
            renderImage()

largeText = pygame.font.Font('freesansbold.ttf', 115)
TextSurf, TextRect = text_objects('EYYY', largeText)
TextRect.center = ((width/2), height/2)
gameDisplay.blit(TextSurf, TextRect)

#pygame.draw.rect(gameDisplay, green, (150, 450, 100, 50))
#pygame.draw.rect(gameDisplay, red, (550, 450, 100, 50))
#gameDisplay.blit(image, (550, 450, 100, 50))

mouse = pygame.mouse.get_pos()
#print(mouse)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((width/2),(height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)
    #start()


see_through = pygame.Surface((100,100)).convert_alpha()
see_through.fill(BLU_HIGHLIGHT)
see_through_rect = see_through.get_rect(topleft = screen_rect.center)

import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((1200,750), pygame.FULLSCREEN)

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

textSurface = myfont.render('Some Text', False, (255,255,255))
gameDisplay.blit(textSurface, (20,30))

pygame.display.update()

    
    #smallText = pygame.font.SysFont("comicsansms",20)
    #textSurf, textRect = text_objects(text, smallText)
    #if centered use this, otherwise use pos_x + some small value

    #textRect.center = ((pos_x+(button_width/2)), (pos_y+(button_height/2))) 
    #gameDisplay.blit(textSurf, textRect)



'''
