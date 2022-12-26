from settings import *

class Dino:
    def __init__(self, game, x):
        self.game = game
        self.imageCount = 0
        self.image = DINO_DEFAULT_IMAGE
        self.x = x
        self.y = GROUND_Y - self.image.get_height() + 50
        self.height = self.y
        self.down = False
        self.jumping = False
        self.falling = False

    def fall(self):
        self.image = DINO_DEFAULT_IMAGE

        if self.y < self.height:
            self.y += JUMP_VELOCITY
        if self.y >= self.height:
            self.falling = False

    def jump(self):
        self.image = DINO_DEFAULT_IMAGE

        if self.y > MAX_JUMP_HEIGHT and not self.falling:
            self.y -= JUMP_VELOCITY
        if self.y <= MAX_JUMP_HEIGHT:
            self.jumping = False
            self.falling = True

    def move(self):
        self.imageCount += 0.5

        if self.imageCount >= 2:
            self.imageCount = 0

        if self.down:
            self.image = DINO_DOWN_IMAGES[int(self.imageCount)]
        else:
            self.image = DINO_RUN_IMAGES[int(self.imageCount)]

        if not self.jumping and not self.falling:
            self.y = GROUND_Y - self.image.get_height() + 50

    def getMask(self):
        return pygame.mask.from_surface(self.image)

    def update(self):
        if not self.game.playing and self.game.points != 0:
            self.image = DINO_DEATH_IMAGE

        imageCenterPos = self.image.get_rect(topleft=(self.x, self.y)).center
        rectangle = self.image.get_rect(center=imageCenterPos)

        self.game.screen.blit(self.image, rectangle.topleft)
