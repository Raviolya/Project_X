import pygame
from settings import *
import os


class SpriteSheet(object):
    
 
    def __init__(self, file_name):
       
 
        self.sprite_sheet = pygame.image.load(file_name).convert()
 
 
    def get_image(self, x, y, width, height):
        
 
        
        image = pygame.Surface([width, height]).convert()
 
        
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
 
        
        image.set_colorkey(BLACK)
 
       
        return image

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()

screen = pygame.display.set_mode(windowSize)


ss_background = pygame.image.load(os.path.join(imgFolder,'start.jpg')).convert()


l1_bg = pygame.image.load(os.path.join(imgFolder,'l1.png')).convert()


bulletImage = pygame.image.load(os.path.join(imgFolder,'bullet.png')).convert()


soldier_sheet = SpriteSheet(os.path.join(imgFolder,'enemies.png'))


player_sheet = SpriteSheet(os.path.join(imgFolder,'playersheet.png'))

PLAYER_RIGHT_0 = player_sheet.get_image(145,15,25,37).convert()
PLAYER_RIGHT_1 = player_sheet.get_image(144,133,22,36).convert()
PLAYER_RIGHT_2 = player_sheet.get_image(167,134,22,36).convert()
PLAYER_RIGHT_3 = PLAYER_RIGHT_0
PLAYER_RIGHT_4 = player_sheet.get_image(190,135,24,35).convert()
PLAYER_RIGHT_5 = player_sheet.get_image(218,133,19,35).convert()
PLAYER_RIGHT_6 = player_sheet.get_image(242,132,18,37).convert()

PLAYER_RIGHT_UP_0 = player_sheet.get_image(145,95,20,35).convert()
PLAYER_RIGHT_UP_1 = player_sheet.get_image(171,95,23,33).convert()
PLAYER_RIGHT_UP_2 = player_sheet.get_image(199,96,25,34).convert()

PLAYER_RIGHT_DOWN_0 = player_sheet.get_image(144,55,19,36).convert()
PLAYER_RIGHT_DOWN_1 = player_sheet.get_image(170,56,19,35).convert()
PLAYER_RIGHT_DOWN_2 = player_sheet.get_image(195,56,23,35).convert()

PLAYER_JUMP_0 = player_sheet.get_image(183,176,22,17).convert()
PLAYER_JUMP_1 = player_sheet.get_image(206,171,17,20).convert()
PLAYER_JUMP_2 = player_sheet.get_image(225,175,22,17).convert()
PLAYER_JUMP_3 = player_sheet.get_image(249,172,17,20).convert()

PLAYER_DEAD_0 = player_sheet.get_image(144,198,25,19).convert()
PLAYER_DEAD_1 = player_sheet.get_image(170,193,19,23).convert()
PLAYER_DEAD_2 = player_sheet.get_image(192,198,22,18).convert()
PLAYER_DEAD_3 = player_sheet.get_image(219,194,17,22).convert()
PLAYER_DEAD_4 = player_sheet.get_image(238,204,35,11).convert()


sniper_sheet = SpriteSheet(os.path.join(imgFolder,'enemies.png'))

SNIPER_LEFT_DOWN = sniper_sheet.get_image(135,249,32,57).convert()
SNIPER_LEFT = sniper_sheet.get_image(98,261,37,47).convert()
SNIPER_LEFT_UP = sniper_sheet.get_image(217,309,33,49).convert()


soldier_sheet = sniper_sheet 

SOLDIER_0 = soldier_sheet.get_image(22,4,37,40).convert()
SOLDIER_1 = soldier_sheet.get_image(60,4,35,46).convert()
SOLDIER_2 = soldier_sheet.get_image(96,4,23,43).convert()
SOLDIER_3 = soldier_sheet.get_image(121,4,29,43).convert()
SOLDIER_4 = soldier_sheet.get_image(151,4,37,43).convert()
SOLDIER_5 = soldier_sheet.get_image(190,4,38,41).convert()
SOLDIER_6 = soldier_sheet.get_image(231,4,29,45).convert()
SOLDIER_7 = soldier_sheet.get_image(261,4,24,44).convert()
SOLDIER_8 = soldier_sheet.get_image(288,4,30,43).convert()


TANK_0 = pygame.image.load(os.path.join(imgFolder,'tank.png'))




POWERUP_SLOW = pygame.image.load(os.path.join(imgFolder,'slow.png')).convert()
POWERUP_BLINK = pygame.image.load(os.path.join(imgFolder,'force.png')).convert()
POWERUP_BULLET = pygame.image.load(os.path.join(imgFolder,'bullet_slow.png')).convert()


explosion_sheet = SpriteSheet(os.path.join(imgFolder,'explosion.png'))

EXPLOSION_0 = explosion_sheet.get_image(0,0,31,30).convert()
EXPLOSION_1 = explosion_sheet.get_image(31,0,31,30).convert()
EXPLOSION_2 = explosion_sheet.get_image(62,0,31,30).convert()
EXPLOSION_3 = explosion_sheet.get_image(93,0,31,30).convert()
EXPLOSION_4 = explosion_sheet.get_image(124,0,31,30).convert()



shoot_sound = pygame.mixer.Sound(os.path.join(soundFolder,'Shoot.wav'))
powerup_sound = pygame.mixer.Sound(os.path.join(soundFolder,'Powerup.wav'))
explosion_sound = pygame.mixer.Sound(os.path.join(soundFolder,'Explosion.wav'))
hit_sound = pygame.mixer.Sound(os.path.join(soundFolder, 'Hit.wav'))
jump_sound = pygame.mixer.Sound(os.path.join(soundFolder, 'Jump.wav'))
dash_sound = pygame.mixer.Sound(os.path.join(soundFolder, 'Dash.wav'))
pygame.mixer.music.load(os.path.join(soundFolder,'Skillet_-_Monster_47950047.mp3'))
pygame.mixer.music.set_volume(0.5)