import pygame.time
import Constants
from Player import Player
from Prop import Items
from Trash import Trash
from Menu import Menu
from Draw import Draw

# set up the pygame
pygame.init()
pygame.display.set_caption("Main Menu")
FPSCLOCK = pygame.time.Clock()
font = pygame.font.Font(None, 30)

# Set up the sound
music_file_path = Constants.curr_song
pygame.mixer.music.load(music_file_path)
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()

player = Player()
prop = Items()
bomb = Items()
trash = Trash(Constants.screen)
menu = Menu(Constants.screen)
draw = Draw(Constants.screen, Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT)

menu.menu_run()


def redraw_game_window():
    draw.draw_background(Constants.screen)
    prop.draw_prop(Constants.screen)
    trash.draw_trash(Constants.screen)
    bomb.draw_bomb(Constants.screen)
    draw.draw_score(Constants.score, Constants.level)
    draw.draw_hearts(Constants.hearts)
    player.draw_player(Constants.screen)
    pygame.display.update()


game_running = True
while game_running:
    if int(Constants.score) == 40:
        FPS = 50
    elif int(Constants.score) == 70:
        FPS = 60
    # score up
    Constants.score += 0.05
    redraw_game_window()
    FPSCLOCK.tick(Constants.FPS)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Constants.terminate()
        player.key_event_listener(event, keys)
    bomb.move_bomb()
    prop.move_prop()
    trash.moving_trash()
    trash.check_compatibility_trash()
    player.player_jump(keys)
    menu.switch_song()
    # if he has no left hearts and the game
    if Constants.hearts == 0:
        game_running = False

menu.end_game()
