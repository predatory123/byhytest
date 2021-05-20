import pygame

class Died():
    def __init__(self,game_set,screen):
        self.screen = screen
        self.game_set = game_set

        #加载游戏角色图像
        self.image = pygame.image.load('image/time.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 确定人物位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # 在飞船的属性 center中存储小数值
        self.center = float(self.rect.centerx)
        self.centery= float(self.rect.centery)

        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down =False

    def update(self):
        #根据移动标志调整角色的位置
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_set.die_speed_factor
        if self.moving_left and self.rect.left >0 :
            self.center -= self.game_set.die_speed_factor
        if self.moving_up and self.rect.top >0 :
            self.centery -= self.game_set.die_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.game_set.die_speed_factor

        # 根据 self.center更新 rect 对象
        self.rect.centerx = self.center
        self.rect.centery = self.centery

    def blitme(self):
        #在指定位置绘制角色
        self.screen.blit(self.image,self.rect)










# import pygame
#
# class Died():
#     def __init__(self,die_set,screen):
#         #初始化飞船并设置其初始位置
#         self.screen = screen
#         self.die_set = die_set
#         #加载飞船图像并获取其外接矩形
#         self.image = pygame.image.load('image/time.jpg')
#         self.rect = self.image.get_rect()
#         self.screen_rect = screen.get_rect()
#         #将每艘新飞船加载在屏幕底部中央
#         self.rect.centerx = self.screen_rect.centerx
#         self.rect.centery = self.screen_rect.centery
#         #在属性 center中存储小数
#         self.center = float(self.rect.centerx)
#         self.centery = float(self.rect.centery)
#
#         #移动标志
#         self.moving_right = False
#         self.moving_left = False
#         self.moving_up = False
#         self.moving_down = False
#     def update(self):
#         '''根据移动标志调整飞船的位置'''
#         if self.moving_right and self.rect.right < self.screen_rect.right:
#             self.center += self.die_set.die_speed_factor
#         if self.moving_left and self.rect.left >0:
#             self.center -= self.die_set.die_speed_factor
#         if self.moving_up and self.rect.top > 0:
#             self.centery -= self.die_set.die_speed_factor
#         if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
#             self.centery += self.die_set.die_speed_factor
#
#         self.rect.centerx = self.center
#         self.rect.centery = self.centery
#     def blitme(self):
#         '''在指定位置绘制飞船'''
#         self.screen.blit(self.image,self.rect)