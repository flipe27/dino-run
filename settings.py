import pygame
import os

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 400

GROUND_Y = 330
MAX_JUMP_HEIGHT = 40
JUMP_VELOCITY = 25
VELOCITY = 15
PTERO_INITIAL = 20000

ICON_IMAGE = pygame.image.load(os.path.join('images', 'icon.ico'))
GROUND_IMAGE = pygame.image.load(os.path.join('images', 'ground.png'))
DINO_DEFAULT_IMAGE = pygame.image.load(os.path.join('images', 'dino-default.png'))
DINO_DEATH_IMAGE = pygame.image.load(os.path.join('images', 'dino-death.png'))
DINO_RUN_IMAGES = [
    pygame.image.load(os.path.join('images', 'dino-run0.png')),
    pygame.image.load(os.path.join('images', 'dino-run1.png'))
]
DINO_DOWN_IMAGES = [
    pygame.image.load(os.path.join('images', 'dino-down0.png')),
    pygame.image.load(os.path.join('images', 'dino-down1.png'))
]
CLOUD_IMAGE = pygame.image.load(os.path.join('images', 'cloud.png'))
CACTUS_IMAGES = [
    pygame.image.load(os.path.join('images', 'cactus0.png')),
    pygame.image.load(os.path.join('images', 'cactus1.png')),
    pygame.image.load(os.path.join('images', 'cactus2.png'))
]
PTERO_IMAGES = [
    pygame.image.load(os.path.join('images', 'ptero0.png')),
    pygame.image.load(os.path.join('images', 'ptero1.png'))
]
RESTART_BUTTON_IMAGE = pygame.image.load(os.path.join('images', 'restart-button.png'))

pygame.mixer.init()
JUMP_SOUND = pygame.mixer.Sound(os.path.join('sounds', 'jump-sound.wav'))
DEATH_SOUND = pygame.mixer.Sound(os.path.join('sounds', 'death-sound.wav'))

pygame.font.init()
POINTS_FONT = pygame.font.SysFont('comicsansms', 30)
GAME_OVER_FONT = pygame.font.SysFont('comicsansms', 40)
