import pygame

pygame.init()

# CLOCK
clock = pygame.time.Clock()

# SCREEN
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PIGS")

# SPRITE
class Pigs(pygame.sprite.Sprite):
	def __init__(self, x_pos, y_pos, width, height, color, image):
		super().__init__()
		self.image = pygame.Surface((width, height))
		self.image.fill(color)
		self.rect = self.image.get_rect(topleft=(0, 0))
		self.image.blit(image, self.rect)


# Spritesheet
pigSheet = pygame.image.load("pig_walk.png").convert_alpha()

# SPRITE GROUP
container = pygame.sprite.Group()

# CUT SPRITE

# up
up1 = pigSheet.subsurface((0, 0, 128, 128))
up2 = pigSheet.subsurface((128, 0, 128, 128))
up3 = pigSheet.subsurface((256, 0, 128, 128))
up4 = pigSheet.subsurface((384, 0, 128, 128))

upList = [up1, up2, up3, up4]

# left
left1 = pigSheet.subsurface((0, 128, 128, 128))
left2 = pigSheet.subsurface((128, 128, 128, 128))
left3 = pigSheet.subsurface((256, 128, 128, 128))
left4 = pigSheet.subsurface((384, 128, 128, 128))

leftList = [left1, left2, left3, left4]

# down
down1 = pigSheet.subsurface((0, 256, 128, 128))
down2 = pigSheet.subsurface((128, 256, 128, 128))
down3 = pigSheet.subsurface((256, 256, 128, 128))
down4 = pigSheet.subsurface((384, 256, 128, 128))

downList = [down1, down2, down3, down4]

# right
right1 = pigSheet.subsurface((0, 384, 128, 128))
right2 = pigSheet.subsurface((128, 384, 128, 128))
right3 = pigSheet.subsurface((256, 384, 128, 128))
right4 = pigSheet.subsurface((384, 384, 128, 128))

rightList = [right1, right2, right3, right4]

# ADD SPRITE
add_sprite = Pigs(0, 0, 128, 128, "white", up1)

sprite_index = 0

container.add(add_sprite)

# MAIN LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill("white")

	# KEYS
	key = pygame.key.get_pressed()

	# UP
	if key[pygame.K_UP]:
		add_sprite.image = upList[sprite_index]
		sprite_index += 1
		add_sprite.rect.y -= 5

	if sprite_index >= len(upList):
		sprite_index = 0

	# LEFT
	if key[pygame.K_LEFT]:
		add_sprite.image = leftList[sprite_index]
		sprite_index += 1
		add_sprite.rect.x -= 5

	if sprite_index >= len(leftList):
		sprite_index = 0

	# DOWN
	if key[pygame.K_DOWN]:
		add_sprite.image = downList[sprite_index]
		sprite_index += 1
		add_sprite.rect.y += 5

	if sprite_index >= len(downList):
		sprite_index = 0

	# RIGHT
	if key[pygame.K_RIGHT]:
		add_sprite.image = rightList[sprite_index]
		sprite_index += 1
		add_sprite.rect.x += 5

	if sprite_index >= len(rightList):
		sprite_index = 0

	
	# DRAW
	container.draw(screen)

	pygame.display.flip()

	clock.tick(30)

pygame.quit()
