import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''表示单个外星人的类'''

    def __init__(self,game_set,screen):
        '''初始化外星人并设置其起始位置'''
        super(Alien,self).__init__()
        self.screen = screen
        self.game_set = game_set

        #加载外星人图像，并设置其 rect属性
        self.image = pygame.image.load('image/index.jpg')
        self.rect = self.image.get_rect()

        #每个外星人最初都在屏幕左上角附近
        self.x = self.rect.width
        self.y = self.rect.height

        #储存外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image,self.rect)

