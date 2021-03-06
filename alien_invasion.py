#-*-coding:utf-8-*-
import pygame
import game_functions as gf

from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
from pygame.sprite import Group
from button import Button
from scoreboard import Scoreboard
from tools import Tools


def run_game():

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, 
        ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    play_button = Button(ai_settings, screen, "play")
    #创建一个用于存储游戏统计信息的实例,并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #创建游戏中所需的道具
    ItemBullet = Tools(ai_settings, screen)

    #创建一个飞船
    ship = Ship(ai_settings, screen)
    
    #创建外星人
    aliens = Group()

    #创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #创建一个用于存储子弹的编组
    bullets = Group()

    while True:

        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
            gf.update_itembullet(ai_settings, screen, ship, ItemBullet, aliens)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, ItemBullet)
        

run_game()
