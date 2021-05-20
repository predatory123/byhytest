import sys
import pygame
from bullet import Bullet

def check_keydown_events(event,game_set,screen,die,bullets):
    if event.key == pygame.K_RIGHT:
        die.moving_right = True
    elif event.key == pygame.K_LEFT:
        die.moving_left = True
    elif event.key == pygame.K_UP:
        die.moving_up = True
    elif event.key == pygame.K_DOWN:
        die.moving_down = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(game_set,screen,die,bullets)

    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(game_set,screen,die,bullets):
    '''如果还没到达限制，就发射一颗子弹'''
    #创建一个新子弹，并将其加入到编程bullets中
    if len(bullets) < game_set.bullet_allowed:
        new_bullet = Bullet(game_set,screen,die)
        bullets.add(new_bullet)





def check_keyup_events(event,die):
    if event.key == pygame.K_RIGHT:
        die.moving_right = False
    elif event.key == pygame.K_LEFT:
        die.moving_left = False
    elif event.key == pygame.K_UP:
        die.moving_up = False
    elif event.key == pygame.K_DOWN:
        die.moving_down = False

def check_events(game_set,screen,die,bullets):
    #响应按键和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,game_set,screen,die,bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event,die)

def update_screen(game_set,screen,die,bullets):
    # 每次循环都重绘屏幕
    screen.fill(game_set.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    die.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

# import sys
# import pygame
# from bullet import Bullet
#
# def check_keydown_events(event,die,die_set,screen,bullets):
#     if event.key == pygame.K_RIGHT:
#         die.moving_right = True
#     elif event.key == pygame.K_LEFT:
#         die.moving_left = True
#     elif event.key == pygame.K_UP:
#         die.moving_up = True
#     elif event.key == pygame.K_DOWN:
#         die.moving_down = True
#
#     # 创建一颗子弹
#     elif event.key == pygame.K_SPACE:
#         new_bullet = Bullet(die_set,screen,die)
#         bullets.add(new_bullet)
#
#
# def check_keyup_events(event,die):
#     if event.key == pygame.K_RIGHT:
#         die.moving_right = False
#     elif event.key == pygame.K_LEFT:
#         die.moving_left = False
#     elif event.key == pygame.K_UP:
#         die.moving_up = False
#     elif event.key == pygame.K_DOWN:
#         die.moving_down = False
#
#
#
#
# def check_events(die,die_set,screen,bullets) :
#     '''响应按键和鼠标事件'''
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             print('quit')
#             sys.exit()
#
#         elif event.type == pygame.KEYDOWN:
#             check_keydown_events(event,die,screen,die_set,bullets)
#             # if event.key == pygame.K_RIGHT:
#             #     die.moving_right = True
#             # elif event.key == pygame.K_LEFT:
#             #     die.moving_left = True
#             # elif event.key == pygame.K_UP:
#             #     die.moving_up = True
#             # elif event.key == pygame.K_DOWN:
#             #     die.moving_down = True
#
#         elif event.type == pygame.KEYUP:
#             check_keyup_events(event,die)
#             # if event.key == pygame.K_RIGHT:
#             #     die.moving_right = False
#             # elif event.key == pygame.K_LEFT:
#             #     die.moving_left = False
#             # elif event.key == pygame.K_UP:
#             #     die.moving_up = False
#             # elif event.key == pygame.K_DOWN:
#             #     die.moving_down = False
#
# def update_screen(die_set,screen,die,bullets):
#     '''更新屏幕上的图像，并切换到新屏幕'''
#     # 每次循环都重绘屏幕
#     screen.fill(die_set.bg_color)
#
#     for bullet in bullets.sprites():
#         bullet.draw_bullet()
#     die.blitme()
#     #让最近绘制的屏幕可见
#     pygame.display.flip()
