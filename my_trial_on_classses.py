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
'''
buttons = ('button_blue', 'button_green', 'button_orange')
scenery = {'Scene1': 'dark_background', 'Scene2': 'placeholder_bg1', 'Scene3': 'placeholder_green', 'Scene4': 'placeholder_red', 'Scene5': 'placeholder_blue', 'Scene6': 'placeholder_purple', 'dScene1': 'placeholder_red','dScene2': 'placeholder_purple', 'dScene3': 'placeholder_green', 'dScene4': 'dark_background'}
character = {'Scene1': 'mom-angry', 'Scene2': 'mom-happy', 'Scene3': 'mom-oface', 'Scene4': 'mom-solo', 'Scene5': 'mom-soloangry', 'Scene6': 'mom-solofinger', 'dScene1': 'mom-angry', 'dScene2': 'mom-happy', 'dScene3': 'mom-oface', 'dScene4': 'mom-solo'}
scene_types = {'Scene1': 'passiveScene', 'Scene2': 'passiveScene', 'Scene3': 'passiveScene', 'Scene4': 'passiveScene', 'Scene5': 'passiveScene', 'Scene6': 'passiveScene', 'dScene1': 'activeScene','dScene2': 'activeScene', 'dScene3': 'activeScene', 'dScene4': 'activeScene'}
dialogue = {'Scene1': [('', '*awesome intro*'), ('Nayeon', 'you and me in the moonlight'), ('Nayeon', 'byeol kkot chukje yeollin bam'), ('Sana','pado sorireul teulgo'), ('Sana', 'chumeul chuneon ni sungan'), ('Sana', 'i neukkim jeongmal ttagya')], 'Scene2': [('Momo', 'badaya uriwa gachi nora'), ('Momo', 'barama neodo ijjogeuro wa')], 'Scene3': [('Jeongyeon', 'dalppit jomyeong araeseo'), ('Jeongyeon', 'neowa nawa sesanggwa'), ('Jeongyeon', 'da gachi Party all night long'), ('Jeongyeon', 'Yeah, it’s good')], 'Scene4': [('Tzuyu', 'If you wanna have some fun'), ('Tzuyu', 'jjapjjalhan gonggicheoreom'), ('Tzuyu', 'i sungane teukbyeolhan'), ('Tzuyu',  'haengbogeul notchiji ma')], 'Scene5': [('Mina', 'One, two, three, let\'s go'), ('Mina', 'chouju wiro'), ('Chaeyoung', 'narageul deut chumchureoga hey'), ('Chaeyoung', 'let\'s dance the night away')], 'Scene6': [('', '*music intensifies*'), ('Chaeyoung', 'Let’s dance the night away'), ('Jihyo', 'One, two, three, let’s go'), ('Jihyo', 'jeo bada geonneo'), ('Jihyo', 'deullil deut sori jilleo'), ('Jihyo', 'Let’s dance the night away')]}
nexts = {'Scene1': 'dScene2', 'Scene2': 'Scene3', 'Scene3': 'Scene4', 'Scene4': 'Scene5', 'Scene5': 'Scene6', 'Scene6': 'Scene1'}
choice_texts = {'dScene1': ('Yes', 'or', 'Yes'), 'dScene2': ('Yes', 'or', 'Yes'), 'dScene3': ('Yes', 'or', 'Yes'), 'dScene4': ('Yes', 'or', 'Yes'), 'dScene5': ('Yes', 'or', 'Yes'), 'dScene6': ('Yes', 'or', 'Yes')}
outcome_texts = {'dScene1': (('What', 'is', 'Love?'), ('jjirit', 'jjirit', 'jjirit', 'jjirit'), ('You\'re', 'my', 'heartshaker shaker')), 'dScene2': (('What', 'is', 'Love?'), ('jjirit', 'jjirit', 'jjirit', 'jjirit'), ('You\'re', 'my', 'heartshaker shaker')), 'dScene3': (('What', 'is', 'Love?'), ('jjirit', 'jjirit', 'jjirit', 'jjirit'), ('You\'re', 'my', 'heartshaker shaker')), 'dScene4': (('What', 'is', 'Love?'), ('jjirit', 'jjirit', 'jjirit', 'jjirit'), ('You\'re', 'my', 'heartshaker shaker'))}
outcome_actions = {'dScene1': ('dScene4', 'Scene2', 'dScene3'), 'dScene2': ('dScene1', 'dScene4', 'dScene3'), 'dScene3': ('dScene1', 'dScene2', 'dScene4'), 'dScene4': ('dScene3', 'dScene2', 'dScene1')}
oddities = {}




'''
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

def buttons(pos_x, pos_y, image, action = None, image_type = 'button/', button_width = 48, button_height = 48): #parameters: pos_x, pos_y, image, image_type = 'button/', action = None, button_width = 48, button_height = 48
    global scene_types

    mouse_position = pygame.mouse.get_pos()
    left_click, scroll, right_click = pygame.mouse.get_pressed()
    buttonRect = pygame.draw.rect(gameDisplay,transparent, [pos_x,pos_y, button_width, button_height])

    if buttonRect.collidepoint(mouse_position):
        renderImage('hover' + image, image_type, pos_x, pos_y).coordinates()
        if left_click and action:
            renderImage(image, pos_x, pos_y, image_type).coordinates()
            string_to_callable(scene_types.get(action))(action).execute()

    else:
        renderImage(image, pos_x, pos_y).coordinates()

def string_to_callable(string): #parameters: string
    pass
def button(pos_x, pos_y, image, action = None, image_type = 'buttons/', button_width = 48, button_height = 48): #parameters: pos_x, pos_y, image, image_type = 'button/', action = None, button_width = 48, button_height = 48
    pass
class renderImage: #filename, image_type = '', pos_x = 0, pos_y = 0, path = 'images/', extension = '.png'
    pass
class displayText: #parameters: text_list, line = 0, size = 45, color = white, pos_x = 0, pos_y = 0, font = None
    pass
class passiveScene: #scene_name, next_type = 'passiveScene'

    def __init__(self, scene_name):

        global scenery
        global character
        global dialogue
        global nexts
        global panel_pos_y
        global scene_types
        self.game_quit = False
        self.scene_done = False
        self.line = 0
        self.scene_name = scene_name
        self.next_scene = nexts.get(self.scene_name)
        self.background = scenery.get(self.scene_name)
        self.speaker = character.get(self.scene_name)
        self.next_type = string_to_callable(scene_types.get(self.next_scene))
        self.speaker_pos_x = 135
        self.speaker_pos_y = 518
        self.text_pos_x = 200
        self.char_pos_x = 500
        self.char_pos_y = 150
        self.panel_pos_y = panel_pos_y
        self.dialog_text_size = 37
        self.speaker_text_size = 35
        self.color = white
        gameDisplay.fill(self.color)
        renderImage(self.background, 'scenery/').center()
        renderImage(self.speaker, 'character/', self.char_pos_x, self.char_pos_y).coordinates()
        renderImage('panel', '', 0, self.panel_pos_y).midtop()


    def execute(self):

        while not self.game_quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        renderImage(self.background, 'scenery/').center()
                        renderImage(self.speaker, 'character/', 0, self.char_pos_y).midtop()
                        renderImage('panel', '', 0, self.panel_pos_y).midtop()
                        self.line += 1
                        if self.line == len(dialogue.get(self.scene_name)):
                            self.next_type(self.next_scene).execute()
                        self.scene_done = False
            self.speaker_name, self.text_list = dialogue.get(self.scene_name)[self.line]
            if not self.scene_done:
                displayText(self.speaker_name, 0, self.speaker_text_size, self.color, self.speaker_pos_x, self.speaker_pos_y).passive()
                displayText(self.text_list, self.line, self.dialog_text_size, self.color, self.text_pos_x, 0).active_panel()
                self.scene_done = True
                continue
            else:
                renderImage(self.background, 'scenery/').center()
                renderImage(self.speaker, 'character/', 0, self.char_pos_y).midtop()
                renderImage('panel', '', 0, self.panel_pos_y).midtop()
                displayText(self.speaker_name, 0, self.speaker_text_size, self.color, self.speaker_pos_x, self.speaker_pos_y).passive()
                displayText(self.text_list, self.line, self.dialog_text_size, self.color, self.text_pos_x, 0).passive_panel()

                self.scene_done = True
                continue

            clock.tick(60)

def text_ani(str, tuple):
    x, y = tuple
    y = y*line_space ##shift text down by one line
    char = ''        ##new string that will take text one char at a time. Not the best variable name I know.
    letter = 0
    count = 0
    for i in range(len(str)):
        pygame.event.clear() ## this is very important if your event queue is not handled properly elsewhere. Alternativly pygame.event.pump() would work.
        time.sleep(0.05) ##change this for faster or slower text animation
        char = char + str[letter]
        text = basicfont.render(char, False, (2, 241, 16), (0, 0, 0)) #First tuple is text color, second tuple is background color
        textrect = text.get_rect(topleft=(x, y)) ## x, y's provided in function call. y coordinate amended by line height where needed
        screen.blit(text, textrect)
        pygame.display.update(textrect) ## update only the text just added without removing previous lines.
        count += 1
        letter += 1
        print (char) ## for debugging in console, comment out or delete.


text_ani('this is line number 1 ', (0, 1)) # text string and x, y coordinate tuple.
text_ani('this is line number 2', (0, 2))
text_ani('this is line number 3', (0, 3))
text_ani('', (0, 3)) # this is a blank line