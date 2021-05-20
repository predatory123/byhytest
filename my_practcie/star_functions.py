import sys
import pygame
from star_alien import Alien

def check_events():
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(star_set,screen,star,aliens):
    '''更新屏幕上的图像，并切换到新屏幕'''
    # 每次循环时都重绘屏幕
    screen.fill(star_set.bg_color)
    star.blitme()
    aliens.draw(screen)
    # 让最近绘制的屏幕可见
    pygame.display.flip()

def create_fleet(star_set,screen,star,aliens):
    '''创建外星人群'''
    #创建一个外星人，并计算一行可容纳多少个外星人
    #外星人间距为外星人宽度
    alien = Alien(star_set,screen)
    # alien_width = alien.rect.width
    # available_space_x = star_set.screen_width - 2*alien_width
    number_aliens_x = get_number_aliens_x(star_set,alien.rect.width)
    number_rows = get_number_rows(star_set,star.rect.height,alien.rect.height)

    # 创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_rows):
            create_alien(star_set,screen,aliens,alien_number,row_number)
        #创建一个外星人并将其加入到当前行
        # alien = Alien(star_set,screen)
        # alien.x = alien_width + 2 * alien_width * alien_number
        # alien.rect.x =alien.x
        # aliens.add(alien)
def get_number_aliens_x(star_set,alien_width):
    available_space_x = star_set.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(star_set,screen,aliens,alien_number,row_number):
    alien = Alien(star_set, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height = 2* alien.rect.height * row_number
    aliens.add(alien)

def get_number_rows(star_set,star_height,alien_height):
    '''计算屏幕可容纳多少外星人'''
    available_space_y = (star_set.screen_height - (3*alien_height) - star_height)
    number_rows = int(available_space_y / (2*alien_height))
    return  number_rows
