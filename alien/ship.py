import  pygame

class Ship():
    def __init__(self,ai_settings,screen):
        #初始化飞船并设置其初始位置
        self.screen = screen
        self.ai_settings = ai_settings
        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #将每艘新飞船加载在屏幕中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #在飞船的属性 center 中存储小数值
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)
        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        '''根据移动标志调整飞船的位置'''
        #更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.bottom -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.ai_settings.ship_speed_factor

        #根据self.center 更新rect对象
        self.rect.centerx = self.center
        self.rect.centery = self.bottom
    def blitme(self):
        '''在指定位置绘制黑崎一护'''
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        #让飞船在屏幕上居中
        self.center = self.screen_rect.centerx