import pygame

from star_setting import Settings
from star import Star
import star_functions as sf
from pygame.sprite import Group




def run_game():
    # 初始化游戏属性 并创建一个屏幕对象
    pygame.init()
    star_set = Settings()
    screen = pygame.display.set_mode((star_set.screen_width,star_set.screen_height))
    pygame.display.set_caption('little star')

    # 创建一个星星
    star = Star(screen)

    aliens = Group()
    sf.create_fleet(star_set,screen,star,aliens)
    # alien = Alien(star_set,screen)
    # 开始游戏的循环
    while True:
        sf.check_events()
        sf.update_screen(star_set,screen,star,aliens)
run_game()
