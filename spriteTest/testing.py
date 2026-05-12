import pygame

pygame.init()

# CLOCK
clock = pygame.time.Clock()

# SCREEN
screen = pygame.display.set_mode((500, 300))

# SPRITE -- create sprite class
class Smile(pygame.sprite.Sprite):
	def __init__(self, x_pos, y_pos, width, height, color, image):
		super().__init__()
		self.image = pygame.Surface((width, height))
		self.image.fill(color)
		self.rect = self.image.get_rect(topleft=(0, 0))
		self.image.blit(image, self.rect)


add_sprite = pygame.sprite.Group() # create sprite container

# Add spritesheet image file
spriteImg = pygame.image.load("smileSprite.png").convert_alpha() # spriteImg = whole pizza

# Cut up the image file
# subsurface = one slice
sprite1 = spriteImg.subsurface((0, 0, 32, 32))
sprite2 = spriteImg.subsurface((32, 0, 32, 32))
sprite3 = spriteImg.subsurface((64, 0, 32, 32))
sprite4 = spriteImg.subsurface((96, 0, 32, 32))
sprite5 = spriteImg.subsurface((128, 0, 32, 32))
sprite6 = spriteImg.subsurface((160, 0, 32, 32))

# store in a list
spriteList = [sprite1, sprite2, sprite3, sprite4, sprite5, sprite6]

# Smile() = person eating the slice
smile_sprite = Smile(0, 0, 32, 32, "red", sprite1) # grab the sprite 

add_sprite.add(smile_sprite) # add it to sprite group

sprite_index = 0

# MAIN LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill("#000000")

	key = pygame.key.get_pressed()

	if key[pygame.K_RIGHT]:
		sprite_index += 1
	if key[pygame.K_LEFT]:
		sprite_index -= 1
		if sprite_index < 0:
			sprite_index = len(spriteList)-1 

	if sprite_index >= len(spriteList):
		sprite_index = 0


	smile_sprite.image = spriteList[sprite_index]

	# DRAW
	add_sprite.draw(screen)

	pygame.display.flip()

	clock.tick(15)

pygame.quit()
