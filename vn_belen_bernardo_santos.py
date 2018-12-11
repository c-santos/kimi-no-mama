import pygame
import pickle
import datetime
import os.path
import glob

# DIMENSIONS
display_width = 1280
display_height = 720
panel_height = 138
panel_pos_y = 490
panel_offset = display_height - (panel_pos_y + 200)

# COLORS
black = (0, 0, 0)
white = (255, 255, 255)
gray = (86, 86, 86)
transparent = (100, 0, 0, 128)

# Kung gusto niyo itry if nagana yung scene, you can run the code tas click ka lang until makapunta ka sa scene na yun
# Or call the function in def main()
# Format ng pagcall ay sceneType('sceneName').execute(), example yung first line sa main

# VARIABLES
# A tuple of button names, nothing special here, unless we decide to change button graphics
item_buttons = ('flashdrive_button', 'journal_button', 'levelup1_button', 'levelup2_button', 'levelup3_button', 'piano_button', 'soup_button', 'twice_button', 'whitebrick_button')
buttons = ('button_blue', 'button_green', 'button_orange')
start_buttons = ('new_game', 'load_game', 'quit')

# A dictionary of scene names and the type of scene
# There are two scene types as of now, passiveScene and activeScene
# The capitalization of S is important
# passive is dialog only, while active involves decision
# Decision scenes will always accompany 3 choices
# Button and text placement will be changed
# Same format but value is the type of scene
scene_types = {
	'Scene0': 'passiveScene',
	'Scene1': 'passiveScene',
	'dScene1': 'activeScene',
		'Scene1.1': 'passiveScene',
		'Scene1.2': 'passiveScene',  
		'Scene1.3': 'passiveScene',
	'Scene2': 'passiveScene',
	'dScene2': 'activeScene',
		'Scene2.1': 'passiveScene',
	'Scene3': 'passiveScene',
	'Scene4': 'passiveScene',
	'Scene5': 'passiveScene',
	'Scene6': 'passiveScene',
	'dScene6': 'activeScene',
		'Scene6.1': 'passiveScene',
		'Scene6.2': 'passiveScene',
		'Scene6.3': 'passiveScene',
	'Scene7': 'passiveScene',
	'Scene8': 'passiveScene',
	'InfancyEvolution': 'passiveScene', # EVOL SCENE

	'Scene9': 'passiveScene',
	'dScene9': 'activeScene',
		'Scene9.1': 'passiveScene',
		'Scene9.2': 'passiveScene',
		'Scene9.3': 'passiveScene',
	'Scene10': 'passiveScene',
	'dScene10': 'activeScene',
		'Scene10.1': 'passiveScene',
		'Scene10.2': 'passiveScene',
		'Scene10.3': 'passiveScene',
	'Scene11': 'passiveScene',
	'dScene11': 'activeScene',
		'Scene11.1': 'passiveScene',
			'Scene12': 'passiveScene',
			'Scene13': 'passiveScene',
			'Scene14': 'passiveScene',
			'dScene14': 'activeScene',
				'Scene14.1': 'passiveScene',
				'Scene14.2': 'passiveScene',
			'Scene15': 'passiveScene',
			'dScene15': 'activeScene',
				'Scene15.1': 'passiveScene', 
					'Scene15.1.1': 'passiveScene',
						'dScene15.1.1': 'activeScene',
							'Scene15.1.1.1': 'passiveScene',
							'Scene15.1.1.2': 'passiveScene',
				'Scene15.2': 'passiveScene',
					'Scene15.2.1': 'passiveScene',
						'dScene15.2.1': 'activeScene',
							'Scene15.2.1.1': 'passiveScene',
							'Scene15.2.1.2': 'passiveScene',
				'Scene15.3': 'passiveScene',

		'Scene11.2': 'passiveScene',
		'Scene16': 'passiveScene',
		'Scene17': 'passiveScene',
	'ChildhoodEvolution1': 'passiveScene', # EVOL SCENE
	'ChildhoodEvolution2': 'passiveScene', # EVOL SCENE

	'Scene18': 'passiveScene',
	'Scene19': 'passiveScene',
	'Scene20': 'passiveScene',
	'Scene21': 'passiveScene',
	'Scene22': 'passiveScene',  # SUICIDE ATTEMPT 1 (from POSTER SCENE)
	'Scene23': 'passiveScene',
	'Scene23.1': 'passiveScene',
	'Scene24': 'passiveScene',
	'Scene25': 'passiveScene',
	'Scene26': 'passiveScene',
	'Scene27': 'passiveScene',
	'dScene27': 'activeScene',
	'Scene27.1.1': 'passiveScene',
	'Scene27.1.2': 'passiveScene',
	'Scene27.1.3': 'passiveScene',
	'Scene27.1.4': 'passiveScene',
	'Scene28': 'passiveScene',
	'dScene28': 'activeScene',
	'Scene29': 'passiveScene',
	'Scene30': 'passiveScene',
	'TeenagehoodEvolution1': 'passiveScene', # EVOL SCENE End 1
	'TeenagehoodEvolution2': 'passiveScene', # EVOL SCENE End 2
	'Scene31': 'passiveScene',
	'Scene32': 'passiveScene',
	'Scene33': 'passiveScene',
	'Scene34': 'passiveScene',
	'Scene35': 'passiveScene',
	'Scene36': 'passiveScene',
	'Scene37': 'passiveScene',

	'GameOver': 'activeScene',
	}

# A dictionary that determines which scene is next
# IMPORTANT UPDATE: This is no longer exclusive to passiveScene
# Use format in outcome_actions for activeScene
# Pero same format pa din if passive yung current scene
# Format is key:value where key is the current scene and value is the next scene(s)
nexts = {
	'Scene0': 'Scene1',
	'Scene1': 'dScene1',
	'dScene1': ('Scene1.1', 'Scene1.2', 'Scene1.3'),
		'Scene1.1': 'Scene2',
		'Scene1.2': 'Scene2',
		'Scene1.3': 'GameOver',
	'Scene2': 'dScene2',
	'dScene2': ('Scene3', 'Scene2.1', ''),
		'Scene2.1': 'GameOver',
	'Scene3': 'Scene4',
	'Scene4': 'Scene5',
	'Scene5': 'Scene6',
	'Scene6': 'dScene6',
	'dScene6': ('Scene6.1', 'Scene6.2', 'Scene6.3'),
		'Scene6.1': 'Scene8',
		'Scene6.2': 'Scene7',
		'Scene6.3': 'Scene7',
	'Scene7': 'Scene8',
	'Scene8': 'InfancyEvolution',
	'InfancyEvolution': 'Scene9',

	'Scene9': 'dScene9',
	'dScene9': ('Scene9.1', 'Scene9.2', 'Scene9.3'),
		'Scene9.1': 'GameOver',
		'Scene9.2': 'Scene10',
		'Scene9.3': 'Scene10',
	'Scene10': 'dScene10',
	'dScene10': ('Scene10.1', 'Scene10.2', 'Scene10.3'),
		'Scene10.1': 'Scene11',
		'Scene10.2': 'Scene11',
		'Scene10.3': 'Scene11',
	'Scene11': 'dScene11',
	'dScene11': ('Scene11.1', 'Scene11.2', ''), 
		'Scene11.1': 'Scene12', #  ROOFTOP SCENE
			'Scene12': 'Scene13',
			'Scene13': 'Scene14',
			'Scene14': 'dScene14',
			'dScene14': ('Scene14.1', 'Scene14.2', 'Scene14.1'),  # POSTER SCENE
				'Scene14.1': 'Scene15',
				'Scene14.2': 'Scene15',
				'Scene15': 'dScene15',
					'dScene15': ('Scene15.1', 'Scene15.2', 'Scene15.3'), #  BUS STOP SCENE
						'Scene15.1': 'Scene15.1.1',
							'Scene15.1.1': 'dScene15.1.1',
								'dScene15.1.1': ('Scene15.1.1.1', 'Scene15.1.1.2', 'Scene15.1.1.1'), #  USB
									'Scene15.1.1.1': 'ChildhoodEvolution',
									'Scene15.1.1.2': 'ChildhoodEvolution',
						'Scene15.2': 'Scene15.2.1',
							'Scene15.2.1': 'dScene15.2.1',
								'dScene15.2.1': ('Scene15.2.1.1', 'Scene15.2.1.2', 'Scene15.2.1.1'), #  coke
									'Scene15.2.1.1': 'ChildhoodEvolution2',
									'Scene15.2.1.2': 'ChildhoodEvolution2',
						'Scene15.3': 'GameOver', #  SOUP

		'Scene11.2': 'Scene16', #  CAFETERIA SCENE
		'Scene16': 'Scene17',
		'Scene17': 'ChildhoodEvolution1',

		'ChildhoodEvolution1': 'Scene18',
		'Scene18': 'Scene19',
		'Scene19': 'Scene20',
		'Scene20': 'Scene21',
		'Scene21': 'Scene22',
		'Scene22': 'Scene23',
		'Scene23': 'Scene24',
		'Scene24': 'GameOver',

		'ChildhoodEvolution2': 'Scene23.1',
		'Scene23.1': 'Scene25',
		'Scene25': 'Scene26',
		'Scene26': 'Scene27',
		'Scene27': 'dScene27',
		'dScene27': ('Scene27.1.1', 'Scene28', 'Scene28'),
		'Scene27.1.1': 'Scene27.1.2',
		'Scene27.1.2': 'Scene27.1.3',
		'Scene27.1.3': 'Scene27.1.4',
		'Scene28': 'dScene28',
		'dScene28': ('Scene29', 'Scene30', 'Scene30'),
		'Scene29': 'TeenagehoodEvolution1',
		'Scene30': 'TeenagehoodEvolution2',

		'TeenagehoodEvolution1': 'Scene31',
		'Scene31': 'Scene23',
		'Scene32': 'Scene24',
		'Scene33': 'GameOver',
		'TeenagehoodEvolution2': 'Scene34',
		'Scene34': 'Scene35',
		'Scene35': 'Scene36',
		'Scene36': 'Scene37',
		'Scene37': 'GameOver',
	'GameOver': ('Scene0', '', '')
	}


# A dictionary of scenes and the background to be used
# As of now, only one background can be called per scene
# Format is key:value with key is the scene name and value is name of background image without extension
# In general, images in our code should be called without the extension
# Extension should be .png
# Elements should be a string
scenery = {
	'Scene0': 'dark_background',
	'Scene1': 'dark_background',
	'dScene1': 'dark_background',
		'Scene1.1': 'dark_background',
		'Scene1.2': 'dark_background',
		'Scene1.3': 'dark_background',
	'Scene2': 'dark_background',
	'dScene2': 'dark_background',
		'Scene2.1': 'dark_background',
	'Scene3': 'dark_background',
	'Scene4': 'hospital',
	'Scene5': 'outside-day',
	'Scene6': 'living-sunset',
	'dScene6': 'living-sunset',
		'Scene6.1': 'living-sunset',
		'Scene6.2': 'living-sunset',
		'Scene6.3': 'living-sunset',
	'Scene7': 'bathroom',
	'Scene8': 'bedroom-night',
	'InfancyEvolution': 'dark_background',  # BLACK SCREEN ASSET

	'Scene9': 'bedroom',
	'dScene9': 'bedroom',
		'Scene9.1': 'bedroom',
		'Scene9.2': 'bedroom',
		'Scene9.3': 'bedroom',
	'Scene10': 'kitchen-day',
	'dScene10': 'kitchen-day',
		'Scene10.1': 'kitchen-day',
		'Scene10.2': 'kitchen-day',
		'Scene10.3': 'kitchen-day',
	'Scene11': 'classroom',
	'dScene11': 'classroom',
		'Scene11.1': 'classroom',
			'Scene12': 'stairway',
			'Scene13': 'rooftop',
			'Scene14': 'hallway-2',
			'dScene14': 'hallway-2',# POSTER SCENE
				'Scene14.1': 'hallway-2',
				'Scene14.2': 'hallway-2',
			'Scene15': 'street-morning',
			'dScene15': 'street-morning', #  BUS STOP SCENE
				'Scene15.1': 'street-morning', #  USB
					'Scene15.1.1': 'bedroom-dusk',
						'dScene15.1.1': 'bedroom-dusk', # CHECK OR SLEEP
							'Scene15.1.1.1': 'bedroom-night',
							'Scene15.1.1.2': 'bedroom-night',
				'Scene15.2': 'street-morning', #  SHROOMS
					'Scene15.2.1': 'bedroom-dusk',
						'dScene15.2.1': 'bedroom-dusk', # CHECK OR SLEEP
							'Scene15.2.1.1': 'bedroom-night',
							'Scene15.2.1.2': 'bedroom-night',
				'Scene15.3': 'dark_background', #  SOUP

		'Scene11.2': 'classroom', #  CAFETERIA SCENE
		'Scene16': 'cafeteria',
		'Scene17': 'living-dusk',
	'ChildhoodEvolution1': 'dark_background', # EVOL SCENE
	'ChildhoodEvolution2': 'dark_background', # EVOL SCENE

	'Scene18': 'bedroom',
	'Scene19': 'living',
	'Scene20': 'hospital',
	'Scene21': 'hospital',
	'Scene22': 'bedroom-dusk',
	'Scene23': 'kitchen-day',
	'Scene23.1': 'kitchen-day',
	'Scene24': 'bedroom',
	'Scene25': 'bedroom',
	'Scene26': 'kitchen-day',
	'Scene27': 'school',
	'dScene27': 'school',
	'Scene27.1.1': 'classroom',
	'Scene27.1.2': 'hallway-2',
	'Scene27.1.3': 'stairway',
	'Scene27.1.4': 'rooftop',
	'Scene28': 'school',
	'dScene28': 'bedroom',
	'Scene29': 'bedroom-night',
	'Scene30': 'bedroom-dusk',
	'TeenagehoodEvolution1': 'dark_background',
	'TeenagehoodEvolution1': 'dark_background',

	'Scene31': 'cafe',
	'Scene32': 'park',
	'Scene33': 'kimi',

	'Scene34': 'bedroom',
	'Scene35': 'living',
	'Scene36': 'store',
	'Scene37': 'hospital',

	'GameOver': 'dark_background',
	}

# A dictionary of scene names and the characters involved
# As of now, only one character can be called per scene
# Same format as scenery but value is name of character image
# If there is no character involved in the scene, pass an empty string
character = {	
	'Scene0': '',
	'Scene1': '',
	'dScene1': '',
		'Scene1.1': '',
		'Scene1.2': '',
		'Scene1.3': '',
	'Scene2': '',
	'dScene2': '',
		'Scene2.1': '',
	'Scene3': '',
	'Scene4': 'doctor',
	'Scene5': '',
	'Scene6': 'mom-oface',
	'dScene6': 'mom-oface',
		'Scene6.1': 'mom-startled',
		'Scene6.2': 'mom-angry',
		'Scene6.3': 'mom-angry',
	'Scene7': 'mom-solosigh',
	'Scene8': '',
	'InfancyEvolution': 'levelup1',  # TRANSMOD ASSET

	'Scene9': 'mom-soloangry',
	'dScene9': 'mom-soloangry',
		'Scene9.1': '',
		'Scene9.2': '',
		'Scene9.3': '',
	'Scene10': 'mom-solo',
	'dScene10': 'mom-solo',
		'Scene10.1': 'mom-solofinger',
		'Scene10.2': 'mom-soloangry',
		'Scene10.3': 'mom-soloangry',
	'Scene11': '',
	'dScene11': '',
		'Scene11.1': '',
			'Scene12': 'twice',  # TWICE ALBUM COVER
			'Scene13': '',
			'Scene14': '',
			'dScene14': '',
				'Scene14.1': '',
				'Scene14.2': '',
			'Scene15': '',
			'dScene15': '',
				'Scene15.1': 'flashdrive',
					'Scene15.1.1': '',
						'dScene15.1.1': '',
							'Scene15.1.1.1': 'flashdrive',
							'Scene15.1.1.2': '',
				'Scene15.2': 'whitebrick',
					'Scene15.2.1': '',
						'dScene15.2.1': '',
							'Scene15.2.1.1': 'whitebrick',
							'Scene15.2.1.2': '',
				'Scene15.3': '',

		'Scene11.2': '',
		'Scene16': '',
		'Scene17': 'piano', 
		'ChildhoodEvolution1': 'levelup2', # EVOL SCENE
		'ChildhoodEvolution2': 'levelup2', # EVOL SCENE

	'Scene18': '',
	'Scene19': '',
	'Scene20': 'doctor',
	'Scene21': 'mom-solosigh',
	'Scene22': '',
	'Scene23': 'mom-solosigh',
	'Scene23.1': 'mom-solosigh',
	'Scene24': '',
	'Scene25': 'mom-solofinger',
	'Scene26': 'mom-solofinger',
	'Scene27': '',
	'dScene27': 'journal',
	'Scene27.1.1': '',
	'Scene27.1.2': '',
	'Scene27.1.3': '',
	'Scene27.1.4': '',
	'Scene28': '',
	'dScene28': '',
	'Scene29': '',
	'Scene30': '',
	'TeenagehoodEvolution1': 'levelup3',
	'TeenagehoodEvolution1': 'levelup3',
	
	'Scene31': '',
	'Scene32': '',
	'Scene33': 'dad',

	'Scene34': '',
	'Scene35': 'granny',
	'Scene36': '',
	'Scene37': 'doctor',

	'GameOver': 'credits',
	}

# A dictionary of scene names and the dialog to be played
# This is exclusive to passiveScenes
# By default, activeScene plays the dialog 'Change your fate Kid'
# Format is scenename:dialog where dialog is a list
# The list should contain tuples with two elements
# Number of tuples inside the list may vary depending on scene but tuples will always have 2 elements
# The tuple format is (speaker, dialog)
dialogue = {
	'Scene0': [
		('SELF', 'Why is it so dark in here?'),
		('SELF', 'Hmmm somebody must have turned off the lights'),
		('SELF', 'Seriously though, where am I?'),
		('SELF', 'But ... but first who am I?')
		], 
	'Scene1': [
		('devs', '*some sort of special scene here*'),
		('devs', 'haven\'t coded it yet'),
		('devs', 'should be an enter name prompt.'),
		('devs', 'Oof. Game devs suck.'),
		('SELF', 'I still don’t know where I am...'),
		('SELF', 'But it seems like I\'m inside a cave.'),
		('SELF', 'There must be a way out...'),
		], 
	'Scene1.1': [
		('devs', 'It’s as if you’re inside an elastic cage...'),
		('devs', 'Wait, what’s that? You hear a muffled voice...'),
		('???', 'I\'m going to see you real soon, Kid.'),
		('devs', 'For some reason, you remember the voice'),
		('SELF', 'Man, that was tiring. Let me just sleep.'),
		],
	'Scene1.2': [
		('devs', 'You tried to feel but the surroundings'),
		('devs', 'don’t have the same feelings for you.'),
		('devs', 'This is so sad.'),
		('devs', 'Alexa might know what to do.'),
		],
	'Scene1.3': [
		('devs', 'As you shadow boxed around the area,'), 
		('devs', 'you became more aware of your surroundings.'),
		('devs', 'It seems like you’re trapped'),
		('devs', 'in some kind of elastic cage...'),
		('devs', 'Just outside the cave,'),
		('devs', 'you hear somebody moan...'),
		('???', 'Ugh, that hurts... fuck!'),
		('devs', 'For some reason, you died.'),
		('devs', 'We won’t tell you how though.'),
		('devs', 'Next time, don’t be a small brain.'),
		],
	'Scene2': [
		('devs', 'Suddenly, a flash of light appears.'), 
		('devs', 'You see a hole.'),
		('SELF', 'It must be the exit!'),
		('SELF', 'But should I really go that way?'),
		],
	'Scene2.1': [
		('devs', 'For some reason, you died.'), 
		('devs', 'You’ll never know what’s on the other side.'),
		('devs', 'You’ll get it next time buddy.'),
		],
	'Scene3': [
		('devs', 'As you were nearing the blinding light,'),
		('devs', 'you finally realized what was happening.'),
		('devs', 'You’re a baby!'),
		('devs', 'What do you think your gender should be?'),
		('devs', 'Sike!'),
		('devs', 'We already assumed your gender, sorry.'),
		('SELF', 'Isn\'t that kind of sexist...'),
		('devs', 'Fly away you little shit.'),
		('devs', 'By the way, good luck dealing with your mom.'),
		],
	'Scene4': [
		('DOC', 'Congratulations, Ma\'am, it was successful'),
		('DOC', 'and it’s a baby boy!'),
		('DOC', 'Good luck on your motherhood.'),
		('devs', 'Just before you "evolve",'),
		('devs', 'you see that devilish smile of hers.'),
		('devs', 'But she doesn’t know what’s coming.'),
		('devs', 'Good luck to her indeed.'),
		],
	'Scene5': [
		('devs', 'After two months...'),
		],
	'Scene6': [
		('SELF', 'It’s been two months and this old woman'),
		('SELF', 'right here is still baby talking you.'),
		('SELF', 'She wants stupid? Show her stupid.'),
		],
	'Scene6.1': [
		('devs', 'Good thing you learned how to cry!'),
		('MOM', 'Awww, don’t cry Kid.'),
		('MOM', 'You know you’re so cute when you cry.'),
		('SELF', 'Oh come on! How is that cute?'),
		],
	'Scene6.2': [
		('MOM', 'You puked all over me.'),
		('MOM', 'Now I’m gonna have to clean this all up.'),
		],
	'Scene6.3': [
		('MOM', 'What’s that smell?'),
		('NON', 'You filthy motherfucker!'),
		('MOM', 'The fucker just shat all over me.'),
		('MOM', 'Alright then, I guess I should clean you up.'),
		],
	'Scene7': [
		('SELF', 'Brrrr the water’s so damn cold!'),
		('SELF', 'Ah shit, now I’m guilty!'),
		('MOM', 'My, my what a little troublemaker you are.'),
		('MOM', 'You’re all cleaned up now!'),
		('MOM', 'Time to go to bed, Kid.'),
		],
	'Scene8': [
		('devs', 'As the night deepens, your mom falls asleep'),
		('devs', 'while caressing you.'),
		('devs', 'You close your eyes and get ready'),
		('devs', 'for the future days to come.'),
		],
	'Scene9': [
		('MOM', 'Kid! Wake up!'),
		('MOM', 'Kid!!!!!!!!!! '),
		('MOM', 'Get ready for school you’re going to be late!'),
		('SELF', 'Okay Mom, I’ll be there in a minute.'),
		('MOM', 'You better make sure you’re not going to'),
		('MOM', 'fall asleep again or I’m going to kill you.'),
		('SELF', 'Agh, mom is such a hothead.'),
		('SELF', 'Should kids even go to school?'),
		('SELF', 'That’s illegal.'),
		],
	'Scene9.1': [
		('devs', 'And that was the last time you fell asleep.'),
		],
	'Scene9.2': [
		('devs', 'You’ve grown up really good.'),
		],
	'Scene9.3': [
		('devs', 'Nice Victory Royale, scrub.'),
		],
	'Scene10': [
		('MOM', 'Here\'s breakfast. Sit down and eat.'),
		('KID', '(Wow the food tastes like shit)'),
		('', 'Mom notices you’re barely touching your food'),
		('MOM', 'Kid, why aren’t you touching your food?'),
		('MOM', 'Don’t you know I worked hard '),
		('MOM', 'to cook that for you?'),
		],
	'Scene10.1': [
		('SELF', 'Sorry Mom, I was just spacing out is all'),
		('MOM', 'Okay, hurry up the bus is here.'),
		],
	'Scene10.2': [
		('SELF', 'Oh the bus is here, I gotta go Mom sorry.'),
		('SELF', '(quickly eats and bails)'),
		('MOM', 'I woke up early in the morning for this'),
		('MOM', 'How ungrateful!'),
		],
	'Scene10.3': [
		('SELF', 'Your cooking tastes bad Mom'),
		('MOM', 'Why you ungrateful little shit!!!'),
		('MOM', 'Get out before I strike you with a broom'),
		('devs', 'You get out of the house immediately'),
		],
	'Scene11': [
		('devs', 'After 30 minutes in the classroom...'),
		('SELF', 'Man, our teacher is probably absent again.'),
		('SELF', 'I’m so tired of this. I\'m out'),
		('SELF', 'but where should I go though?'),
		],
	'Scene11.1': [
		('SELF', 'I should just chill at the rooftop for a bit'),
		],
	'Scene12': [
		('devs', 'While going up the stairs you found something'),
		('SELF', 'What’s this? A TWICE... Album?'),
		('devs', 'TWICE album added to inventory.'),
		('SELF', 'They look cute,'),
		('SELF', 'I should probably keep this for later.'),
		],
	'Scene13': [
		('SELF', 'Ahh, it’s always relaxing here.'),
		('SELF', 'I’m gonna take a short nap.'),
		('devs', 'After a few hours...'),
		('SELF', 'Wow I think I overslept.'),
		('devs', 'You check your phone to discover'),
		('devs', 'that you have 6 missed calls from Mom'),
		('SELF', 'Crap, Mom’s gonna kill me.'),
		('SELF', 'I better get home ASAP.'),
		],
	'Scene14': [
		('devs', 'While running through the hallway,'),
		('devs', 'you notice some commotion going on outside'),
		('devs', 'Apparently, someone jumped off the building'),
		('SELF', 'What’s with people these days,'),
		('SELF', 'doing all sorts of stupid things'),
		('devs', 'You shrug it off as you see someone'),
		('devs', 'crying while looking up at a poster,'),
		('devs', 'but you are in a hurry.'),
		('devs', 'Do you decide to stop and look at it'),
		('devs', 'or continue running?'),
		],
	'Scene14.1': [
		('SELF', 'It should only take a sec.'),
		('SELF', '"Psalm 23:4"'),
		('devs', 'You read the poster.'),
		],
	'Scene14.2': [
		('devs', 'You continue on outside the school'),
		],
	'Scene15': [
		('devs', 'While waiting for a bus,'),
		('devs', 'you noticed a parcel beside you.'),
		('devs', 'You looked inside the parcel and you saw'),
		('devs', 'a flash drive, a white brick, and soup'),
		('devs', 'You only have space for one of these.'),
		('devs', 'Which will you take?'),
		],
	'Scene15.1': [
		('devs', 'The bus arrives, and you get in and go home'),
		('devs', 'FLASH DRIVE added to inventory.'),
		],
	'Scene15.1.1': [
		('devs', 'After a long day, you decide to hit the hay'),
		('devs', 'However, this night was a unique one.'),
		('SELF', 'I feel kind of weird.'),
		('SELF', 'You can’t really sleep,'),
		('SELF', 'what should you do?'),
		],
	'Scene15.1.1.1': [
		('SELF', 'I should probably check'),
		('SELF', 'what was in that flash drive.'),
		('devs', 'You see three items.'),
		('SELF', 'A Bayesian-based email spam filter?'),
		('SELF', 'What the hell is this?'),
		('SELF', 'A DotA 2 game folder?'),
		('SELF', 'I should give this a try sometime...'),
		('SELF', 'Hmm, Tito Badang.mp4...'),
		('devs', 'Plays TitoBadang.mp4'),
		('SELF', 'Oh shit it\'s late, I gotta sleep.'),
		],
	'Scene15.1.1.2': [
		('SELF', 'Oh well, whatever.'),
		('devs', 'You force yourself asleep.'),
		],
	'Scene15.2': [
		('devs', 'The bus arrives, and you get in and go home'),
		('devs', 'WHITE BRICK added to inventory.'),
		],
	'Scene15.2.1': [
		('devs', 'After a long day, you decide to hit the hay'),
		('devs', 'However, this night was a unique one.'),
		('SELF', 'I feel kind of weird.'),
		('SELF', 'You can’t really sleep,'),
		('SELF', 'what should you do?'),
		],
	'Scene15.2.1.1': [
		('SELF', 'I’ll check out that white brick.'),
		('devs', 'Upon inspection, you see that it has'),
		('devs', 'something written on it'),
		('devs', '“BlueAxis’s Coke'),
		('devs', 'You open the bag and smell it'),
		('devs', 'You realize you sniffed some cocaine'),
		('devs', 'You become high as fuck'),
		('SELF', 'You get so high, you pass out.'),
		],
	'Scene15.2.1.2': [
		('SELF', 'Oh well, whatever.'),
		('devs', 'You force yourself asleep.'),
		],
	'Scene15.3': [
		('devs', 'You devour the soup, but suddenly'),
		('devs', 'Your stomach starts to growl insanely'),
		('devs', 'You pass out. RIP.'),
		],
	'Scene11.2': [
		('devs', 'I’ll probably grab some food'),
		('devs', 'at the cafeteria and head home.'),
		],
	'Scene16': [
		('devs', 'You were eating your usual food combo,'),
		('devs', 'pancit canton with 3 pcs of tofu'),
		('SELF', 'I really love this.'),
		('SELF', 'I’ve been eating this ever since'),
		('SELF', 'and I never got tired of it.'),
		('SELF', 'Itadakimasu!'),
		('devs', 'While you were busy enjoying your food,'),
		('devs', 'you weren’t able to notice your mom'),
		('devs', 'calling you through the phone.'),
		('SELF', 'Shit, mom called. I better go home.'),
		],
	'Scene17': [
		('devs', 'You get home and go straight to your room.'),
		('devs', 'But you notice an pianobook on the floor.'),
		('devs', 'You pick it up and out of nowhere'),
		('devs', 'you know how to play the piano.'),
		('devs', 'Amazing, right?'),
		('devs', 'You head to your room to sleep.'),
		],
	'Scene18': [
		('devs', 'You wake up, and notice you have increased'),
		('devs', 'height and mature appearance'),
		('SELF', 'Nani tf, so desu nEEEEE?'),
		('devs', 'Stfu bitch.'),
		('devs', 'As if you were programmed,'),
		('devs', 'you act as if you had'),
		('devs', 'not transformed overnight'),
		('SELF', 'I’m all set.'),
		('SELF', 'Time to go down and get ready for school'),
		('', ''),
		],
	'Scene19': [
		('', 'Upon reaching the kitchen,'),
		('', 'you feel a grumbling pain'),
		('SELF', 'Arghhh!'),
		('', 'You collapse to the floor'),
		],
	'Scene20': [
		('devs', 'The next thing you knew,'),
		('devs', 'you woke up at a hospital'),
		('devs', 'You were face to face with the doctor'),
		('DOC', 'Kid.. I have something to tell you.'),
		('DOC', 'You have cancer.'),
		('DOC', 'Remember all those pancit cantons?'),
		('DOC', 'Yeah, that gave you cancer.'),
		],
	'Scene21': [
		('MOM', 'Wtf, Kid...'),
		('devs', 'Your mom is shocked in disbelief'),
		('devs', 'You both head home right after'),
		],
	'Scene22': [
		('devs', 'Your mind bursts with regret.'),
		('devs', 'Your thoughts are racing'),
		('SELF', 'Why did it have to come to this?'),
		('SELF', 'You spiral to a state of confusion,'),
		('SELF', 'anxiety, and eventually depression'),
		('SELF', 'This was all new to you,'),
		('SELF', 'and the emotional pain'),
		('SELF', 'proved too much to bear'),
		('SELF', 'Why did it have to be me?'),
		],
	'Scene23': [
		('devs', 'During the morning, Mom was'),
		('devs', 'waiting for you to come'),
		('devs', 'down for breakfast,'),
		('MOM', 'I wonder what this child is up to'),
		],
	'Scene23.1': [
		('devs', 'During the morning, Mom was'),
		('devs', 'waiting for you to come'),
		('devs', 'down for breakfast,'),
		('MOM', 'I wonder what this child is up to'),
		],
	'Scene24': [
		('devs', 'Upon opening the door, she sees'),
		('devs', 'your lifeless body dangling'),
		('devs', 'from the ceiling fan. RIP'),
		],
	'Scene25': [
		('devs', 'Upon opening the door, she sees'),
		('devs', 'you fast asleep on your bed.'),
		('MOM', 'Kid, wake up!'),
		('MOM', 'I prepared breakfast for you. '),
		('SELF', ' Oh, I’m sorry mom.'),
		('SELF', 'I’ll be down right away.'),
		('devs', 'Despite being diagnosed with cancer,'),
		('devs', 'you still decide to go'),
		('devs', 'to school like any normal day.'),
		],
	'Scene26': [
		('devs', 'Mom, I’m going to school.'),
		('devs', 'See you later.'),
		('MOM', 'Oh, wait! I haven’t given your lunch ye-'),
		('MOM', '(He seems weird today. I wonder why.)'),
		],
	'Scene27': [
		('devs', 'When you arrive to school,'),
		('devs', 'you were surprised to find'),
		('devs', 'a scientific journal on the ground'),
		('devs', 'You decide to pick it up'),
		('SELF', 'Hmm, this seems interesting...'),
		],
	'Scene27.1.1': [
		('SELF', 'Ugh, he’s absent again...'),
		('SELF', 'Is this teacher for real?!'),
		('SELF', 'Well, I sure wasted my time here.'),
		('SELF', 'I’m just gonna head to my usual spot.'),
		('devs', 'You go out of the classroom'),
		('devs', 'and head to the rooftop'),
		],
	'Scene27.1.2': [
		('devs', 'While crossing the hallway, you see a'),
		('devs', 'bouquet of flowers and candles.'),
		('devs', 'Right at the spot where someone'),
		('devs', 'landed when they jumped.'),
		('SELF', 'I wonder why he did that.'),
		('devs', 'You just shrug it off and'),
		('devs', 'continue to walk off your way.'),
		],
	'Scene27.1.3': [
		('devs', 'While walking up the staircase,'),
		('devs', 'you feel a strange chill'),
		('devs', 'Suddenly, you hear a whisper'),
		('???', '“I will not be the last”'),
		('devs', 'Suddenly, you lose control of your body'),
		('devs', 'as if something had possessed you '),
		('devs', 'You walk towards the rooftop'),
		],
	'Scene27.1.4': [
		('devs', 'Your heart was filled with despair.'),
		('devs', 'You hear voices in your head.'),
		('???', '“Your mom doesn’t love you”'),
		('???', '“You will never know your Father”'),
		('???', '“You’re alone”'),
		('devs', 'As if you were a puppet,'),
		('devs', 'you found yourself standing'),
		('devs', 'on the ledge of the rooftop'),
		('???', '"Take the leap and join me"'),
		('devs', 'You jumped off the building, you died.'),
		],
	'Scene28': [
		('SELF', 'Hmm, I better bring this home'),
		],
	'Scene29': [
		('devs', 'You decide to spend the remaining'),
		('devs', 'hours of the day playing DotA'),
		('SELF', 'You wasted the day but, hey,'),
		('SELF', 'at least you got that +25 MMR'),
		],
	'Scene30': [
		('devs', 'Ahh shit, I almost forgot.'),
		('devs', 'We have exams tomorrow.'),
		('SELF', 'I better study.'),
		('SELF', 'You study for your exams.'),
		('SELF', 'Your mom would be proud.'),
		],
	'Scene31': [
		('SELF', 'You\'re all grown up now, you\'re now,'),
		('SELF', 'taking up college when you remember'),
		('SELF', 'that scientific journal from high school.'),
		('SELF', 'Let me take a look at this...'),
		('SELF', 'You open the scientific journal and'),
		('devs', 'read through its contents'),
		('devs', 'You then stumble upon a'),
		('devs', ' research made by Dr. Saucy'),
		('devs', 'Apparently, it was discovered that'),
		('devs', 'mangos can cure cancer!'),
		('SELF', 'Well shit. I better go find'),
		('devs', 'You set out to go to the Park'),
		('devs', 'to find some mango stalls'),
		],
	'Scene32': [
		('devs', 'You find a vendor selling a '),
		('devs', 'beverage called ‘Mango Graham”'),
		('SELF', 'This looks tasty, I’ll try it.'),
		('devs', 'You bought a Mango Graham'),
		('devs', 'and enjoyed drinking it'),
		('devs', 'While you were drinking, you'),
		('devs', 'overhear a familiar voice.'),
		('SELF', 'That voice sounds...'),
		('SELF', 'Could it be... No it can\'t be.'),
		('devs', 'The voice was starting to leave'),
		('SELF', 'Wait!!!'),
		('devs', 'You rush off to follow the voice.'),
		],
	'Scene33': [
		('devs', 'You finally catch up to the guy'),
		('devs', 'Hey!'),
		('SELF', 'Wait aren’t you…'),
		('devs', 'Kid! I’m Kid!'),
		('devs', 'Are you m-my...'),
		('devs', 'Why yes Kid.'),
		('devs', 'I am your Father.'),
		('SELF', 'Your mom is...'),
		],
	'Scene34': [
		('devs', 'After that horrendous decision of'),
		('devs', 'playing DotA instead of studying'),
		('devs', 'you flunked out of high school and'),
		('devs', 'got a job as a convenience store clerk.'),
		('devs', 'You head downstairs to get to work.'),
		],
	'Scene35': [
		('SELF', 'I\'m heading out to work, Mom.'),
		('MOM', 'Alright, I\'ll see you when you'),
		('MOM', 'get home, okay?'),
		('SELF', 'Yes, mom.'),
		],
	'Scene36': [
		('SELF', 'Agh, another day at work.'),
		('SELF', 'When is this gonna end...'),
		('SELF', 'I just need enough money t-'),
		('PHONE', '*RING RING*'),
		('SELF', 'Hello, welcome to Chili\'s'),
		('SELF', 'What can I do f-'),
		('SELF', 'Ok, ok.'),
		('SELF', 'Yes.'),
		('SELF', 'I\'ll be right there.'),
		],
	'Scene37': [
		('DOC', 'Hello, kid...'),
		('DOC', 'I\'m sorry to say this but...'),
		('DOC', 'Your mom is...'),
		('', ''),
		],
	'InfancyEvolution': [
		('devs', 'Congratulations!'),
		('devs', 'You are now entering Childhood'),
		],
	'InfancyEvolCheck': [
		('', ''),

		],
	'ChildhoodEvolution1': [
		('devs', 'Congratulations!'),
		('devs', 'You are now entering TeenageHood'),
		],
	'ChildhoodEvolution2': [
		('devs', 'Congratulations!'),
		('devs', 'You are now entering TeenageHood'),
		],
	'ChildEvolCheck': [
		('', ''),

		],
	'TeenagehoodEvolution': [
		('devs', 'Congratulations!'),
		('devs', 'You are now entering Adulthood'),
		],
	'TeenagehoodEvolCheck': [
		('', ''),
		],

	}

# A dictionary of the choices in activeScene
# Key:value format, key is scene name while value is a tuple with 3 elements
# Tuple's format is (choice1, choice2, choice3) from top to bottom
choice_texts = {
	'dScene1': ('Move aggresively', 'Feel surroundings', 'Go apeshit'), # A
	'dScene2': ('Yes', 'No', 'Let devs choose'), # A
	'dScene6': ('Cry', 'Puke', 'Shit'), # B
	'dScene9': ('Go back to sleep', 'Get breakfast', 'Play some Fortnite'), # A
	'dScene10': ('Eat everything', 'Leave and go to school', 'Be honest'), # B
	'dScene11': ('Go to Rooftop', 'Go to Cafeteria', 'Let devs choose'), # A
	'dScene14': ('Look', 'Ignore', 'Let devs choose'), # 
	'dScene15': ('Flash drive', 'White brick', 'Soup'),
	'dScene15.1.1': ('Check flash drive', 'Sleep', 'Let devs choose'),
	'dScene15.2.1': ('Check white brick', 'Sleep', 'Let devs choose'),
	'dScene27': ('Put in your bag', 'Bring home', 'Let devs choose'),
	'dScene28': ('Play DotA', 'Study', 'Let devs choose'),

	'GameOver': ('Back to start', '-', '-'),
	 }

# A list of previous the previous scenes, the last element is the latest scene
previous_scenes = []
save_checker = []
previous_save_1 = []
previous_save_2 = []
previous_save_3 = []
previous_save_4 = []
previous_save_5 = []
previous_save_6 = []
previous_save_7 = []
previous_save_8 = []
previous_save_9 = []
previous_save_10 = []

# Should be a dictionary where there are some special interactions in a scene
# Will find a way to interact with this
oddities = {}

pygame.init()
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Kimi no Mama')
gameIcon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(gameIcon)
pygame.mixer.init()
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

	def load(self):
		return self.image

	def center(self):
		self.imageRect.center = (self.display_width/2, self.display_height/2)
		gameDisplay.blit(self.image, self.imageRect)

	def midtop(self):
		self.imageRect.midtop = (self.display_width/2, self.pos_y)
		gameDisplay.blit(self.image, self.imageRect)

	def midleft(self):
		self.imageRect.midleft = (self.pos_x, self.pos_y)
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
		#a = pygame.mixer.Sound('pop.mp3')
		#b = pygame.mixer.Sound('H1.mp3')
		#a.play()
		#b.play()
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

class Button:

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
		buttonRect = renderImage(self.image, self.image_type, self.pos_x, self.pos_y).load().get_rect()
		buttonRect.topleft = (self.pos_x, self.pos_y)

		if buttonRect.collidepoint(mouse_position):
			renderImage('hover' + self.image, self.image_type, self.pos_x, self.pos_y).coordinates()
			if left_click and self.action:
				renderImage(self.image, self.image_type, self.pos_x, self.pos_y).coordinates()
				string_to_callable(scene_types.get(self.action))(self.action).execute()
			return True

		else:
			renderImage(self.image, self.image_type, self.pos_x, self.pos_y).coordinates()
			return False

	def simple(self):

		mouse_position = pygame.mouse.get_pos()
		left_click = pygame.mouse.get_pressed()[0]

		buttonRect = renderImage(self.image, self.image_type, self.pos_x, self.pos_y).load().get_rect()
		buttonRect.midleft = (self.pos_x, self.pos_y)

		if buttonRect.collidepoint(mouse_position):
			renderImage('hover' + self.image, self.image_type, self.pos_x, self.pos_y).midleft()
			if left_click and self.action:
				self.action()
			return True

		else:
			renderImage(self.image, self.image_type, self.pos_x, self.pos_y).midleft()
			return False

class Screen:

	def __init__(self, scene_name = ''):

		self.game_quit = False
		self.scene_name = scene_name
		self.next_scene = nexts.get(self.scene_name)
		self.background = scenery.get(self.scene_name)
		self.speaker = character.get(self.scene_name)
		self.char_name_pos_x = 195
		self.char_name_pos_y = 550
		self.char_pos_x = 500
		self.char_pos_y = 150
		self.text_pos_x = 150
		self.panel_pos_y = panel_pos_y
		self.color = gray
		self.color_speaker = gray
		self.dialog_text_size = 37
		self.speaker_text_size = 35
		self.item_pos_x = 80
		self.save_pos_x = 180
		self.save_pos_y = 120
		self.item_pos_y = 95
		self.item_offset = 70
		self.menu_panel_y = 30
		self.speaker_font = 'RobotoMono-Italic'
		self.dialog_box = 'dialog_panel'

	def button(self):
		Button(1205, 50, 'menu', god_menu, 'buttons/', 50, 50).simple()
		Button(self.item_pos_x, self.item_pos_y, item_buttons[0], item_use).simple()
		Button(self.item_pos_x + self.item_offset, self.item_pos_y, item_buttons[1], item_use).simple()
		Button(self.item_pos_x + 2*self.item_offset, self.item_pos_y, item_buttons[2], item_use).simple()
		Button(self.item_pos_x + 3*self.item_offset, self.item_pos_y, item_buttons[3], item_use).simple()
		Button(self.item_pos_x + 4*self.item_offset, self.item_pos_y, item_buttons[4], item_use).simple()
		Button(self.item_pos_x + 5*self.item_offset, self.item_pos_y, item_buttons[5], item_use).simple()
		Button(self.item_pos_x + 6*self.item_offset, self.item_pos_y, item_buttons[6], item_use).simple()
		Button(self.item_pos_x + 7*self.item_offset, self.item_pos_y, item_buttons[7], item_use).simple()
		Button(self.item_pos_x + 8*self.item_offset, self.item_pos_y, item_buttons[8], item_use).simple()
		Button(self.item_pos_x + 9*self.item_offset, self.item_pos_y, 'button_gray', item_use).simple()

	def menu_buttons(self):

		Button(551, self.menu_panel_y + 115, 'load-save', save_func, 'buttons/', 189, 48).simple()
		Button(551, self.menu_panel_y + 195, 'menu_quit', game_quit, 'buttons/', 189, 48).simple()

	def save_buttons(self):
		Button(self.save_pos_x, self.save_pos_y, buttons[1], Save().saveslot1).simple()
		Button(self.save_pos_x + self.item_offset, self.save_pos_y, buttons[1], Save().saveslot2).simple()
		Button(self.save_pos_x + 2*self.item_offset, self.save_pos_y, buttons[1], Save().saveslot3).simple()
		Button(self.save_pos_x + 3*self.item_offset, self.save_pos_y, buttons[1], Save().saveslot4).simple()
		Button(self.save_pos_x + 4*self.item_offset, self.save_pos_y, buttons[1], Save().saveslot5).simple()
		Button(self.save_pos_x + 5*self.item_offset, self.save_pos_y, buttons[1], Save().saveslot6).simple()
		Button(self.save_pos_x + 6*self.item_offset, self.save_pos_y, buttons[1], Save().saveslot7).simple()
		Button(self.save_pos_x + 7*self.item_offset, self.save_pos_y, buttons[1], Save().saveslot8).simple()
		Button(self.save_pos_x + 8*self.item_offset, self.save_pos_y, buttons[1], Save().saveslot9).simple()
		Button(self.save_pos_x + 9*self.item_offset, self.save_pos_y, buttons[1], Save().saveslot10).simple()

	def load_buttons(self):
		Button(self.item_pos_x, self.item_pos_y, buttons[1], Load().loadslot1).simple()
		Button(self.item_pos_x + self.item_offset, self.item_pos_y, buttons[1], Load().loadslot2).simple()
		Button(self.item_pos_x + 2*self.item_offset, self.item_pos_y, buttons[1], Load().loadslot3).simple()
		Button(self.item_pos_x + 3*self.item_offset, self.item_pos_y, buttons[1], Load().loadslot4).simple()
		Button(self.item_pos_x + 4*self.item_offset, self.item_pos_y, buttons[1], Load().loadslot5).simple()
		Button(self.item_pos_x + 5*self.item_offset, self.item_pos_y, buttons[1], Load().loadslot6).simple()
		Button(self.item_pos_x + 6*self.item_offset, self.item_pos_y, buttons[1], Load().loadslot7).simple()
		Button(self.item_pos_x + 7*self.item_offset, self.item_pos_y, buttons[1], Load().loadslot8).simple()
		Button(self.item_pos_x + 8*self.item_offset, self.item_pos_y, buttons[1], Load().loadslot9).simple()
		Button(self.item_pos_x + 9*self.item_offset, self.item_pos_y, buttons[1], Load().loadslot10).simple()

class passiveScene(Screen):

	def __init__(self, scene_name = ''):

		Screen.__init__(self, scene_name)
		self.scene_done = False
		self.line = 0
		self.next_type = string_to_callable(scene_types.get(self.next_scene))
		previous_scenes.append(scene_name)

	def execute(self):

		gameDisplay.fill(self.color)
		renderImage(self.background, 'scenery/').center()
		if self.speaker:
			renderImage(self.speaker, 'character/', 0, self.char_pos_y).midtop()
		renderImage(self.dialog_box, '', 0, self.panel_pos_y).midtop()
		renderImage('inventory', 'buttons/', 50, 75).midleft()
		while not self.game_quit:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						pygame.quit()
						quit()
				elif event.type == pygame.QUIT:
					pygame.quit()
					quit()
				elif event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1 and pygame.mouse.get_pos()[1] > 75 or pygame.mouse.get_pos()[0] < 25:
						renderImage(self.background, 'scenery/').center()
						if self.speaker:
							renderImage(self.speaker, 'character/', 0, self.char_pos_y).midtop()
						renderImage(self.dialog_box, '', 0, self.panel_pos_y).midtop()
						renderImage('inventory', 'buttons/', 50, 75).midleft()
						self.line += 1
						if self.line == len(dialogue.get(self.scene_name)):
							self.next_type(self.next_scene).execute()
						self.scene_done = False
				#pygame.display.update()
			self.speaker_name, self.text_list = dialogue.get(self.scene_name)[self.line]
			Screen.button(self)
			pygame.display.update()
			if not self.scene_done:
				#Screen.button(self)
				displayText(self.speaker_name, 0, self.speaker_text_size, self.color_speaker, self.char_name_pos_x, self.char_name_pos_y, self.speaker_font).passivecenter()
				displayText('ITEMS', 0, self.speaker_text_size, self.color_speaker, 133, 40, self.speaker_font).passivecenter()
				displayText(self.text_list, self.line, self.dialog_text_size, self.color, self.text_pos_x, 0).active_panel()
				self.scene_done = True
				continue
			else:
				renderImage(self.background, 'scenery/').center()
				Screen.button(self)
				if self.speaker:
					renderImage(self.speaker, 'character/', 0, self.char_pos_y).midtop()
				renderImage(self.dialog_box, '', 0, self.panel_pos_y).midtop()
				renderImage('inventory', 'buttons/', 50, 75).midleft()
				displayText(self.speaker_name, 0, self.speaker_text_size, self.color_speaker, self.char_name_pos_x, self.char_name_pos_y, self.speaker_font).passivecenter()
				displayText('ITEMS', 0, self.speaker_text_size, self.color_speaker, 133, 40, self.speaker_font).passivecenter()
				displayText(self.text_list, self.line, self.dialog_text_size, self.color, self.text_pos_x, 0).passive_panel()
				#Screen.button(self)
				self.scene_done = True
				pygame.display.update()
				continue
			pygame.display.update()
			clock.tick(60)

class activeScene(Screen):

	def __init__(self, scene_name = ''):

		Screen.__init__(self, scene_name)
		self.oddity = oddities.get(scene_name)
		self.choices = choice_texts.get(self.scene_name)
		self.char_pos_x += 200
		self.button_pos_x = 250
		self.button_pos_y = 310
		self.button_offset_x = 70
		self.button_offset_y = 24
		self.start_pos_x = 535
		self.start_pos_y = 470
		self.start_offset_y = 70
		self.color = white
		previous_scenes.append(scene_name)

	def game_start(self):

		gameDisplay.fill(self.color)
		renderImage('start_background', 'scenery/').center()
		pygame.mixer.music.load('H2.mp3')
		pygame.mixer.music.play(-1)

		while not self.game_quit:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						pygame.quit()
						quit()
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			Button(self.start_pos_x, self.start_pos_y, start_buttons[0], 'Scene0').aScene()
			Button(self.start_pos_x, self.start_pos_y + self.start_offset_y + 25, start_buttons[1], activeScene().load_slots).simple()
			Button(self.start_pos_x, self.start_pos_y + 2*self.start_offset_y + 25, start_buttons[2], game_quit).simple()
			pygame.display.update()
			clock.tick(60)

	def main_menu(self):

		gameDisplay.fill(self.color)
		renderImage('start_background', 'scenery/').center()
		renderImage(self.dialog_box, '', 0, self.panel_pos_y).midtop()
		displayText('devs', 0, self.speaker_text_size, self.color_speaker, self.char_name_pos_x, self.char_name_pos_y, self.speaker_font).passivecenter()
		displayText('What do you want to do?', 0, self.dialog_text_size, self.color, self.text_pos_x, 0).active_panel()
		renderImage('menu_panel', '', 0, self.menu_panel_y).midtop()
		displayText('MENU', 0, self.speaker_text_size, self.color_speaker, 530, 49, self.speaker_font).passivecenter()
		while not self.game_quit:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						pygame.quit()
						quit()
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			Screen().menu_buttons()
			pygame.display.update()
			clock.tick(60)

	def execute(self):

		gameDisplay.fill(self.color)
		pygame.mixer.music.load('H1.mp3')
		pygame.mixer.music.play(-1)
		renderImage(self.background, 'scenery/').center()
		renderImage('inventory', 'buttons/', 50, 75).midleft()
		Screen.button(self)

		if self.speaker:
			renderImage(self.speaker, 'character/', self.char_pos_x, self.char_pos_y).coordinates()
		if self.oddity:
			renderImage(self.oddity, 'character/', 0, self.char_pos_y).midtop()
		renderImage(self.dialog_box, '', 0, self.panel_pos_y).midtop()
		renderImage('inventory', 'buttons/', 50, 75).midleft()
		displayText('devs', 0, self.speaker_text_size, self.color_speaker, self.char_name_pos_x, self.char_name_pos_y, self.speaker_font).passivecenter()
		displayText('ITEMS', 0, self.speaker_text_size, self.color_speaker, 133, 40, self.speaker_font).passivecenter()
		displayText('Choose your fate Kid', 0, self.dialog_text_size, self.color, self.text_pos_x, 0).active_panel()
		displayText(self.choices[0], 0, self.dialog_text_size, self.color, self.button_pos_x + self.button_offset_x, self.button_pos_y + self.button_offset_y).passivemidleft()
		displayText(self.choices[1], 0, self.dialog_text_size, self.color, self.button_pos_x + self.button_offset_x, self.button_pos_y + self.button_offset_y + 60).passivemidleft()
		displayText(self.choices[2], 0, self.dialog_text_size, self.color, self.button_pos_x + self.button_offset_x, self.button_pos_y + self.button_offset_y + 120).passivemidleft()

		while not self.game_quit:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						pygame.quit()
						quit()
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			Button(self.button_pos_x, self.button_pos_y, buttons[0], self.next_scene[0]).aScene()
			Button(self.button_pos_x, self.button_pos_y + 60, buttons[1], self.next_scene[1]).aScene()
			Button(self.button_pos_x, self.button_pos_y + 120, buttons[2], self.next_scene[2]).aScene()
			Screen.button(self)
			pygame.display.update()
			clock.tick(60)

	def save_slots(self):

		gameDisplay.fill(self.color)
		renderImage('start_background', 'scenery/').center()
		renderImage(self.dialog_box, '', 0, self.panel_pos_y).midtop()
		displayText('devs', 0, self.speaker_text_size, self.color_speaker, self.char_name_pos_x, self.char_name_pos_y, self.speaker_font).passivecenter()
		displayText('What file do you want to access?', 0, self.dialog_text_size, self.color, self.text_pos_x, 0).active_panel()
		while not self.game_quit:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						pygame.quit()
						quit()
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			Screen.save_buttons(self)
			pygame.display.update()
			clock.tick(60)

	def load_slots(self):
		gameDisplay.fill(self.color)
		renderImage('start_background', 'scenery/').center()
		
		renderImage(self.dialog_box, '', 0, self.panel_pos_y).midtop()
		displayText('devs', 0, self.speaker_text_size, self.color_speaker, self.char_name_pos_x, self.char_name_pos_y, self.speaker_font).passivecenter()
		displayText('What do you want to do?', 0, self.dialog_text_size, self.color, self.text_pos_x, 0).active_panel()
		while not self.game_quit:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						pygame.quit()
						quit()
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			Screen.load_buttons(self)
			pygame.display.update()
			clock.tick(60)

savedata = os.listdir('savedata/')
savedibs = []
previoussave = []

class Load:
	def loadslot1(self):
		rabble = savedata[0]
		rabble1 = os.path.join("savedata/",rabble)
		scene_name = pickle.load(open(rabble1, "rb"))
		string_to_callable(scene_types.get(scene_name))(scene_name).execute()

	def loadslot2(self):
		rabble = savedata[1]
		rabble1 = os.path.join("savedata/",rabble)
		scene_name = pickle.load(open(rabble1, "rb"))
		string_to_callable(scene_types.get(scene_name))(scene_name).execute()

	def loadslot3(self):
		rabble = savedata[2]
		rabble1 = os.path.join("savedata/",rabble)
		scene_name = pickle.load(open(rabble1, "rb"))
		string_to_callable(scene_types.get(scene_name))(scene_name).execute()

	def loadslot4(self):
		rabble = savedata[3]
		rabble1 = os.path.join("savedata/",rabble)
		scene_name = pickle.load(open(rabble1, "rb"))
		string_to_callable(scene_types.get(scene_name))(scene_name).execute()

	def loadslot5(self):
		rabble = savedata[4]
		rabble1 = os.path.join("savedata/",rabble)
		scene_name = pickle.load(open(rabble1, "rb"))
		string_to_callable(scene_types.get(scene_name))(scene_name).execute()

	def loadslot6(self):
		rabble = savedata[5]
		rabble1 = os.path.join("savedata/",rabble)
		scene_name = pickle.load(open(rabble1, "rb"))
		string_to_callable(scene_types.get(scene_name))(scene_name).execute()

	def loadslot7(self):
		rabble = savedata[6]
		rabble1 = os.path.join("savedata/",rabble)
		scene_name = pickle.load(open(rabble1, "rb"))
		string_to_callable(scene_types.get(scene_name))(scene_name).execute()


	def loadslot8(self):
		rabble = savedata[7]
		rabble1 = os.path.join("savedata/",rabble)
		scene_name = pickle.load(open(rabble1, "rb"))
		string_to_callable(scene_types.get(scene_name))(scene_name).execute()

	def loadslot9(self):
		rabble = savedata[8]
		rabble1 = os.path.join("savedata/",rabble)
		scene_name = pickle.load(open(rabble1, "rb"))
		string_to_callable(scene_types.get(scene_name))(scene_name).execute()

	def loadslot10(self):
		rabble = savedata[9]
		rabble1 = os.path.join("savedata/",rabble)
		scene_name = pickle.load(open(rabble1, "rb"))
		string_to_callable(scene_types.get(scene_name))(scene_name).execute()


class Save:
	def saveslot1(self):
		now = datetime.datetime.now()
		nowfile = now.isoformat()
		spaces = ''
		current_scene = ''
		truetitle = str(truetime(nowfile)) + ".txt"
		truestitle = os.path.join('savedata/', truetitle)
		pygame.time.delay(200)
		if not 1 in savedibs:
			i = -1
			current_scene = previous_scenes[i]
			while current_scene == '':
				i -= 1
				current_scene = previous_scenes[i] 
			pickle.dump(current_scene, open(truestitle, "wb"))
			previoussave.append(truestitle)
			savedibs.append(1)
			print(savedibs)
			pygame.time.delay(2)
		else:
			try:
				a = previoussave[-1]
				os.remove(a)
			except OSError:
				pass
			pickle.dump(current_scene, open(truestitle, "wb"))	
			print("done")

	def saveslot2(self):
		now = datetime.datetime.now()
		nowfile = now.isoformat()
		spaces = ''
		current_scene = ''
		truetitle = str(truetime(nowfile)) + ".txt"
		truestitle = os.path.join('savedata/', truetitle)
		pygame.time.delay(200)
		if not 2 in savedibs:
			i = -1
			current_scene = previous_scenes[i]
			while current_scene == '':
				i -= 1
				current_scene = previous_scenes[i] 
			pickle.dump(current_scene, open(truestitle, "wb"))
			previoussave.append(truestitle)
			savedibs.append(2)
			print(savedibs)
			pygame.time.delay(2)
		else:
			try:
				a = previoussave[-1]
				os.remove(a)
			except OSError:
				pass
			pickle.dump(current_scene, open(truestitle, "wb"))	
			print("done")

	def saveslot3(self):
		now = datetime.datetime.now()
		nowfile = now.isoformat()
		spaces = ''
		current_scene = ''
		truetitle = str(truetime(nowfile)) + ".txt"
		truestitle = os.path.join('savedata/', truetitle)
		pygame.time.delay(200)
		if not 3 in savedibs:
			i = -1
			current_scene = previous_scenes[i]
			while current_scene == '':
				i -= 1
				current_scene = previous_scenes[i] 
			pickle.dump(current_scene, open(truestitle, "wb"))
			previoussave.append(truestitle)
			savedibs.append(3)
			print(savedibs)
			pygame.time.delay(2)
		else:
			try:
				a = previoussave[-1]
				os.remove(a)
			except OSError:
				pass
			pickle.dump(current_scene, open(truestitle, "wb"))	
			print("done")

	def saveslot4(self):
		now = datetime.datetime.now()
		nowfile = now.isoformat()
		spaces = ''
		current_scene = ''
		truetitle = str(truetime(nowfile)) + ".txt"
		truestitle = os.path.join('savedata/', truetitle)
		pygame.time.delay(200)
		if not 4 in savedibs:
			i = -1
			current_scene = previous_scenes[i]
			while current_scene == '':
				i -= 1
				current_scene = previous_scenes[i] 
			pickle.dump(current_scene, open(truestitle, "wb"))
			previoussave.append(truestitle)
			savedibs.append(4)
			print(savedibs)
			pygame.time.delay(2)
		else:
			try:
				a = previoussave[-1]
				os.remove(a)
			except OSError:
				pass
			pickle.dump(current_scene, open(truestitle, "wb"))	
			print("done")

	def saveslot5(self):
		now = datetime.datetime.now()
		nowfile = now.isoformat()
		spaces = ''
		current_scene = ''
		truetitle = str(truetime(nowfile)) + ".txt"
		truestitle = os.path.join('savedata/', truetitle)
		pygame.time.delay(200)
		if not 5 in savedibs:
			i = -1
			current_scene = previous_scenes[i]
			while current_scene == '':
				i -= 1
				current_scene = previous_scenes[i] 
			pickle.dump(current_scene, open(truestitle, "wb"))
			previoussave.append(truestitle)
			savedibs.append(5)
			print(savedibs)
			pygame.time.delay(2)
		else:
			try:
				a = previoussave[-1]
				os.remove(a)
			except OSError:
				pass
			pickle.dump(current_scene, open(truestitle, "wb"))	
			print("done")

	def saveslot6(self):
		now = datetime.datetime.now()
		nowfile = now.isoformat()
		spaces = ''
		current_scene = ''
		truetitle = str(truetime(nowfile)) + ".txt"
		truestitle = os.path.join('savedata/', truetitle)
		pygame.time.delay(200)
		if not 6 in savedibs:
			i = -1
			current_scene = previous_scenes[i]
			while current_scene == '':
				i -= 1
				current_scene = previous_scenes[i] 
			pickle.dump(current_scene, open(truestitle, "wb"))
			previoussave.append(truestitle)
			savedibs.append(6)
			print(savedibs)
			pygame.time.delay(2)
		else:
			try:
				a = previoussave[-1]
				os.remove(a)
			except OSError:
				pass
			pickle.dump(current_scene, open(truestitle, "wb"))	
			print("done")

	def saveslot7(self):
		now = datetime.datetime.now()
		nowfile = now.isoformat()
		spaces = ''
		current_scene = ''
		truetitle = str(truetime(nowfile)) + ".txt"
		truestitle = os.path.join('savedata/', truetitle)
		pygame.time.delay(200)
		if not 7 in savedibs:
			i = -1
			current_scene = previous_scenes[i]
			while current_scene == '':
				i -= 1
				current_scene = previous_scenes[i] 
			pickle.dump(current_scene, open(truestitle, "wb"))
			previoussave.append(truestitle)
			savedibs.append(7)
			print(savedibs)
			pygame.time.delay(2)
		else:
			try:
				a = previoussave[-1]
				os.remove(a)
			except OSError:
				pass
			pickle.dump(current_scene, open(truestitle, "wb"))	
			print("done")


	def saveslot8(self):
		now = datetime.datetime.now()
		nowfile = now.isoformat()
		spaces = ''
		current_scene = ''
		truetitle = str(truetime(nowfile)) + ".txt"
		truestitle = os.path.join('savedata/', truetitle)
		pygame.time.delay(200)
		if not 8 in savedibs:
			i = -1
			current_scene = previous_scenes[i]
			while current_scene == '':
				i -= 1
				current_scene = previous_scenes[i] 
			pickle.dump(current_scene, open(truestitle, "wb"))
			previoussave.append(truestitle)
			savedibs.append(8)
			print(savedibs)
			pygame.time.delay(2)
		else:
			try:
				a = previoussave[-1]
				os.remove(a)
			except OSError:
				pass
			pickle.dump(current_scene, open(truestitle, "wb"))	
			print("done")

	def saveslot9(self):
		now = datetime.datetime.now()
		nowfile = now.isoformat()
		spaces = ''
		current_scene = ''
		truetitle = str(truetime(nowfile)) + ".txt"
		truestitle = os.path.join('savedata/', truetitle)
		pygame.time.delay(200)
		if not 9 in savedibs:
			i = -1
			current_scene = previous_scenes[i]
			while current_scene == '':
				i -= 1
				current_scene = previous_scenes[i] 
			pickle.dump(current_scene, open(truestitle, "wb"))
			previoussave.append(truestitle)
			savedibs.append(9)
			print(savedibs)
			pygame.time.delay(2)
		else:
			try:
				a = previoussave[-1]
				os.remove(a)
			except OSError:
				pass
			pickle.dump(current_scene, open(truestitle, "wb"))	
			print("done")

	def saveslot10(self):
		now = datetime.datetime.now()
		nowfile = now.isoformat()
		spaces = ''
		current_scene = ''
		truetitle = str(truetime(nowfile)) + ".txt"
		truestitle = os.path.join('savedata/', truetitle)
		pygame.time.delay(200)
		if not 10 in savedibs:
			i = -1
			current_scene = previous_scenes[i]
			while current_scene == '':
				i -= 1
				current_scene = previous_scenes[i] 
			pickle.dump(current_scene, open(truestitle, "wb"))
			previoussave.append(truestitle)
			savedibs.append(10)
			print(savedibs)
			pygame.time.delay(2)
		else:
			try:
				a = previoussave[-1]
				os.remove(a)
			except OSError:
				pass
			pickle.dump(current_scene, open(truestitle, "wb"))	
			print("done")



class oddScene(Screen):

	def __init__(self, scene_name):

		Screen.__init__(self, scene_name)
		self.scene_done = False
		self.line = 0
		self.next_type = string_to_callable(scene_types.get(self.next_scene))
		previous_scenes.append(scene_name)

	def credits(self):

		gameDisplay.fill(self.color)
		renderImage(self.background, 'scenery/').center()

def truetime(filename):
	return filename.replace(':', '-').replace('T', ' ')

def item_use():

	main()

def save_func():

	activeScene().save_slots()

def god_menu():

	activeScene().main_menu()

def game_quit():

	pygame.quit()
	quit()

def main():

	activeScene('GameOver').execute()()
	pygame.quit()
	quit()

if __name__ == '__main__':
	main()