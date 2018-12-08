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

#a dictionary of scenes and their background
scenery = {'Scene1': 'dark_background', 'Scene2': 'placeholder_bg1', 'Scene3': 'placeholder_green', 'Scene4': 'placeholder_red', 'Scene5': 'placeholder_blue', 'Scene6': 'placeholder_purple'}
character = {'Scene1': 'mom', 'Scene2': 'mom', 'Scene3': 'mom', 'Scene4': 'mom', 'Scene5': 'mom', 'Scene6': 'mom'}
dialogue = {'Scene1': ['you and me in the moonlight', 'byeol kkot chukje yeollin bam', 'pado sorireul teulgo', 'chumeul chuneon ni sungan', 'i neukkim jeongmal ttagya'], 'Scene2': ['badaya uriwa gachi nora', 'barama neodo ijjogeuro wa'], 'Scene3': ['dalppit jomyeong araeseo', 'neowa nawa sesanggwa', 'da gachi Party all night long', 'Yeah, it’s good'], 'Scene4': ['If you wanna have some fun', 'jjapjjalhan gonggicheoreom', 'i sungane teukbyeolhan', 'haengbogeul notchiji ma'], 'Scene5': ['One, two, three, let\'s go', 'chouju wiro', 'narageul deut chumchureoga hey', 'oh let\'s dance the night away'], 'Scene6': ['Let’s dance the night away', 'One, two, three, let’s go', 'jeo bada geonneo', 'deullil deut sori jilleo', 'Let’s dance the night away']}
nexts = {'Scene1': 'Scene2', 'Scene2': 'Scene3', 'Scene3': 'Scene4', 'Scene4': 'Scene5', 'Scene5': 'Scene6', 'Scene6': 'Scene1'}

#colors in a tuple
black = (0, 0, 0)
transparent = (255, 255, 255, 100)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)

clock = pygame.time.Clock()

def button(pos_x, pos_y, image, action = None, button_width = 48, button_height = 48): #parameters: pos_x, pos_y, image, action = None, button_width = 48, button_height = 48

	mouse_position = pygame.mouse.get_pos()
	left_click, scroll, right_click = pygame.mouse.get_pressed()
	buttonRect = pygame.draw.rect(gameDisplay,transparent, [pos_x,pos_y, button_width, button_height])

	if buttonRect.collidepoint(mouse_position):
		renderImage('hover' + image, pos_x, pos_y).coordinates()
		if left_click and action:
			renderImage(image, pos_x, pos_y).coordinates()
			action()

	else:
		renderImage(image, pos_x, pos_y).coordinates()

def string_to_callable(string):

	callables = {'passiveScene':passiveScene}
	callable_name = callables.get(string)
	return callable_name

class renderImage: #parameters: self, filename, pos_x = 0, pos_y = 0, path = 'images/', extension = '.png'

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

class displayText: #parameters: self, text_list, line = 0, size = 40, color = white, pos_x = 0, pos_y = 0, font = 'Comics Sans MS'

	def __init__(self, text_list, line = 0, size = 40, color = white, pos_x = 0, pos_y = 0, font = 'Comics Sans MS'):

		self.text_list = text_list
		self.line = line
		self.font = font
		self.size = size
		self.color = color
		self.pos_x = pos_x
		self.pos_y = pos_y

	def passive(self):

		fontography = pygame.font.SysFont(self.font, self.size)
		textSurface = fontography.render(self.text_list[self.line], True, self.color)
		textRect = textSurface.get_rect()
		textRect.topleft = (self.pos_x, self.pos_y)
		gameDisplay.blit(textSurface, textRect)
		pygame.display.update()

	def active(self):

		string = ''
		fontography = pygame.font.SysFont(self.font, self.size)
		for character in self.text_list[self.line]:
			string += character
			textSurface = fontography.render(string, True, self.color)
			textRect = textSurface.get_rect()
			textRect.topleft = (self.pos_x, self.pos_y)
			gameDisplay.blit(textSurface, textRect)
			pygame.display.update()
			clock.tick(60)
			pygame.time.wait(40)

class passiveScene: #self, scene_name, next_scene = None, next_type = None

	def __init__(self, scene_name, next_type = 'passiveScene'):

		global scenery
		global character
		global dialogue
		global nexts
		self.game_quit = False
		self.scene_done = False
		self.line = 0
		self.scene_name = scene_name
		self.text_list = dialogue.get(self.scene_name)
		self.next_scene = nexts.get(self.scene_name)
		self.next_type = next_type
		gameDisplay.fill(black)
		renderImage(scenery.get(self.scene_name)).center()
		renderImage(character.get(self.scene_name), 0, 100).midtop()

	def execute(self):

		while not self.game_quit:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						renderImage(scenery.get(self.scene_name)).center()
						renderImage(character.get(self.scene_name), 0, 100).midtop()
						self.line += 1
						if self.line == len(self.text_list):
							string_to_callable(self.next_type)(self.next_scene).execute()
						self.scene_done = False
			if not self.scene_done:
				displayText(self.text_list, self.line, 45, black, 300, 360).active()
				self.scene_done = True
				continue
			else:
				displayText(self.text_list, self.line, 45, black, 300, 360).passive()
				self.scene_done = True
				continue

passiveScene('Scene1').execute()

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

		button(100, 450, 'button1', screen1, 175, 50)
		button(500, 450, 'button2', screen2, 175, 50)
		button(100, 510, 'button3', screen3, 175, 50)
		button(500, 510, 'button4', screen4, 175, 50)
		pygame.display.update()

		clock.tick(60)

def screen1():

	gameDisplay.fill(white)
	renderImage('placeholder_green').center()
	game_done = False

	while not game_done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		renderImage('mom').center()
		renderImage('panel', 0, 440).midtop()

		button(100, 510, 'button_blue', screen1)
		button(100, 570, 'button_green', screen2)
		button(100, 630, 'button_orange', screen3)
				
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

		button(100, 450, 'button1', screen1, 175, 50)
		button(500, 450, 'button2', screen2, 175, 50)
		button(100, 510, 'button3', screen3, 175, 50)
		button(500, 510, 'button4', screen4, 175, 50)

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

		button(100, 450, 'button1', screen1, 175, 50)
		button(500, 450, 'button2', screen2, 175, 50)
		button(100, 510, 'button3', screen3, 175, 50)
		button(500, 510, 'button4', screen4, 175, 50)
		pygame.display.update()
		clock.tick(60)

start()
pygame.quit()
quit()

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



'''
