from settings import *
from pygame.locals import *
from sys import exit
from classes.ground import Ground
from classes.dino import Dino
from classes.cloud import Cloud
from classes.cactus import Cactus
from classes.ptero import Ptero

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('T-Rex Run')
        pygame.display.set_icon(ICON_IMAGE)
        self.playing = False
        self.points = 0
        self.highPoints = 0
        self.dead = False
        self.showHighScore = False
        self.gameVelocity = VELOCITY

        self.ground = Ground(self, GROUND_Y)
        self.dino = Dino(self, 50)
        self.cloud = Cloud(self)
        self.cactus = [Cactus(self, 0), Cactus(self, 1)]
        self.ptero = Ptero(self)

    def update(self):
        self.screen.fill((255, 255, 255))

        if self.points != 0:
            text = POINTS_FONT.render(f'{int(self.points):0>5}', True, (0, 0, 0))
            self.screen.blit(text, (SCREEN_WIDTH - 10 - text.get_width(), 10))

            if self.showHighScore or self.dead:
                highScore = POINTS_FONT.render(f'HI {int(self.highPoints):0>5}', True, (80, 80, 80))
                self.screen.blit(highScore, (SCREEN_WIDTH - 30 - text.get_width() - highScore.get_width(), 10))

        self.ground.update()
        self.cloud.update()
        for cacto in self.cactus:
            cacto.update()
        self.ptero.update()
        self.dino.update()

        if self.dead:
            text = GAME_OVER_FONT.render('GAME OVER', True, (0, 0, 0))
            self.screen.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, 100))
            self.screen.blit(RESTART_BUTTON_IMAGE, (SCREEN_WIDTH / 2 - RESTART_BUTTON_IMAGE.get_width() / 2, 180))

        pygame.display.update()

    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE or event.key == K_UP:
                    if self.dead:
                        del self.dino, self.cactus, self.ptero

                        self.dino = Dino(self, 50)
                        self.cactus = [Cactus(self, 0), Cactus(self, 1)]
                        self.ptero = Ptero(self)
                        self.points = 0
                        self.gameVelocity = VELOCITY
                        self.dead = False
                        self.showHighScore = True

                    if not self.dino.jumping:
                        self.dino.jumping = True
                        JUMP_SOUND.play()

                    self.playing = True
            if event.type == KEYUP:
                if event.key == K_DOWN:
                    self.dino.down = False

        if pygame.key.get_pressed()[K_DOWN] and not self.dino.jumping and not self.dino.falling:
            self.dino.down = True

    def run(self):
        while True:
            self.clock.tick(30)
            self.checkEvents()

            if self.dead and self.points > self.highPoints:
                self.highPoints = self.points

            if self.playing:
                for cacto in self.cactus:
                    if cacto.collide() or self.ptero.collide():
                        DEATH_SOUND.play()
                        self.dead = True
                        self.playing = False
                    if self.cactus[0].x + self.cactus[0].image.get_width() < 0 and self.cactus[1].x + self.cactus[1].image.get_width() < 0:
                        del self.cactus
                        self.cactus = [Cactus(self, 0), Cactus(self, 1)]

                    if self.ptero.x == cacto.x:
                        self.ptero.x += 150
                    elif cacto.x + 150 > self.ptero.x > cacto.x - 150:
                        self.ptero.x += 300

                    cacto.move()

                self.ground.move()
                self.dino.move()
                if self.dino.jumping:
                    self.dino.jump()
                if self.dino.falling:
                    self.dino.fall()
                self.cloud.move()
                self.ptero.move()
                self.points += 0.2

                if int(self.points) != 0 and int(self.points) % 200 == 0:
                    self.gameVelocity += 0.5

            self.update()

if __name__ == '__main__':
    game = Game()
    game.run()
