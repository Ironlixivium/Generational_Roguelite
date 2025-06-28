import pygame
import sys


class Game:
	def __init__(self, fps:int=60):
		pygame.init()
		self.fps = fps
		self.running = True
		

	def start(self):
		self.screen = self._init_screen()
		self.clock = pygame.time.Clock()
		#self.state = MenuState(self)
		self._run()

	def _run(self):
		while self.running:
			dt = self.clock.tick(self.fps) / 1000.0
			self.handle_events()
			self.update(dt)
			self.draw()
		pygame.quit()
		sys.exit()

	def handle_events(self):
		for evt in pygame.event.get():
			if evt.type == pygame.QUIT:
				self.running = False
			# elif ... route other input to self.state

	def update(self, dt:float):
		# advance your game-state, animations, physics, etc.
		# e.g. self.state.update(dt)
		pass

	def draw(self):
		self.screen.fill((30, 30, 30))
		# e.g. self.state.render(self.screen)
		pygame.display.flip()


	def _init_screen(self) -> pygame.Surface:
		pygame.init()
		screen = pygame.display.set_mode((800, 600))
		pygame.display.set_caption("Generational Roguelite")
		return screen

if __name__ == "__main__":
	Game().start()
