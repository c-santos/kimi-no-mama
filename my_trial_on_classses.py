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

    def subtract(self):
        pass

some_variable = Add(3, 4).addition()
some_variablex = Add(3, 4).lul()
some_variables = Another_Add(3,3).addition()
print (some_variablex)
print (some_variables)

dictionary = {'Scene1': 'dark_background', 'Scene2': 'placeholder_bg1', 'Scene3': 'placeholder_green', 'Scene4': 'placeholder_red', 'Scene5': 'placeholder_blue', 'Scene6': 'placeholder_purple'}

a = dictionary.get('Scene4')
print (a)

'''
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
display_text_passive(text_list[line], size, color, pos_x, pos_y)
    
    if gameDisplay.get_rect().collidepoint(mouse_position):
        if left_click:
            line += 1
            display_text_active(text_list, line, size, color, pos_x, pos_y)
    else:
        pass


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

def screen2():

    gameDisplay.fill(white)
    renderImage('placeholder_red').center()
    game_done = False
    scene_done = False

    while not game_done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        renderImage('mom').center()

        if not scene_done:
            print(scene_done)
            displayText(['One, two, three, let\'s go', 'chouju wiro', 'narageul deut chumchureoga hey', 'oh let\'s dance the night away'], 0, 45, white, 100, 530).active()
            scene_done = True
        else:
            print(scene_done)
            displayText(['One, two, three, let\'s go', 'chouju wiro', 'narageul deut chumchureoga hey', 'oh let\'s dance the night away'], 0, 45, white, 100, 530).passive()
            scene_done = True

        button(100, 450, 'button1', screen1, 175, 50)
        button(500, 450, 'button2', screen2, 175, 50)
        button(100, 510, 'button3', screen3, 175, 50)
        button(500, 510, 'button4', screen4, 175, 50)

        pygame.display.update()
        clock.tick(60)

'''
#+20 life exp. Use this to buy a decent nervous system. Seriously though, you need a check-up
