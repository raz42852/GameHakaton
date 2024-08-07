import Constants
import pygame


class Draw():
    def __init__(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.screen = screen
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT

    def draw_score(self, score, level):
        font = pygame.font.SysFont("arialblack", 32)
        if Constants.day:
            scoreSurf = font.render('Score: %s' % int(score), True, Constants.BLACK)
            levelSurf = font.render('Level: %s' % int(level), True, Constants.BLACK)
        else:
            scoreSurf = font.render('Score: %s' % int(score), True, Constants.WHITE)
            levelSurf = font.render('Level: %s' % int(level), True, Constants.WHITE)
        scoreRect = scoreSurf.get_rect()
        levelRect = levelSurf.get_rect()
        scoreRect.topleft = (self.SCREEN_WIDTH - 799, 10)
        levelRect.topleft = (self.SCREEN_WIDTH - 799, 50)
        self.screen.blit(scoreSurf, scoreRect)
        self.screen.blit(levelSurf, levelRect)

    def draw_text(self, text, color, location, time_pause):
        font = pygame.font.SysFont("arialblack", 70)
        text_Surf = font.render(text, True, color)
        text_Rect = text_Surf.get_rect()
        text_Rect.topleft = location
        self.screen.blit(text_Surf, text_Rect)
        pygame.display.flip()
        Constants.time_screen(time_pause)

    def draw_hearts(self, hearts):
        font = pygame.font.SysFont("arialblack", 40)
        if Constants.day:
            heartSurf = font.render(' %sx' % int(hearts), True, Constants.BLACK)
        else:
            heartSurf = font.render(' %sx' % int(hearts), True, Constants.WHITE)
        heartRect = heartSurf.get_rect()
        heartRect.topleft = (5, 90)
        self.screen.blit(heartSurf, heartRect)
        self.screen.blit(Constants.heart_img, (80, 95))

    def draw_background(self, screen):
        # Scroll the background
        Constants.background_y += Constants.speed
        screen.blit(Constants.bg, (200, Constants.background_y))
        screen.blit(Constants.bg, (200, Constants.background_y - self.SCREEN_HEIGHT))
        # If the background has scrolled off the screen, reset the y-coordinate
        if Constants.background_y >= self.SCREEN_HEIGHT:
            Constants.background_y = 0
        # switch side backgrounds from day - night
        if int(Constants.level / 5) % 2 == 1:
            screen.blit(Constants.bg_left_night, (0, 0))
            screen.blit(Constants.bg_right_night, (600, 0))
            Constants.day = False
            Constants.night = True
        elif int(Constants.level / 5) % 2 == 0:
            screen.blit(Constants.bg_left_day, (0, 0))
            screen.blit(Constants.bg_right_day, (600, 0))
            Constants.day = True
            Constants.night = False
