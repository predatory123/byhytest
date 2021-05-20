import sys
import pygame
from pygame.sprite import Group
from setting import settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import  Button

import game_functions as gf

def run_game():
    # 初始化游戏界面，并创建一个屏幕对象
    pygame.init()
    ai_settings = settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    #创建一艘飞船
    ship =  Ship(ai_settings,screen)

    #创建一个用于存储子弹的编组
    bullets = Group()

    #创建一个外星人 群组
    # alien = Alien(ai_settings,screen)

    #创建一个play按键
    play_button = Button(ai_settings,screen,"Play")

    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)

    #创建一个用于存储有系统及信息的实例
    stats = GameStats(ai_settings)
    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
            gf.update_screen(ai_settings,screen,ship,aliens,bullets,play_button)

run_game()
