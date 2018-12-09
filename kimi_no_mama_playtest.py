import pygame, sys
from pygame.locals import *
import time

#dimensions variable
display_width = 1280
display_height = 720
panel_height = 138
panel_pos_y = 490
panel_offset = display_height - (panel_pos_y + 200)

#a dictionary of everything
buttons = ('button_green', 'button_green', 'button_green')
scenery = {'Scene1': 'dark_background', 'Scene2': 'placeholder_bg1', 'Scene3': 'placeholder_green', 'Scene4': 'placeholder_red', 'Scene5': 'placeholder_blue', 'Scene6': 'placeholder_purple', 'dScene1': 'placeholder_red','dScene2': 'placeholder_purple', 'dScene3': 'placeholder_green', 'dScene4': 'dark_background'}
character = {'Scene1': '', 'Scene2': 'mom-happy', 'Scene3': 'mom-oface', 'Scene4': 'mom-solo', 'Scene5': 'mom-soloangry', 'Scene6': 'mom-solofinger', 'dScene1': 'mom-angry', 'dScene2': 'mom-happy', 'dScene3': 'mom-oface', 'dScene4': 'mom-solo'}
scene_types = {'Scene1': 'passiveScene', 'Scene2': 'passiveScene', 'Scene3': 'passiveScene', 'Scene4': 'passiveScene', 'Scene5': 'passiveScene', 'Scene6': 'passiveScene', 'dScene1': 'activeScene','dScene2': 'activeScene', 'dScene3': 'activeScene', 'dScene4': 'activeScene'}
dialogue = {'Scene1': [('', '*awesome intro*')], 'Scene2': [('Momo', 'badaya uriwa gachi nora'), ('Momo', 'barama neodo ijjogeuro wa')], 'Scene3': [('Jeongyeon', 'dalppit jomyeong araeseo'), ('Jeongyeon', 'neowa nawa sesanggwa'), ('Jeongyeon', 'da gachi Party all night long'), ('Jeongyeon', 'Yeah, it’s good')], 'Scene4': [('Tzuyu', 'If you wanna have some fun'), ('Tzuyu', 'jjapjjalhan gonggicheoreom'), ('Tzuyu', 'i sungane teukbyeolhan'), ('Tzuyu',  'haengbogeul notchiji ma')], 'Scene5': [('Mina', 'One, two, three, let\'s go'), ('Mina', 'chouju wiro'), ('Chaeyoung', 'narageul deut chumchureoga hey'), ('Chaeyoung', 'let\'s dance the night away')], 'Scene6': [('', '*music intensifies*'), ('Chaeyoung', 'Let’s dance the night away'), ('Jihyo', 'One, two, three, let’s go'), ('Jihyo', 'jeo bada geonneo'), ('Jihyo', 'deullil deut sori jilleo'), ('Jihyo', 'Let’s dance the night away')]}
nexts = {'Scene1': 'dScene2', 'Scene2': 'Scene3', 'Scene3': 'Scene4', 'Scene4': 'Scene5', 'Scene5': 'Scene6', 'Scene6': 'Scene1'}
choice_texts = {'dScene1': ('Yes', 'or', 'Yes'), 'dScene2': ('Yes', 'or', 'Yes'), 'dScene3': ('Yes', 'or', 'Yes'), 'dScene4': ('Yes', 'or', 'Yes'), 'dScene5': ('Yes', 'or', 'Yes'), 'dScene6': ('Yes', 'or', 'Yes')}
outcome_texts = {'dScene1': (('What', 'is', 'Love?'), ('jjirit', 'jjirit', 'jjirit', 'jjirit'), ('You\'re', 'my', 'heartshaker shaker')), 'dScene2': (('What', 'is', 'Love?'), ('jjirit', 'jjirit', 'jjirit', 'jjirit'), ('You\'re', 'my', 'heartshaker shaker')), 'dScene3': (('What', 'is', 'Love?'), ('jjirit', 'jjirit', 'jjirit', 'jjirit'), ('You\'re', 'my', 'heartshaker shaker')), 'dScene4': (('What', 'is', 'Love?'), ('jjirit', 'jjirit', 'jjirit', 'jjirit'), ('You\'re', 'my', 'heartshaker shaker'))}
outcome_actions = {'dScene1': ('dScene4', 'Scene2', 'dScene3'), 'dScene2': ('dScene1', 'dScene4', 'dScene3'), 'dScene3': ('dScene1', 'dScene2', 'dScene4'), 'dScene4': ('dScene3', 'dScene2', 'dScene1')}
oddities = {}

pygame.init()
gameDisplay = pygame.display.set_mode((display_width,display_height), pygame.FULLSCREEN)
pygame.display.toggle_fullscreen
pygame.display.set_caption('Kimi no Mama')
gameIcon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(gameIcon)

#colors in a tuple
black = (0, 0, 0)
transparent = (0, 0, 255, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)

clock = pygame.time.Clock()

def string_to_callable(string): #parameters: string

	callables = {'passiveScene':passiveScene, 'activeScene':activeScene}
	callable_name = callables.get(string)
	return callable_name

def button(pos_x, pos_y, image, action = None, image_type = 'buttons/', button_width = 48, button_height = 48): #parameters: pos_x, pos_y, image, image_type = 'button/', action = None, button_width = 48, button_height = 48

	mouse_position = pygame.mouse.get_pos()
	left_click, scroll, right_click = pygame.mouse.get_pressed()
	buttonRect = pygame.draw.rect(gameDisplay,transparent, [pos_x,pos_y, button_width, button_height])

	if buttonRect.collidepoint(mouse_position):
		renderImage('hover' + image, image_type, pos_x, pos_y).coordinates()
		if left_click and action:
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

	def __init__(self, text_list, line = 0, size = 35, color = white, pos_x = 0, pos_y = 0, font = 'assets/DeJavuSans.ttf'):
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
		textSurface = fontography.render(self.text_list, True, self.color)
		textRect = textSurface.get_rect()
		textRect.midleft = (self.pos_x, self.pos_y)
		gameDisplay.blit(textSurface, textRect)
		pygame.display.update()

	def active_panel(self):

		string = ''
		fontography = pygame.font.Font(self.font, self.size)
		for character in self.text_list:
			pygame.time.wait(40)
			string += character
			textSurface = fontography.render(string, True, self.color)
			textRect = textSurface.get_rect()
			textRect.midleft = (self.pos_x, self.pos_y)
			gameDisplay.blit(textSurface, textRect)
			pygame.display.update()
			clock.tick(60)

	def passive(self):

		fontography = pygame.font.Font(self.font, self.size)
		textSurface = fontography.render(self.text_list, True, self.color)
		textRect = textSurface.get_rect()
		textRect.topleft = (self.pos_x, self.pos_y_speaker)
		gameDisplay.blit(textSurface, textRect)
		pygame.display.update()

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
		if self.speaker:
			renderImage(self.speaker, 'character/', 0, self.char_pos_y).midtop()
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

class activeScene: 

	def __init__(self, scene_name):
		global scenery
		global choice_texts
		global outcome_actions
		global outcome_texts
		global oddities
		global buttons
		self.scene_name = scene_name
		self.outcome_text = outcome_texts.get(self.scene_name)
		self.possible_outcomes = outcome_actions.get(self.scene_name)
		self.choices = choice_texts.get(self.scene_name)
		self.background = scenery.get(self.scene_name)
		self.speaker = character.get(self.scene_name)
		self.oddity = oddities.get(scene_name)
		self.speaker_pos_x = 135
		self.speaker_pos_y = 518
		self.button_pos_x = 250
		self.button_pos_y = 310
		self.char_pos_x = 700
		self.char_pos_y = 150
		self.button_offset_x = 70
		self.button_offset_y = 3
		self.panel_pos_y = panel_pos_y
		self.dialog_text_size = 37
		self.speaker_text_size = 35
		self.color = white
		self.game_quit = False

	def execute(self):
		gameDisplay.fill(self.color)
		renderImage(self.background, 'scenery/').center()
		if self.speaker:
			renderImage(self.speaker, 'character/', self.char_pos_x, self.char_pos_y).coordinates()
		if self.oddity:
			renderImage(self.oddity, 'character/', 0, self.char_pos_y).midtop()
		renderImage('panel', '', 0, self.panel_pos_y).midtop()
		displayText('DEVS', 0, self.speaker_text_size, self.color, self.speaker_pos_x, self.speaker_pos_y).passive()
		displayText(self.choices[0], 0, self.dialog_text_size, self.color, self.button_pos_x + self.button_offset_x, self.button_pos_y + self.button_offset_y).passive()
		displayText(self.choices[1], 0, self.dialog_text_size, self.color, self.button_pos_x + self.button_offset_x, self.button_pos_y + self.button_offset_y + 60).passive()
		displayText(self.choices[2], 0, self.dialog_text_size, self.color, self.button_pos_x + self.button_offset_x, self.button_pos_y + self.button_offset_y + 120).passive()
		while not self.game_quit:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			buttonss(self.button_pos_x, self.button_pos_y, buttons[0], self.possible_outcomes[0])
			buttonss(self.button_pos_x, self.button_pos_y + 60, buttons[1], self.possible_outcomes[1])
			buttonss(self.button_pos_x, self.button_pos_y + 120, buttons[2], self.possible_outcomes[2])
			pygame.display.update()
			clock.tick(60)

def buttonss(pos_x, pos_y, image, action = None, image_type = 'buttons/', button_width = 48, button_height = 48): #parameters: pos_x, pos_y, image, image_type = 'button/', action = None, button_width = 48, button_height = 48
    global scene_types

    mouse_position = pygame.mouse.get_pos()
    left_click, scroll, right_click = pygame.mouse.get_pressed()
    buttonRect = pygame.draw.rect(gameDisplay, transparent, [pos_x,pos_y, button_width, button_height])

    if buttonRect.collidepoint(mouse_position):
        renderImage('hover' + image, image_type, pos_x, pos_y).coordinates()
        if left_click and action:
            renderImage(image, image_type, pos_x, pos_y).coordinates()
            string_to_callable(scene_types.get(action))(action).execute()

    else:
        renderImage(image, image_type, pos_x, pos_y).coordinates()

def main():

	passiveScene('Scene1').execute()
	pygame.quit()
	quit()

if __name__ == '__main__':
	main()