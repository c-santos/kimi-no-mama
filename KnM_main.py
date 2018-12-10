import pygame
import pickle

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
buttons = ('button_blue', 'button_green', 'button_orange')
start_buttons = ('new_game', 'load_game', 'quit')

# A dicionary of scene names and the type of scene
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
	'InfancyEvolution': 'passiveScene',  # EVOL SCENE

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
		'Scene11.1': 'passiveScene', #  ROOFTOP SCENE
			'Scene12': 'passiveScene',
			'Scene13': 'passiveScene',
			'Scene14': 'passiveScene',
			'dScene14': 'activeScene',# POSTER SCENE
				'Scene14.1': 'passiveScene',
				'Scene14.2': 'passiveScene',
			'Scene15': 'passiveScene',
			'dScene15': 'activeScene', #  BUS STOP SCENE
				'Scene15.1': 'passiveScene', #  USB
					'Scene15.1.1': 'passiveScene',
						'dScene15.1.1': 'activeScene', # CHECK OR SLEEP
							'Scene15.1.1.1': 'passiveScene',
							'Scene15.1.1.2': 'passiveScene',
				'Scene15.2': 'passiveScene', #  COKE
					'Scene15.2.1': 'passiveScene',
						'dScene15.2.1': 'activeScene', # CHECK OR SLEEP
							'Scene15.2.1.1': 'passiveScene',
							'Scene15.2.1.2': 'passiveScene',
				'Scene15.3': 'passiveScene', #  SOUP

		'Scene11.2': 'passiveScene', #  CAFETERIA SCENE
		'Scene16': 'passiveScene',
		'Scene17': 'passiveScene',
	'ChildhoodEvolution': 'passiveScene', # EVOL SCENE



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
			'dScene14': ('Scene14.1', 'Scene14.2', ''),  # POSTER SCENE
				'Scene14.1': 'Scene15',
				'Scene14.2': 'Scene15',
				'Scene15': 'dScene15',
					'dScene15': ('Scene15.1', 'Scene15.2', 'Scene15.3'), #  BUS STOP SCENE
						'Scene15.1': 'Scene15.1.1',
							'Scene15.1.1': 'dScene15.1.1',
								'dScene15.1.1': ('Scene15.1.1.1', 'Scene15.1.1.2', ''), #  USB
									'Scene15.1.1.1': 'ChildhoodEvolution',
									'Scene15.1.1.2': 'ChildhoodEvolution',
						'Scene15.2': 'Scene15.2.1',
							'Scene15.2': 'dScene15.2.1',
								'dScene15.2.1': ('Scene15.2.1.1', 'Scene15.2.1.2', ''), #  coke
									'Scene15.2.1.1': 'ChildhoodEvolution',
									'Scene15.2.1.2': 'ChildhoodEvolution',
						'Scene15.3': 'GameOver', #  SOUP

		'Scene11.2': 'Scene16', #  CAFETERIA SCENE
		'Scene16': 'Scene17',
		'Scene17': 'ChildhoodEvolution',



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
	'ChildhoodEvolution': 'dark_background', # EVOL SCENE


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
	'InfancyEvolution': '',  # TRANSMOD ASSET

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
			'Scene12': '',  # TWICE ALBUM COVER
			'Scene13': '',
			'Scene14': '',
			'dScene14': '',# POSTER ASSET
				'Scene14.1': '',
				'Scene14.2': '',
			'Scene15': '',
			'dScene15': '', #  BUS STOP SCENE
				'Scene15.1': '', #  USB ASSET
					'Scene15.1.1': '',
						'dScene15.1.1': '', # CHECK OR SLEEP
							'Scene15.1.1.1': '',
							'Scene15.1.1.2': '',
				'Scene15.2': 'bedroom-dusk', #  WHITE BRICK ASSET
					'Scene15.2.1': 'bedroom-dusk',
						'dScene15.2.1': 'bedroom-dusk', # CHECK OR SLEEP
							'Scene15.2.1.1': 'bedroom-night',
							'Scene15.2.1.2': 'bedroom-night',
				'Scene15.3': 'dark_background', #  SOUP ASSET

		'Scene11.2': 'classroom', #  CAFETERIA SCENE
		'Scene16': 'cafeteria',
		'Scene17': 'living-dusk', # MUSIC BOOK ASSET
		'ChildhoodEvolution': 'dark_background', # EVOL SCENE


	'GameOver': '',
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
		('devs', 'should be an enter name prompt'),
		('', 'Oof.'),
		('SELF', 'I still don’t know where I am...'),
		('SELF', 'But it seems like I\'m inside a cave.'),
		('SELF', 'There must be a way out...'),
		], 
	'Scene1.1': [
		('', 'It’s as if you’re inside an elastic cage...'),
		('', 'Wait, what’s that? You hear a muffled voice...'),
		('???', 'I\'m going to see you real soon, Kid'),
		('', 'For some reason, you remember the voice'),
		('SELF', 'Man, that was tiring. Let me just sleep.'),
		],
	'Scene1.2': [
		('', 'You tried to feel but the surroundings'),
		('', 'don’t have the same feelings for you.'),
		('', 'This is so sad.'),
		('', 'Alexa might know what to do.'),
		],
	'Scene1.3': [
		('', 'As you shadow boxed around the area,'), 
		('', 'you became more aware of your surroundings.'),
		('', 'It seems like you’re trapped'),
		('', 'in some kind of elastic cage...'),
		('', 'Just outside the cave,'),
		('', 'you hear somebody moan...'),
		('???', 'Ugh, that hurts... fuck!'),
		('', 'For some reason, you died.'),
		('', 'We won’t tell you how though.'),
		('', 'Next time, don’t be a small brain.'),
		],
	'Scene2': [
		('', 'Suddenly, a flash of light appears.'), 
		('', 'You see a hole.'),
		('SELF', 'It must be the exit!'),
		('SELF', 'But should I really go that way?'),
		],
	'Scene2.1': [
		('', 'For some reason, you died.'), 
		('', 'You’ll never know what’s on the other side.'),
		('', 'You’ll get it next time buddy.'),
		],
	'Scene3': [
		('', 'As you were nearing the blinding light,'),
		('', 'you finally realized what was happening.'),
		('', 'You’re a baby!'),
		('', 'What do you think your gender should be?'),
		('devs', 'Sike!'),
		('devs', 'We already assumed your gender, sorry.'),
		('SELF', 'Isn\'t that kind of sexist...'),
		('devs', 'Fly away you little shit.'),
		('devs', 'By the way, good luck dealing with your mom.'),
		('', ''),
		],
	'Scene4': [
		('DOCTOR', 'Congratulations, Ma\'am, it was successful'),
		('DOCTOR', 'and it’s a baby boy!'),
		('DOCTOR', 'Good luck on your motherhood.'),
		('', 'As the screen fades to black,'),
		('', 'you see that devilish smile of hers.'),
		('', 'But she doesn’t know what’s coming.'),
		('', 'Good luck to her indeed.'),
		],
	'Scene5': [
		('', 'After two months...'),
		],
	'Scene6': [
		('SELF', 'It’s been two months and this old woman'),
		('SELF', 'right here is still baby talking you.'),
		('SELF', 'She wants stupid? Show her stupid.'),
		],
	'Scene6.1': [
		('', '(+1 XP) Good thing you learned how to cry!'),
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
		('', 'As the night deepens, your mom falls asleep'),
		('', 'while caressing you.'),
		('', 'You close your eyes and get ready'),
		('', 'for the future days to come.'),
		],
	'InfancyEvolution': [
		('', ''),
		('', ''),
		('', ''),
		('', ''),
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
		('', 'And that was the last time you fell asleep.'),
		],
	'Scene9.2': [
		('', '(+20 life exp) You’ve grown up really good.'),
		],
	'Scene9.3': [
		('', '(+15 life experience) for being awesome.'),
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
		('', 'You earned +10 life xp'),
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
		('', 'You get out of the house immediately'),
		],
	'Scene11': [
		('', 'After 30 minutes in the classroom...'),
		('SELF', 'Man, our teacher is probably absent again.'),
		('SELF', 'I’m so tired of this. I\'m out'),
		('SELF', 'but where should I go though?'),
		],
	'Scene11.1': [
		('SELF', 'I should just chill at the rooftop for a bit'),
		],
	'Scene12': [
		('', 'While going up the stairs you found something'),
		('SELF', 'What’s this? A TWICE... Album?'),
		('', 'TWICE album added to inventory.'),
		('SELF', 'They look cute,'),
		('SELF', 'I should probably keep this for later.'),
		('', 'You earned +15 life exp.'),
		],
	'Scene13': [
		('SELF', 'Ahh, it’s always relaxing here.'),
		('SELF', 'I’m gonna take a short nap.'),
		('', 'After a few hours...'),
		('SELF', 'Wow I think I overslept.'),
		('', 'You check your phone to discover'),
		('', 'that you have 6 missed calls from Mom'),
		('SELF', 'Crap, Mom’s gonna kill me.'),
		('SELF', 'I better get home ASAP.'),
		],
	'Scene14': [
		('', 'While running through the hallway,'),
		('', 'you notice some commotion going on outside'),
		('', 'Apparently, someone  jumped off the building'),
		('SELF', 'What’s with people these days,'),
		('SELF', 'doing all sorts of stupid things'),
		('', 'You shrug it off as you see someone'),
		('', 'crying while looking up at a poster,'),
		('', 'but you are in a hurry.'),
		('', 'Do you decide to stop and look at it'),
		('', 'or continue running?'),
		],
	'Scene14.1': [
		('SELF', 'It should only take a sec.'),
		('SELF', '"Psalm 23:4"'),
		('', 'You read the poster and earn +20 XP.'),
		],
	'Scene14.2': [
		('', 'You continue on outside the school'),
		],
	'Scene15': [
		('', 'While waiting for a bus,'),
		('', 'you noticed a parcel beside you.'),
		('', 'You looked inside the parcel and you saw'),
		('', 'a flash drive, a white brick, and soup'),
		('', 'You only have space for one of these.'),
		('', 'Which will you take?'),
		],
	'Scene15.1': [
		('', 'The bus arrives, and you get in and go home'),
		],
	'Scene15.1.1': [
		('', 'After a long day, you decide to hit the hay'),
		('', 'However, this night was a unique one.'),
		('SELF', 'I feel kind of weird.'),
		('SELF', 'You can’t really sleep,'),
		('SELF', 'what should you do?'),
		],
	'Scene15.1.1.1': [
		('SELF', 'I should probably check'),
		('SELF', 'what was in that flash drive.'),
		('', 'You see three items.'),
		('SELF', 'A Bayesian-based email spam filter?'),
		('SELF', 'What the hell is this?'),
		('', '+15 XP'),
		('SELF', 'A DotA 2 game folder?'),
		('SELF', 'I should give this a try sometime...'),
		('', '+15 XP'),
		('SELF', 'Hmm, Tito Badang.mp4...'),
		('', 'Plays TitoBadang.mp4'),
		('', '+60 XP'),
		('SELF', 'Oh shit it\'s late, I gotta sleep.'),
		],
	'Scene15.1.1.2': [
		('SELF', 'Oh well, whatever.'),
		('', 'You force yourself asleep.'),
		],
	'Scene15.2': [
		('', 'The bus arrives, and you get in and go home'),
		],
	'Scene15.2.1': [
		('', 'After a long day, you decide to hit the hay'),
		('', 'However, this night was a unique one.'),
		('SELF', 'I feel kind of weird.'),
		('SELF', 'You can’t really sleep,'),
		('SELF', 'what should you do?'),
		],
	'Scene15.2.1.1': [
		('SELF', 'I’ll check out that white brick.'),
		('', 'Upon inspection, you see that it has'),
		('', 'something written on it'),
		('', '“BlueAxis’s Coke'),
		('', 'You open the bag and smell it'),
		('', 'You realize you sniffed some cocaine'),
		('', 'You become high as fuck'),
		('', '+90 XP'),
		('SELF', 'You get so high, you pass out.'),
		],
	'Scene15.2.1.2': [
		('SELF', 'Oh well, whatever.'),
		('', 'You force yourself asleep.'),
		('', ''),
		('', ''),
		],
	'Scene15.3': [
		('', 'You devour the soup, but suddenly'),
		('', 'Your stomach starts to growl insanely'),
		('', 'You pass out. RIP.'),
		],
	'Scene11.2': [
		('', 'I’ll probably grab some food'),
		('', 'at the cafeteria and head home.'),
		('', ''),
		('', ''),
		],
	'Scene16': [
		('', 'You were eating your usual food combo,'),
		('', 'pancit canton with 3 pcs of tofu'),
		('SELF', 'I really love this.'),
		('SELF', 'I’ve been eating this ever since'),
		('SELF', 'and I never got tired of it.'),
		('SELF', 'Itadakimasu!'),
		('', 'While you were busy enjoying your food,'),
		('', 'you weren’t able to notice your mom'),
		('', 'calling you through the phone.'),
		('SELF', 'Shit, mom called. I better go home.'),
		],
	'Scene17': [
		('', 'You get home and go straight to your room.'),
		('', 'But you notice an pianobook on the floor.'),
		('', 'You pick it up and out of nowhere'),
		('', 'you know how to play the piano.'),
		('devs', 'Amazing, right?'),
		('', 'You head to your room to sleep.'),
		],
	'ChildhoodEvolution': [
		('', ''),
		('', ''),
		('', ''),
		('', ''),
		],
	'InfancyEvolution': [
		('', ''),
		('', ''),
		('', ''),
		('', ''),
		],

	}

# A dictionary of the choices in activeScene
# Key:value format, key is scene name while value is a tuple with 3 elements
# Tuple's format is (choice1, choice2, choice3) from top to bottom
choice_texts = {
	'dScene1': ('Move aggresively', 'Feel surroundings', 'Go apeshit'),
	'dScene2': ('Yes', 'No', '-'),
	'dScene6': ('Cry Scene6.1', 'Puke Scene6.2', 'Shit Scene6.3'),
	'dScene9': ('Go back to sleep', 'Get breakfast', 'Play some Fortnite'),
	'dScene10': ('Eat everything', 'Leave and go to school', 'Be honest'),
	'dScene11': ('Go to Rooftop', 'Go to Cafeteria', ''),
	'dScene14': ('Look', 'Ignore', ''),
	'dScene15': ('Flash drive', 'White brick', 'Soup'),
	'dScene15.1.1': ('Check flash drive', 'Sleep', ''),
	'dScene15.2.1': ('Check white brick', 'Ignore', ''),

	'GameOver': ('Back to start', '', ''),
	 }

# A list of previous the previous scenes, the last element is the latest scene
previous_scenes = []

# Should be a dictionary where there are some special interactions in a scene
# Will find a way to interact with this
oddities = {}

pygame.init()
gameDisplay = pygame.display.set_mode((display_width,display_height), pygame.FULLSCREEN)
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
		self.item_pos_y = 95
		self.item_offset = 70
		self.menu_panel_y = 30
		self.speaker_font = 'RobotoMono-Italic'
		self.dialog_box = 'dialog_panel'

	def button(self):
		Button(1205, 50, 'menu', god_menu, 'buttons/', 50, 50).simple()
		#Button(930,50, 'menu', save, 'buttons/', 50,50).simple()
		Button(self.item_pos_x, self.item_pos_y, buttons[1], item_use).simple()
		Button(self.item_pos_x + self.item_offset, self.item_pos_y, buttons[1], item_use).simple()
		Button(self.item_pos_x + 2*self.item_offset, self.item_pos_y, buttons[1], item_use).simple()
		Button(self.item_pos_x + 3*self.item_offset, self.item_pos_y, buttons[1], item_use).simple()
		Button(self.item_pos_x + 4*self.item_offset, self.item_pos_y, buttons[1], item_use).simple()
		Button(self.item_pos_x + 5*self.item_offset, self.item_pos_y, buttons[1], item_use).simple()
		Button(self.item_pos_x + 6*self.item_offset, self.item_pos_y, buttons[1], item_use).simple()
		Button(self.item_pos_x + 7*self.item_offset, self.item_pos_y, buttons[1], item_use).simple()
		Button(self.item_pos_x + 8*self.item_offset, self.item_pos_y, buttons[1], item_use).simple()
		Button(self.item_pos_x + 9*self.item_offset, self.item_pos_y, buttons[1], item_use).simple()

	def menu_buttons(self):

		Button(551, self.menu_panel_y + 115, 'load-save', save_func, 'buttons/', 189, 48).simple()
		Button(551, self.menu_panel_y + 195, 'menu_quit', game_quit, 'buttons/', 189, 48).simple()

	def save_buttons(self):
		Button(self.item_pos_x, self.item_pos_y, buttons[1], item_use).simple()
		Button(self.item_pos_x + self.item_offset, self.item_pos_y, buttons[1], item_use).simple()
		Button(self.item_pos_x + 2*self.item_offset, self.item_pos_y, buttons[1], item_use).simple()
		Button(self.item_pos_x, self.item_pos_y + self.item_offset, buttons[1], item_use).simple()
		Button(self.item_pos_x + self.item_offset, self.item_pos_y + self.item_offset, buttons[1], item_use).simple()
		Button(self.item_pos_x + 2*self.item_offset, self.item_pos_y + self.item_offset, buttons[1], item_use).simple()
		Button(self.item_pos_x, self.item_pos_y + 2*self.item_offset, buttons[1], item_use).simple()
		Button(self.item_pos_x + self.item_offset, self.item_pos_y + 2*self.item_offset, buttons[1], item_use).simple()
		Button(self.item_pos_x + 2*self.item_offset, self.item_pos_y + 2*self.item_offset, buttons[1], item_use).simple()
		Button(self.item_pos_x, self.item_pos_y + 3*self.item_offset, buttons[1], item_use).simple()

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
				if event.type == pygame.QUIT:
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
			self.speaker_name, self.text_list = dialogue.get(self.scene_name)[self.line]
			Screen.button(self)
			pygame.display.update()
			if not self.scene_done:
				Screen.button(self)
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
				self.scene_done = True
				continue
			pygame.display.update()
			clock.tick(90)

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
			Button(self.start_pos_x, self.start_pos_y + self.start_offset_y, start_buttons[1], 'Scene0').aScene()
			Button(self.start_pos_x, self.start_pos_y + 2*self.start_offset_y, start_buttons[2], 'Scene0').aScene()
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
		displayText('Change your fate Kid', 0, self.dialog_text_size, self.color, self.text_pos_x, 0).active_panel()
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
		renderImage('mom-solo', 'character/', self.char_pos_x, self.char_pos_y).coordinates()
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
			Screen.save_buttons(self)
			pygame.display.update()
			clock.tick(60)

def item_use():

	main()

def save_func():

	activeScene().save_slots()

def god_menu():

	activeScene().main_menu()

def save():

	current_scene = previous_scenes[-1]
	pickle.dump(current_scene, open("savedata.txt", "wb"))
	print(previous_scenes)

def game_quit():

	pygame.quit()
	quit()

def main():

	activeScene('Start').game_start()
	pygame.quit()
	quit()

if __name__ == '__main__':
	main()