import Constants
import pygame
from Menu import Menu


class Player():
    def __init__(self):
        pass

    def draw_player(self, screen):
        if Constants.walkCount >= 3:
            Constants.walkCount = 0

        # draw male frames
        if Constants.Male_choose:
            screen.blit(Constants.running_male[Constants.walkCount], (Constants.startx, Constants.starty))
            Constants.walkCount += 1
        # draw female frames
        elif Constants.Female_choose:
            screen.blit(Constants.running_female[Constants.walkCount], (Constants.startx, Constants.starty))
            Constants.walkCount += 1

    def key_event_listener(self, event, keys):
        if event.type == pygame.KEYDOWN:
            # if press left or a and set boundaries
            if event.key == pygame.K_LEFT and Constants.startx > 230 or event.key == pygame.K_a and Constants.startx > 230:
                Constants.startx -= 130
            # if press right or a and set boundaries
            if event.key == pygame.K_RIGHT and Constants.startx < 490 or event.key == pygame.K_d and Constants.startx < 490:
                Constants.startx += 130
        # if press escape to pause the game
        if keys[pygame.K_ESCAPE]:
            Constants.game_paused = True
            Constants.menu_state = "main"
            Menu(Constants.screen).menu_run()

    def player_jump(self, keys):
        # if the character does not jump
        if not Constants.isJump:
            if keys[pygame.K_SPACE]:
                Constants.isJump = True
        # if the character does jump
        else:
            if Constants.jumpCount >= -10:
                Constants.starty -= (Constants.jumpCount * abs(Constants.jumpCount)) * 0.5
                Constants.jumpCount -= 1
            else:
                Constants.jumpCount = 10
                Constants.isJump = False
