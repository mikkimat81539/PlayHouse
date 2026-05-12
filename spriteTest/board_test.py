import pygame, random

pygame.init()

# SCREEN
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Board Game")

# SPRITE
class BoardGame(pygame.sprite.Sprite):
	def __init__(self, x_pos, y_pos, width, height, color):
		super().__init__()
		self.image = pygame.Surface((width, height))
		self.image.fill(color)
		self.rect = self.image.get_rect(topleft = (x_pos, y_pos))

#class Squares:
#	def __init__(self, x_pos, y_pos, width, height, color):
#		self.x_pos = x_pos
#		self.y_pos = y_pos
#		self.width = width
#		self.height = height
#		self.color = color
#		self.rect = pygame.Rect((self.x_pos, self.y_pos), (self.width, self.height))
#
#	def drawShape(self, surface):
#		pygame.draw.rect(surface, self.color, self.rect)


# SPRITESHEET
colorList = ["red", "blue", "green", "purple", "white", "black", "teal"]
# square1 = BoardGame(200, 200, 50, 50, random.choice(colorList))

# GROUP
container = pygame.sprite.Group()

# MATRIX
matrix_data = [1, 0, 0, 1, 1]

x = 200
y = 200

for row in matrix_data:
	if row != 0:
		container.add(BoardGame(x, y, 50, 50, random.choice(colorList)))
	x += 50


# MAIN LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill("wheat")


	container.draw(screen)

	pygame.display.flip()

pygame.quit()
