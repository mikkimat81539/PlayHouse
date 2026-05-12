import pygame, random

pygame.init()

# CLOCK
clock = pygame.time.Clock()

# SCREEN
screen = pygame.display.set_mode((500, 300))

# SPRITE
class BoardGame(pygame.sprite.Sprite):
	def __init__(self, x, y, width, height, color):
		super().__init__()
		self.width = width
		self.height = height
		self.color = color

		self.image = pygame.Surface((self.width, self.height))
		self.image.fill(color)

		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)

colorList = ["red", "blue", "purple", "green", "yellow", "brown", "teal", "white", "black"]
matrix_data = [1, 0, 0, 1, 1]

all_sprites = pygame.sprite.Group()
x, y = 0, 0

for i in matrix_data:
	if i != 0:
		tile = BoardGame(x, y, 50, 50, random.choice(colorList))
		all_sprites.add(tile)
	x += 50  # move x for the next tile


# MAIN LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill("wheat")

	all_sprites.draw(screen)

	pygame.display.flip()

	clock.tick(60)
	
pygame.quit()
