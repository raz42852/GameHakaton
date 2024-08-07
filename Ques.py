import Constants
import pygame
import random
from Draw import Draw


class Questions():
    def __init__(self, used_ques, screen_height, screen_width):
        self.used_ques = used_ques
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.font_ques = pygame.font.Font(None, 30)
        self.question_run = True

    def draw_questions(self):
        import time
        # Shuffle the questions to randomize the order
        while True:
            ran_ques = random.randint(0, 16)
            if ran_ques not in self.used_ques:
                break
            elif len(self.used_ques) == 17:
                self.used_ques = []
        self.used_ques.append(ran_ques)

        start_time = time.time()
        time_limit = 30

        # set up the question and options
        question = Constants.QUESTIONS[ran_ques]["question"]
        options = Constants.QUESTIONS[ran_ques]["answers"]
        correct_answer = Constants.QUESTIONS[ran_ques]["answers"][Constants.QUESTIONS[ran_ques]["correct_answer"]]

        # main game loop
        while self.question_run:
            # check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.question_run = False
                    Constants.terminate()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # check if the user clicked on any of the option rectangles
                    for i, option_rect in enumerate(option_rects):
                        if option_rect.collidepoint(pygame.mouse.get_pos()):
                            # check if the user clicked on the correct answer
                            if options[i] == correct_answer:
                                self.question_run = False
                                return True
                            else:
                                self.question_run = False
                                return False

            # calculate the remaining time
            elapsed_time = time.time() - start_time
            remaining_time = max(time_limit - elapsed_time, 0)

            # fill the window with white
            Constants.screen.fill(Constants.WHITE)

            # draw the question
            question_surface = self.font_ques.render(question, True, Constants.BLACK)
            question_rect = question_surface.get_rect(center=(Constants.SCREEN_WIDTH / 2, Constants.SCREEN_HEIGHT / 6))
            if question_rect.bottom > Constants.SCREEN_HEIGHT:
                # if the question goes off the bottom of the screen, move it to the next line
                question_rect.top = Constants.SCREEN_HEIGHT / 3 + 10
                question_rect.left = 10
            Constants.screen.blit(question_surface, question_rect)

            # draw the options
            option_surfaces = []
            option_rects = []
            for i, option in enumerate(options):
                option_surface = self.font_ques.render(option, True, Constants.BLACK)
                option_rect = option_surface.get_rect(
                    center=(Constants.SCREEN_WIDTH / 2, (i + 2) * Constants.SCREEN_HEIGHT / 7))
                if option_rect.bottom > Constants.SCREEN_HEIGHT:
                    # if an option goes off the bottom of the screen, move it to the next line
                    option_rect.top = (i + 2) * Constants.SCREEN_HEIGHT / 4 + 10
                    option_rect.left = 10
                Constants.screen.blit(option_surface, option_rect)
                option_surfaces.append(option_surface)
                option_rects.append(option_rect)

            # draw the timer
            timer_surface = self.font_ques.render(f"Time left: {int(remaining_time)}", True, Constants.BLACK)
            timer_rect = timer_surface.get_rect(topright=(Constants.SCREEN_WIDTH - 10, 10))
            Constants.screen.blit(timer_surface, timer_rect)

            # update the display
            pygame.display.update()

            # check if the time limit has been reached
            if elapsed_time >= time_limit:
                self.question_run = False
                return False

    def draw_ans(self, answer):
        if answer:
            Constants.screen.fill(Constants.WHITE)
            Draw(Constants.screen, Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT).draw_text('Right Answer',
                                                                                              (0, 255, 0), (175, 150),
                                                                                              1.5)
        # if the user answer wrong
        else:
            Constants.hearts -= 1
            Constants.fail_sound()
            Constants.screen.fill(Constants.WHITE)
            Draw(Constants.screen, Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT).draw_text('Wrong Answer',
                                                                                              (255, 0, 0), (150, 150),
                                                                                              1.5)
