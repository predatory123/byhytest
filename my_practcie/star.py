import pygame

class Star():
    def __init__(self,screen):
        #初始化小星星的位置
        self.screen = screen

        #加载星星图像并获取其外接矩形
        self.image = pygame.image.load('image/time.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将每个星星放在屏幕底部
        self.rect.centerx =self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        #在指定位置绘制星星
        self.screen.blit(self.image,self.rect)