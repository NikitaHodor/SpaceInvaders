#import sys now in game_functions module
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship

import game_functions as gf

def run_game():
    #init game and make screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #init button
    play_button = Button(ai_settings, screen, "Play") 
    #init ship
    ship = Ship(ai_settings, screen)
    #init bullets
    bullets = Group()
    #init alien
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    #stats
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #launch main game cicle
    while True:
        #keyboard event listen
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
