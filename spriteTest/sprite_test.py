import pygame

pygame.init()

# CLOCK
clock = pygame.time.Clock()

# SCREEN
screen = pygame.display.set_mode((800, 600))

# SPRITES
class Pig_Sprite(pygame.sprite.Sprite):
	def __init__(self, x_pos, y_pos, width, height, image):
		super().__init__()
		
		self.image = pygame.Surface((width, height))
		self.image.fill("wheat")

		self.rect = self.image.get_rect()
		self.rect.topleft = (x_pos, y_pos)

		self.image.blit(image, self.rect.topleft)

sprite_container = pygame.sprite.Group()

pig_image = pygame.image.load("pig_walk.png")

pig_up = [Pig_Sprite(0, 0, 128, 128, pig_image), 
	Pig_Sprite(128, 0, 128, 128, pig_image),
	Pig_Sprite(256, 0, 128, 128, pig_image), 
	Pig_Sprite(384, 0, 128, 128, pig_image)]
pig_left = []
pig_down = []
pig_right = []

pig_index = 0

sprite_container.add(pig_up[0])

def UP():
	global pig_index
	key = pygame.key.get_pressed()

	if key[pygame.K_UP]:
		#sprite_container.empty()
		sprite_container.add(pig_up[pig_index])
		pig_index += 1

		if pig_index == len(pig_up):
			pig_index = 0
		for i in pig_up:
			i.rect.y += 5

def LEFT():
	pass

def DOWN():
	pass

def RIGHT():
	pass

# MAIN LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill("wheat")

	sprite_container.draw(screen)
	UP()

	pygame.display.flip()

	clock.tick(60)

pygame.quit()
