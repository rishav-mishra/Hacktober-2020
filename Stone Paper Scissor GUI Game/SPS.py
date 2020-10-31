import sys, pygame, time, random
pygame.init()

################## GLOBAL ##################
size = width, height = 1050, 600
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('stOnE PaPer scIsSoR')
clock = pygame.time.Clock()
stoneImg = pygame.image.load('stone.jpg')
paperImg = pygame.image.load('paper.jpg')
scissorImg = pygame.image.load('scissor.jpg')
imgs = stoneImg, paperImg, scissorImg
da = pygame.image.load('1.jpg')
dt = pygame.image.load('2.jpg')
dth = pygame.image.load('3.jpg')
dancer = da,dt,dth
##############################################

def myrand(x, y):
	#GENERATE NUMBER IN RANGE [x,y]
	return random.randrange(x,y)	
def text_objects(text, font, clr) :
	textSurface = font.render(text, True, clr)
	return textSurface, textSurface.get_rect()
def message_display(text, x, y, sz, clr) :
	text_ = pygame.font.Font('freesansbold.ttf',sz)
	textSurface, textRect = text_objects(text, text_,clr)
	textRect.center = (x, y)
	screen.blit(textSurface, textRect)
	pygame.display.update()
def draw_(idx, x, y) :
	screen.blit(imgs[idx], (x,y))
def won(me, comp) :
	if me == 0 and comp == 2 :
		return True
	elif me == 1 and comp == 0 :
		return True
	elif me == 2 and comp == 1 :
		return True
	return False
def draw_d(idx, x, y) :
	screen.blit(dancer[idx], (x, y))
def game_loop() :
	start_ = False
	screen.fill(black)
	message_display('a-stone   s-paper   d-scissor',width * 0.5, height * 0.5, 30, green)
	while not start_ :
		for event in pygame.event.get() :
			if event.type == pygame.QUIT : #'X'
				pygame.quit()
				quit()
			elif event.type == pygame.KEYDOWN :
				start_ = True
				screen.fill(black)
				break
	cheater = 10000
	result = False
	while not result :
		screen.fill(black)
		ott = 3
		no_event = True
		while ott > 0 :
			cheater = 10000
			message_display(' ' + `ott`, width * 0.5, height * 0.5, 50, (myrand(0,255),myrand(0,255),myrand(0,255)))
			ott -= 1
			time.sleep(0.5)
			screen.fill(black)
			#while cheater > 100000 :
			#	cheater -= 1
			#	draw_d(random.randrange(0,2), 20,20)##
			#	pygame.display.update()
			pygame.display.update()
		computer_move = random.randrange(0,2)
		pygame.event.clear()
		message_display('PRESS', width * 0.5, height * 0.5, 50, red)
		while no_event :
			screen.fill(black)
			#draw_d(random.randrange(0,2), 20,20)##
			for event in pygame.event.get() :
				#draw_d(random.randrange(0,2), 20,20)##
				if event.type == pygame.QUIT :
					no_event = False
					pygame.quit()
					quit()
				elif event.type == pygame.KEYDOWN :
					no_event = False
					if event.key == pygame.K_LEFT :
						draw_(computer_move, width * 0.6, height * 0.5)
						draw_(0, width * 0.4, height * 0.5)
						if won(0,computer_move) :
							message_display('YOU WON',  width * 0.5, height * 0.3, 55, (myrand(0,255),myrand(0,255),myrand(0,255)))
							victory = True
						elif computer_move == 0 : 
							message_display('DRAW',  width * 0.5, height * 0.3, 55, (myrand(0,255),myrand(0,255),myrand(0,255)))
						else :
							message_display('YOU LOOSE',  width * 0.5, height * 0.3, 55, (myrand(0,255),myrand(0,255),myrand(0,255)))
							result = True
					
					elif event.key == pygame.K_UP :
						draw_(computer_move, width * 0.6, height * 0.5)
						draw_(1, width * 0.4, height * 0.5)
						if won(1,computer_move) :
							message_display('YOU WON',  width * 0.5, height * 0.3, 55, (myrand(0,255),myrand(0,255),myrand(0,255)))
							victory = True
						elif computer_move == 1 : 
							message_display('DRAW',  width * 0.5, height * 0.3, 55, (myrand(0,255),myrand(0,255),myrand(0,255)))
						else :
							message_display('YOU LOOSE',  width * 0.5, height * 0.3, 55, (myrand(0,255),myrand(0,255),myrand(0,255)))
							result = True
					
					elif event.key == pygame.K_RIGHT :
						draw_(computer_move, width * 0.6, height * 0.5)
						draw_(2, width * 0.4, height * 0.5)
						if won(2,computer_move) :
							message_display('YOU WON',  width * 0.5, height * 0.3, 55, (myrand(0,255),myrand(0,255),myrand(0,255)))
							victory = True
						elif computer_move == 2 : 
							message_display('DRAW',  width * 0.5, height * 0.3, 55, (myrand(0,255),myrand(0,255),myrand(0,255)))
						else :
							message_display('YOU LOOSE',  width * 0.5, height * 0.3, 55, (myrand(0,255),myrand(0,255),myrand(0,255)))
							result = True
				time.sleep(3)
				pygame.display.update()
				
	decide = False
	while not decide :
		screen.fill((myrand(0,255),myrand(0,255),myrand(0,255)))
		message_display('PRESS <- FOR NEW GAME ELSE PRESS ANY KEY TO EXIT', width * 0.5, height * 0.5, 30, (myrand(0,255),myrand(0,255),myrand(0,255)))
		draw_d(random.randrange(0,2), 20,20)##
		pygame.display.update()
		for event in pygame.event.get() :
			if event.type == pygame.QUIT : #'X'
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_LEFT :
					game_loop()
					decide = True
				else  :
					decide = True
		time.sleep(0.3)

game_loop()
pygame.quit()
