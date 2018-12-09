import pygame, sys

#dimensions variable
display_width = 1280
display_height = 720
panel_height = 138
panel_pos_y = 490
panel_offset = display_height - (panel_pos_y + 200)

# Kung gusto niyo itry if nagana yung scene, you can run the code tas click ka lang until makapunta ka sa scene na yun
# Or call the function in def main()
# Format ng pagcall ay sceneType('sceneName').execute(), example yung first line sa main

# VARIABLES
# A tuple of button names, nothing special here, unless we decide to change button graphics
buttons = ('button_blue', 'button_green', 'button_orange')

# A dictionary of scenes and the background to be used
# As of now, only one background can be called per scene
# Format is key:value with key is the scene name and value is name of background image without extension
# In general, images in our code should be called without the extension
# Extension should be .png
# Elements should be a string
scenery = {'Intro': 'dark_background', 'Intro2': 'dark_background', 'Intro3': 'dark_background', 'Scene4': 'placeholder_red', 'Scene5': 'placeholder_blue', 'Scene6': 'placeholder_purple', 'dIntro': 'placeholder_red','dScene2': 'placeholder_purple', 'dScene3': 'placeholder_green', 'dScene4': 'dark_background'}

# A dictionary of scene names and the characters involved
# As of now, only one character can be called per scene
# Same format as scenery but value is name of character image
# If there is no character involved in the scene, pass an empty string
character = {'Intro': '', 'Intro2': '', 'Intro3': '', 'Scene4': 'mom-solo', 'Scene5': 'mom-soloangry', 'Scene6': 'mom-solofinger', 'dIntro': 'mom-angry', 'dScene2': 'mom-happy', 'dScene3': 'mom-oface', 'dScene4': 'mom-solo'}

# A dicionary of scene names and the type of scene
# There are two scene types as of now, passiveScene and activeScene
# The capitalization of S is important
# passive is dialog only, while active involves decision
# Decision scenes will always accompany 3 choices
# Button and text placement will be changed
# Same format but value is the type of scene
scene_types = {'Intro': 'passiveScene', 'Intro2': 'passiveScene', 'Intro3': 'passiveScene', 'Scene4': 'passiveScene', 'Scene5': 'passiveScene', 'Scene6': 'passiveScene', 'dIntro': 'activeScene','dScene2': 'activeScene', 'dScene3': 'activeScene', 'dScene4': 'activeScene'}

# A dictionary of scene names and the dialog to be played
# This is exclusive to passiveScenes
# By default, activeScene plays the dialog 'Change your fate Kid'
# Format is scenename:dialog where dialog is a list
# The list should contain tuples with two elements
# Number of tuples inside the list may vary depending on scene but tuples will always have 2 elements
# The tuple format is (speaker, dialog)
dialogue = {'Intro': [('SELF', 'Why is it so dark in here?'),('SELF', 'Hmmm somebody must have turned off the lights'),('SELF', 'Seriously though, where am I?'),('SELF', 'But ... but first who am I?')], 'Intro2': [('devs', '*some sort of special scene here*'),('devs', 'haven\'t coded it yet'),('devs', 'should be an enter name prompt')], 'Intro3': [('devs', 'Oof'), ('devs', 'Sorry game devs suck'), ('devs', 'From now on, you\'re name\'s \"Kid\"'), ('devs', 'Deal with it')], 'Scene4': [('devs', 'If you wanna have some fun'), ('Tzuyu', 'jjapjjalhan gonggicheoreom'), ('Tzuyu', 'i sungane teukbyeolhan'), ('Tzuyu',  'haengbogeul notchiji ma')], 'Scene5': [('Mina', 'One, two, three, let\'s go'), ('Mina', 'chouju wiro'), ('Chaeyoung', 'narageul deut chumchureoga hey'), ('Chaeyoung', 'let\'s dance the night away')], 'Scene6': [('', '*music intensifies*'), ('Chaeyoung', 'Let’s dance the night away'), ('Jihyo', 'One, two, three, let’s go'), ('Jihyo', 'jeo bada geonneo'), ('Jihyo', 'deullil deut sori jilleo'), ('Jihyo', 'Let’s dance the night away')]}

# A dictionary that determines which scene is next
# Exclusive to passiveScene only, if you want to determine next scene of activeScene use outcome_actions
# Format is key:value where key is the current scene and value is the next scene
nexts = {'Intro': 'Intro2', 'Intro2': 'Intro3', 'Intro3': 'dScene2', 'Scene4': 'Scene5', 'Scene5': 'dScene3', 'Scene6': 'Intro'}

# A dictionary of the choices in activeScene
# Key:value format, key is scene name while value is a tuple with 3 elements
# Tuple's format is (choice1, choice2, choice3) from top to bottom
choice_texts = {'dIntro': ('Yes', 'or', 'Yes'), 'dScene2': ('What', 'is', 'Love?'), 'dScene3': ('Merry', 'and', 'Happy'), 'dScene4': ('Heart', 'Shaker', '*'), 'dScene5': ('Eye', 'Eye', 'Eyes'), 'dScene6': ('Stay', 'by my', 'Side')}

# A dictionary of outcome texts for an active scene
# Haven't implented this yet
outcome_texts = {'dIntro': (('What', 'is', 'Love?'), ('jjirit', 'jjirit', 'jjirit', 'jjirit'), ('You\'re', 'my', 'heartshaker shaker')), 'dScene2': (('What', 'is', 'Love?'), ('jjirit', 'jjirit', 'jjirit', 'jjirit'), ('You\'re', 'my', 'heartshaker shaker')), 'dScene3': (('What', 'is', 'Love?'), ('jjirit', 'jjirit', 'jjirit', 'jjirit'), ('You\'re', 'my', 'heartshaker shaker')), 'dScene4': (('What', 'is', 'Love?'), ('jjirit', 'jjirit', 'jjirit', 'jjirit'), ('You\'re', 'my', 'heartshaker shaker'))}

# A dictionary of next scenes for activeScene
# Basically, 'if i press this button, then ill go to this scene'
# Key:value format where value is a tuple of next scenes
# Value is (sceneA, sceneB, sceneC), arranged from top to bottom
outcome_actions = {'dIntro': ('dScene4', 'Intro2', 'dScene3'), 'dScene2': ('dIntro', 'dScene4', 'dScene3'), 'dScene3': ('dIntro', 'dScene2', 'dScene4'), 'dScene4': ('dScene3', 'dScene2', 'dIntro')}

# Should be a dictionary where there are some special interactions in a scene
# Will find a way to interact with this
oddities = {}

pygame.init()
gameDisplay = pygame.display.set_mode((display_width,display_height), pygame.FULLSCREEN)
pygame.display.toggle_fullscreen
pygame.display.set_caption('Kimi no Mama')
gameIcon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(gameIcon)

#colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (86, 86, 86)
transparent = (0, 0, 255, 0)

clock = pygame.time.Clock()

def string_to_callable(string):

	callables = {'passiveScene':passiveScene, 'activeScene':activeScene}
	callable_name = callables.get(string)
	return callable_name

class renderImage:

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

class displayText:

	def __init__(self, text_list, line = 0, size = 35, color = white, pos_x = 0, pos_y = 0, font = 'RobotoMono-Regular', path = 'assets/fonts/', extension = '.ttf'):

		self.text_list = text_list
		self.line = line
		self.font = path + font + extension
		self.size = size
		self.color = color
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.pos_y_mid = display_height - (panel_offset + panel_height/2)

	def passive_panel(self):

		fontography = pygame.font.Font(self.font, self.size)
		textSurface = fontography.render(self.text_list, True, self.color)
		textRect = textSurface.get_rect()
		textRect.midleft = (self.pos_x, self.pos_y_mid)
		gameDisplay.blit(textSurface, textRect)
		pygame.display.update()

	def active_panel(self):

		string = ''
		fontography = pygame.font.Font(self.font, self.size)
		for character in self.text_list:
			pygame.event.clear()
			pygame.time.wait(40)
			string += character
			textSurface = fontography.render(string, True, self.color)
			textRect = textSurface.get_rect()
			textRect.midleft = (self.pos_x, self.pos_y_mid)
			gameDisplay.blit(textSurface, textRect)
			pygame.display.update()
			clock.tick(60)

	def passivecenter(self):

		fontography = pygame.font.Font(self.font, self.size)
		textSurface = fontography.render(self.text_list, True, self.color)
		textRect = textSurface.get_rect()
		textRect.center = (self.pos_x, self.pos_y)
		gameDisplay.blit(textSurface, textRect)
		pygame.display.update()

	def passivemidleft(self):

		fontography = pygame.font.Font(self.font, self.size)
		textSurface = fontography.render(self.text_list, True, self.color)
		textRect = textSurface.get_rect()
		textRect.midleft = (self.pos_x, self.pos_y)
		gameDisplay.blit(textSurface, textRect)
		pygame.display.update()

class passiveScene:

	def __init__(self, scene_name):

		self.game_quit = False
		self.scene_done = False
		self.scene_name = scene_name
		self.line = 0
		self.next_scene = nexts.get(self.scene_name)
		self.background = scenery.get(self.scene_name)
		self.speaker = character.get(self.scene_name)
		self.next_type = string_to_callable(scene_types.get(self.next_scene))
		self.char_name_pos_x = 195
		self.char_name_pos_y = 550
		self.char_pos_x = 500
		self.char_pos_y = 150
		self.text_pos_x = 150
		self.panel_pos_y = panel_pos_y
		self.dialog_text_size = 37
		self.speaker_text_size = 35
		self.color_text = white
		self.color_speaker = gray
		self.speaker_font = 'RobotoMono-Italic'

	def execute(self):

		gameDisplay.fill(self.color_text)
		renderImage(self.background, 'scenery/').center()
		if self.speaker:
			renderImage(self.speaker, 'character/', 0, self.char_pos_y).midtop()
		renderImage('panel1', '', 0, self.panel_pos_y).midtop()
		while not self.game_quit:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						renderImage(self.background, 'scenery/').center()
						if self.speaker:
							renderImage(self.speaker, 'character/', 0, self.char_pos_y).midtop()
						renderImage('panel1', '', 0, self.panel_pos_y).midtop()
						self.line += 1
						if self.line == len(dialogue.get(self.scene_name)):
							self.next_type(self.next_scene).execute()
						self.scene_done = False
			self.speaker_name, self.text_list = dialogue.get(self.scene_name)[self.line]
			if not self.scene_done:
				displayText(self.speaker_name, 0, self.speaker_text_size, self.color_speaker, self.char_name_pos_x, self.char_name_pos_y, self.speaker_font).passivecenter()
				displayText(self.text_list, self.line, self.dialog_text_size, self.color_text, self.text_pos_x, 0).active_panel()
				self.scene_done = True
				continue
			else:
				renderImage(self.background, 'scenery/').center()
				if self.speaker:
					renderImage(self.speaker, 'character/', 0, self.char_pos_y).midtop()
				renderImage('panel1', '', 0, self.panel_pos_y).midtop()
				displayText(self.speaker_name, 0, self.speaker_text_size, self.color_speaker, self.char_name_pos_x, self.char_name_pos_y, self.speaker_font).passivecenter()
				displayText(self.text_list, self.line, self.dialog_text_size, self.color_text, self.text_pos_x, 0).passive_panel()

				self.scene_done = True
				continue

			clock.tick(60)

class activeScene:

	def __init__(self, scene_name):

		self.game_quit = False
		self.scene_name = scene_name
		self.outcome_text = outcome_texts.get(self.scene_name)
		self.possible_outcomes = outcome_actions.get(self.scene_name)
		self.choices = choice_texts.get(self.scene_name)
		self.background = scenery.get(self.scene_name)
		self.speaker = character.get(self.scene_name)
		self.oddity = oddities.get(scene_name)
		self.char_name_pos_x = 195
		self.char_name_pos_y = 550
		self.button_pos_x = 250
		self.button_pos_y = 310
		self.char_pos_x = 700
		self.char_pos_y = 150
		self.button_offset_x = 70
		self.text_pos_x = 150
		self.text_button_os_y = 24
		self.button_offset_y = 4
		self.panel_pos_y = panel_pos_y
		self.dialog_text_size = 37
		self.speaker_text_size = 35
		self.color = white
		self.color_speaker = gray
		self.speaker_font = 'RobotoMono-Italic'

	def execute(self):
		gameDisplay.fill(self.color)
		renderImage(self.background, 'scenery/').center()
		if self.speaker:
			renderImage(self.speaker, 'character/', self.char_pos_x, self.char_pos_y).coordinates()
		if self.oddity:
			renderImage(self.oddity, 'character/', 0, self.char_pos_y).midtop()
		renderImage('panel1', '', 0, self.panel_pos_y).midtop()
		displayText('devs', 0, self.speaker_text_size, self.color_speaker, self.char_name_pos_x, self.char_name_pos_y, self.speaker_font).passivecenter()
		displayText('Change your fate Kid', 0, self.dialog_text_size, self.color, self.text_pos_x, 0).active_panel()
		displayText(self.choices[0], 0, self.dialog_text_size, self.color, self.button_pos_x + self.button_offset_x, self.button_pos_y + self.text_button_os_y).passivemidleft()
		displayText(self.choices[1], 0, self.dialog_text_size, self.color, self.button_pos_x + self.button_offset_x, self.button_pos_y + self.text_button_os_y + 60).passivemidleft()
		displayText(self.choices[2], 0, self.dialog_text_size, self.color, self.button_pos_x + self.button_offset_x, self.button_pos_y + self.text_button_os_y + 120).passivemidleft()
		while not self.game_quit:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			clickButton(self.button_pos_x, self.button_pos_y, buttons[0], self.possible_outcomes[0]).aScene()
			clickButton(self.button_pos_x, self.button_pos_y + 60, buttons[1], self.possible_outcomes[1]).aScene()
			clickButton(self.button_pos_x, self.button_pos_y + 120, buttons[2], self.possible_outcomes[2]).aScene()
			pygame.display.update()
			clock.tick(60)

class clickButton:

	def __init__(self, pos_x, pos_y, image, action = None, image_type = 'buttons/', button_width = 48, button_height = 48):
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.image = image
		self.action = action
		self.image_type = image_type
		self.button_width = button_width
		self.button_height = button_height

	def aScene(self): 

		mouse_position = pygame.mouse.get_pos()
		left_click = pygame.mouse.get_pressed()[0]
		buttonRect = pygame.draw.rect(gameDisplay, transparent, [self.pos_x, self.pos_y, self.button_width, self.button_height])

		if buttonRect.collidepoint(mouse_position):
			renderImage('hover' + self.image, self.image_type, self.pos_x, self.pos_y).coordinates()
			if left_click and self.action:
				renderImage(self.image, self.image_type, self.pos_x, self.pos_y).coordinates()
				string_to_callable(scene_types.get(self.action))(self.action).execute()

		else:
			renderImage(self.image, self.image_type, self.pos_x, self.pos_y).coordinates()

	def simple(self):

		mouse_position = pygame.mouse.get_pos()
		left_click = pygame.mouse.get_pressed()[0]
		buttonRect = pygame.draw.rect(gameDisplay,transparent, [self.pos_x, self.pos_y, self.button_width, self.button_height])

		if buttonRect.collidepoint(mouse_position):
			renderImage('hover' + self.image, self.image_type, self.pos_x, self.pos_y).coordinates()
			if left_click and self.action:
				action()

		else:
			renderImage(self.image, self.pos_x, self.pos_y).coordinates()

def main():

	a = passiveScene('Intro').execute()
	print(a)
	pygame.quit()
	quit()

if __name__ == '__main__':
	main()