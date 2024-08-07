import Constants
from Ques import Questions
from Draw import Draw


class Trash():
    def __init__(self, screen):
        self.screen = screen

    def draw_trash(self, screen):
        # if the trash pass the screen all down
        if Constants.starty_trash >= 150:
            Constants.starty_trash = -475
            Constants.move_trash = False
            Constants.collect_prop = False
            Constants.starty_prop = -50
        # draw the trashes
        screen.blit(Constants.trash_blue_img, (210, Constants.starty_trash))
        screen.blit(Constants.trash_orange_img, (340, Constants.starty_trash))
        screen.blit(Constants.trash_purple_img, (470, Constants.starty_trash))

    def moving_trash(self):
        # if the trash need to move down
        if Constants.move_trash:
            Constants.starty_trash += Constants.vel

    def check_compatibility_trash(self):
        # if the user put the item in the trash
        if Constants.starty == Constants.starty_trash + Constants.SCREEN_HEIGHT:
            Constants.prop_in = False
            # if the character on the left side of the screen
            if Constants.startx == 230:
                # check if the item match to blue trash
                for index in range(0, 2):
                    if Constants.ran_prop_path == Constants.prop_list[0]["blue"][index]:
                        Constants.prop_in = True
                    if Constants.prop_in:
                        Constants.level += 1
                        Draw(Constants.screen, Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT).draw_text('Level up !',
                                                                                                          (255, 0, 0),
                                                                                                          (225, 150),
                                                                                                          0.5)
                        break
                # if the character failed to match the item in the trash
                if not Constants.prop_in:
                    answer_for_ques = Questions(Constants.used_ques, Constants.SCREEN_HEIGHT,
                                                Constants.SCREEN_WIDTH).draw_questions()
                    # check the answer and draw it
                    Questions(Constants.used_ques, Constants.SCREEN_HEIGHT, Constants.SCREEN_WIDTH).draw_ans(
                        answer_for_ques)
            elif Constants.startx == 360:
                # check if the item match to orange trash
                for index in range(0, 4):
                    if Constants.ran_prop_path == Constants.prop_list[1]["orange"][index]:
                        Constants.prop_in = True
                    if Constants.prop_in:
                        Constants.level += 1
                        Draw(Constants.screen, Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT).draw_text('Level up !',
                                                                                                          (255, 0, 0),
                                                                                                          (225, 150),
                                                                                                          0.5)
                        break
                # if the character failed to match the item in the trash
                if not Constants.prop_in:
                    answer_for_ques = Questions(Constants.used_ques, Constants.SCREEN_HEIGHT,
                                                Constants.SCREEN_WIDTH).draw_questions()
                    # check the answer and draw it
                    Questions(Constants.used_ques, Constants.SCREEN_HEIGHT, Constants.SCREEN_WIDTH).draw_ans(
                        answer_for_ques)
            elif Constants.startx == 490:
                # check if the item match to purple trash
                for index in range(0, 2):
                    if Constants.ran_prop_path == Constants.prop_list[2]["purple"][index]:
                        Constants.prop_in = True
                    if Constants.prop_in:
                        Constants.level += 1
                        Draw(Constants.screen, Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT).draw_text('Level up !',
                                                                                                          (255, 0, 0),
                                                                                                          (225, 150),
                                                                                                          0.5)
                        break
                # if the character failed to match the item in the trash
                if not Constants.prop_in:
                    answer_for_ques = Questions(Constants.used_ques, Constants.SCREEN_HEIGHT,
                                                Constants.SCREEN_WIDTH).draw_questions()
                    # check the answer and draw it
                    Questions(Constants.used_ques, Constants.SCREEN_HEIGHT, Constants.SCREEN_WIDTH).draw_ans(
                        answer_for_ques)
