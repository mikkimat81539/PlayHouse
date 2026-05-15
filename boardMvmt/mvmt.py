import pygame, random

pygame.init()

# SCREEN
screen = pygame.display.set_mode((700, 400))

# SPRITE CLASS
class Tiles(pygame.sprite.Sprite):
	def __init__(self, x_pos, y_pos, width, height, color):
		super().__init__()
		self.image = pygame.Surface((width, height))
		self.image.fill(color)
		self.rect = self.image.get_rect(topleft=(x_pos, y_pos))


# PLAYER CLASS
class Player:
	def __init__(self, x_pos, y_pos, radius, color):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.radius = radius
		self.color = color

		self.center = pygame.math.Vector2(self.x_pos, self.y_pos)

	def drawCircle(self, surface):
		pygame.draw.circle(surface, self.color, self.center, self.radius)


# SPRITE CONTAINER
container = pygame.sprite.Group()

# MATRIX
matrix_data = [[1, 1, 1, 1, 1, 1, 1],
		[1, 0, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 0, 0, 1],
		[1, 1, 1, 1, 1, 1, 1]]

# PLAYER
player = Player(100, 100, 10, "blue")

# COLOR LIST
colorList = ["red", "yellow", "white", "black", "brown", "green", "gray"]

# SPRITE OBJECT
init_x = 100
init_y = 100

y = init_y
for row in matrix_data:
	x = init_x
	for col in row:
		if col != 0:
			tiles = Tiles(x, y, 50, 50, random.choice(colorList))
			container.add(tiles)
		x += 50

	y += 50


# MAIN LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill("wheat")

	container.draw(screen)
	player.drawCircle(screen)


	pygame.display.flip()

pygame.quit()
