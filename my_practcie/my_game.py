import sys
import pygame
from pygame.sprite import Group
from game_setting import settings
from died import Died
import  function as f
def run_game():
    # 初始化游戏对象，并定义屏幕属性
    pygame.init()
    game_set = settings()
    screen = pygame.display.set_mode((game_set.screen_width,game_set.screen_height))
    pygame.display.set_caption('my game')

    #创建一个角色
    die = Died(game_set,screen)

    #创建一个用于存储子弹的编组
    bullets = Group()

    #开始游戏循环
    while True:
        f.check_events(game_set,screen,die,bullets)
        die.update()
        bullets.update()
        f.update_bullets(bullets)


        f.update_screen(game_set,screen,die,bullets)
run_game()


# import sys
# import pygame
#
# from game_setting import settings
# import function as fu
# from died import Died
# from pygame.sprite import Group
#
# def run_game():
#     pygame.init()
#     die_set = settings()
#     screen = pygame.display.set_mode((die_set.screen_width,die_set.screen_height))
#     pygame.display.set_caption('my world')
#     die= Died(die_set,screen)
#     bullets = Group()
#
#
#     # bg_color = (230,230,230)
#
#     while True:
#         fu.check_events(die,die_set,screen,bullets)
#         die.update()
#         bullets.update()
#         fu.update_screen(die_set,screen,die,bullets)
#
#
#
#
#
#
#         # for event in pygame.event.get():
#         #     if event.type == pygame.QUIT:
#         #         sys.exit()
#     #每次循环都重绘屏幕
#         # screen.fill(shezhi.bg_color)
#         # die.blitme()
#         # pygame.display.flip()
#
# run_game()