import pygame, sys
from pygame.locals import *
import time

display_width = 1280
display_height = 720

pygame.init()
gameDisplay = pygame.display.set_mode((display_width,display_height), pygame.FULLSCREEN)
pygame.display.toggle_fullscreen
pygame.display.set_caption('Kimi no Mama')
gameIcon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(gameIcon)

#a dictionary of scenes and their background
scenery = {'Scene1': 'dark_background', 'Scene2': 'placeholder_bg1', 'Scene3': 'placeholder_green', 'Scene4': 'placeholder_red', 'Scene5': 'placeholder_blue', 'Scene6': 'placeholder_purple'}
character = {'Scene1': 'mom-angry', 'Scene2': 'mom-happy', 'Scene3': 'mom-oface', 'Scene4': 'mom-solo', 'Scene5': 'mom-soloangry', 'Scene6': 'mom-solofinger'}
dialogue = {'Scene1': [('Nayeon', 'you and me in the moonlight'), ('Nayeon', 'byeol kkot chukje yeollin bam'), ('Sana','pado sorireul teulgo'), ('Sana', 'chumeul chuneon ni sungan'), ('Sana', 'i neukkim jeongmal ttagya')], 'Scene2': [('Momo', 'badaya uriwa gachi nora'), ('Momo', 'barama neodo ijjogeuro wa')], 'Scene3': [('Jeongyeon', 'dalppit jomyeong araeseo'), ('Jeongyeon', 'neowa nawa sesanggwa'), ('Jeongyeon', 'da gachi Party all night long'), ('Jeongyeon', 'Yeah, it’s good')], 'Scene4': [('Tzuyu', 'If you wanna have some fun'), ('Tzuyu', 'jjapjjalhan gonggicheoreom'), ('Tzuyu', 'i sungane teukbyeolhan'), ('Tzuyu',  'haengbogeul notchiji ma')], 'Scene5': [('Mina', 'One, two, three, let\'s go'), ('Mina', 'chouju wiro'), ('Chaeyoung', 'narageul deut chumchureoga hey'), ('Chaeyoung', 'oh let\'s dance the night away')], 'Scene6': [('Chaeyoung', 'Let’s dance the night away'), ('Jihyo', 'One, two, three, let’s go'), ('Jihyo', 'jeo bada geonneo'), ('Jihyo', 'deullil deut sori jilleo'), ('Jihyo', 'Let’s dance the night away')]}
nexts = {'Scene1': 'Scene2', 'Scene2': 'Scene3', 'Scene3': 'Scene4', 'Scene4': 'Scene5', 'Scene5': 'Scene6', 'Scene6': 'Scene1'}

#colors in a tuple
black = (0, 0, 0)
transparent = (255, 255, 255, 100)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)

clock = pygame.time.Clock()

#some_variables
panel_height = 138
panel_pos_y = 490
panel_offset = display_height - (panel_pos_y + 200)

def string_to_callable(string): #parameters: string

	callables = {'passiveScene':passiveScene}
	callable_name = callables.get(string)
	return callable_name

def button(pos_x, pos_y, image, image_type = 'button/', action = None, button_width = 48, button_height = 48): #parameters: pos_x, pos_y, image, image_type = 'button/', action = None, button_width = 48, button_height = 48

	mouse_position = pygame.mouse.get_pos()
	left_click, scroll, right_click = pygame.mouse.get_pressed()
	buttonRect = pygame.draw.rect(gameDisplay,transparent, [pos_x,pos_y, button_width, button_height])

	if buttonRect.collidepoint(mouse_position):
		renderImage('hover' + image, image_type, pos_x, pos_y).coordinates()
		if left_click and action:
			renderImage(image, pos_x, pos_y, image_type).coordinates()
			action()

	else:
		renderImage(image, pos_x, pos_y).coordinates()

class renderImage: #filename, image_type = '', pos_x = 0, pos_y = 0, path = 'images/', extension = '.png'

	def __init__(self, filename, image_type = '', pos_x = 0, pos_y = 0, path = 'assets/', extension = '.png'):
		global display_width
		global display_height
		self.display_width = display_width
		self.display_height = display_height
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.image = pygame.image.load(path+image_type+filename+extension)
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

class displayText: #parameters: text_list, line = 0, size = 45, color = white, pos_x = 0, pos_y = 0, font = None

	def __init__(self, text_list, line = 0, size = 45, color = white, pos_x = 0, pos_y = 0, font = 'assets/DeJavuSans.ttf'):
		global display_height
		global panel_offset
		global panel_height
		self.text_list = text_list
		self.line = line
		self.font = font
		self.size = size
		self.color = color
		self.pos_x = pos_x
		self.pos_y = display_height - (panel_offset + panel_height/2)
		self.pos_y_speaker = pos_y

	def passive_panel(self):

		fontography = pygame.font.Font(self.font, self.size)
		textSurface = fontography.render(self.text_list[self.line], True, self.color)
		textRect = textSurface.get_rect()
		textRect.midleft = (self.pos_x, self.pos_y)
		gameDisplay.blit(textSurface, textRect)
		pygame.display.update()

	def active_panel(self):

		string = ''
		fontography = pygame.font.Font(self.font, self.size)
		for character in self.text_list:
			string += character
			textSurface = fontography.render(string, True, self.color)
			textRect = textSurface.get_rect()
			textRect.midleft = (self.pos_x, self.pos_y)
			gameDisplay.blit(textSurface, textRect)
			pygame.display.update()
			clock.tick(60)
			pygame.time.wait(40)

	def passive(self):

		fontography = pygame.font.Font(self.font, self.size)
		textSurface = fontography.render(self.text_list, True, self.color)
		textRect = textSurface.get_rect()
		textRect.topleft = (self.pos_x, self.pos_y_speaker)
		gameDisplay.blit(textSurface, textRect)
		pygame.display.update()

class passiveScene: #scene_name, next_scene = None, next_type = 'passiveScene'

	def __init__(self, scene_name, next_type = 'passiveScene'):

		global scenery
		global character
		global dialogue
		global nexts
		global panel_pos_y
		self.game_quit = False
		self.scene_done = False
		self.line = 0
		self.scene_name = scene_name
		#self.speaker_name, self.text_list = dialogue.get(self.scene_name)[self.line]
		self.next_scene = nexts.get(self.scene_name)
		self.next_type = next_type
		self.speaker_pos_x = 135
		self.speaker_pos_y = 518
		self.text_pos_x = 200
		self.char_pos_y = 150
		self.panel_pos_y = panel_pos_y
		self.dialog_text_size = 37
		self.speaker_text_size = 35
		self.color = white
		gameDisplay.fill(self.color)
		renderImage(scenery.get(self.scene_name), 'scenery/').center()
		renderImage(character.get(self.scene_name), 'character/', 0, self.char_pos_y).midtop()
		renderImage('panel', '', 0, self.panel_pos_y).midtop()

	def execute(self):

		while not self.game_quit:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						renderImage(scenery.get(self.scene_name), 'scenery/').center()
						renderImage(character.get(self.scene_name), 'character/', 0, self.char_pos_y).midtop()
						renderImage('panel', '', 0, self.panel_pos_y).midtop()
						self.line += 1
						if self.line == len(dialogue.get(self.scene_name)):
							string_to_callable(self.next_type)(self.next_scene).execute()
						self.scene_done = False
			self.speaker_name, self.text_list = dialogue.get(self.scene_name)[self.line]
			if not self.scene_done:
				displayText(self.speaker_name, 0, self.speaker_text_size, self.color, self.speaker_pos_x, self.speaker_pos_y).passive()
				displayText(self.text_list, self.line, self.dialog_text_size, self.color, self.text_pos_x, 0).active_panel()
				self.scene_done = True
				continue
			else:
				#displayText(self.text_list, self.line, self.font_size, self.color, 150, 400).passive_panel()
				self.scene_done = True
				continue

class activeScene:

	def __init__(self):
		pass

passiveScene('Scene1').execute()

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
