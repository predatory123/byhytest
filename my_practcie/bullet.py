import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, game_set, screen, die):
        # 在游戏对象所在的位置创建一个子单的对象
        super(Bullet,self).__init__()
        self.screen = screen

    # 在(0,0)处创建一个表示子弹的矩形，在设置正确的位置
        self.rect = pygame.Rect(0, 0, game_set.bullet_width, game_set .bullet_height)
        self.rect.centerx = die.rect.centerx
        self.rect.top = die.rect.top

    # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)

        self.color = game_set.bullet_color
        self.speed_factor = game_set.bullet_speed_factor


    def update(self):
        self.y -= self.speed_factor
    # 更新表示子弹的rect的位置
        self.rect.y =self.y

    def draw_bullet(self):

    # 在屏幕上绘制子弹
        pygame.draw.rect(self.screen,self.color,self.rect)

