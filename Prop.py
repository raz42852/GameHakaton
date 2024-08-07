from Ques import Questions
import Constants
import pygame
import random


class Items():
    def __init__(self):
        self.font = pygame.font.SysFont("arialblack", 40)

    def draw_prop(self, screen):
        # check if prop is appear
        if Constants.show_prop:
            screen.blit(Constants.prop_img, (Constants.ran_prop_x, Constants.starty_prop))
            Constants.time = Constants.score
        # check if the user collect the prop
        if Constants.collect_prop:
            screen.blit(Constants.prop_img, (600, 20))
            # write on the amount of the item and his photo
            if Constants.day:
                text_type_name = self.font.render('1x', True, Constants.BLACK)
            else:
                text_type_name = self.font.render('1x', True, Constants.WHITE)
            screen.blit(text_type_name, (670, 40))
        # if the user collect the prop and do some delay with the move trash
        if Constants.collect_prop and round(Constants.time + 1) == round(Constants.score):
            Constants.move_trash = True

    def draw_bomb(self, screen):
        # check if the bomb need to show on the screen
        if Constants.bomb_show:
            # check if you have 1 bomb
            if Constants.num_bomb_1:
                screen.blit(Constants.bomb_img, (Constants.ran_bomb_x, Constants.starty_bomb_1))
            # check if you have 2 bombs
            if not Constants.num_bomb_1:
                screen.blit(Constants.bomb_img, (Constants.ran_bomb_x, Constants.starty_bomb_1))
                screen.blit(Constants.bomb_img, (Constants.ran_bomb_x2, Constants.starty_bomb_2))
        # draw the animation of the bomb if the player touch the bomb
        if Constants.bomb_touch:
            if Constants.count_bomb == 1:
                Constants.bomb_sound()
            if Constants.count_bomb <= 4:
                screen.blit(Constants.bomb_animation[Constants.count_bomb], (100, 20))
                pygame.time.delay(120)
                Constants.count_bomb += 1
            if Constants.count_bomb == 4:
                Constants.bomb_touch = False
                Constants.count_bomb = 0

    def move_prop(self):
        # if the character collected the item
        if Constants.startx == Constants.ran_prop_x and abs(
                Constants.starty_prop) == Constants.starty and not Constants.isJump:
            Constants.collect_prop = True
            Constants.show_prop = False

        # if the item appears so it will keep moving
        if Constants.show_prop:
            Constants.starty_prop += Constants.vel

        # if the character did not collect the item
        if Constants.starty_prop == 600 and not Constants.collect_prop:
            Constants.hearts -= 1
            Constants.fail_sound()
            Constants.starty_prop = -50
            Constants.show_prop = False

        # if there is no an item on the screen it random an item and trash to collect
        if not Constants.show_prop and Constants.score >= 1 and not Constants.collect_prop and not Constants.bomb_show:
            prop_loop = True
            while prop_loop:
                Constants.ran_prop_x = random.choice(Constants.list_route)
                ran_trash = random.randint(0, 2)
                if ran_trash == 0:
                    trash = "blue"
                elif ran_trash == 1:
                    trash = "orange"
                else:
                    trash = "purple"
                length_props = len(Constants.prop_list[ran_trash][trash])
                ran_prop = random.randint(0, length_props - 1)
                Constants.ran_prop_path = Constants.prop_list[ran_trash][trash][ran_prop]
                if len(Constants.prop_list_used) == 7:
                    Constants.prop_list_used = []
                if Constants.ran_prop_path not in Constants.prop_list_used:
                    prop_loop = False
                Constants.prop_list_used.append(Constants.ran_prop_path)
                Constants.prop_img = pygame.image.load(Constants.ran_prop_path)
                Constants.show_prop = True

    def move_bomb(self):
        # if the current level is equal to the drawn level and there is no object that needs to be recycled the bomb is
        # activated
        if Constants.level == Constants.ran_level and Constants.starty_trash == -475 and not Constants.show_prop and not Constants.collect_prop:
            Constants.bomb_show = True
            Constants.choose_num_bomb = True
        # if the current level is equal to the drawn level the bomb is not activated
        elif Constants.level != Constants.ran_level:
            Constants.bomb_show = False
            Constants.choose_num_bomb = False
            Constants.ran_bomb_x = 0
            Constants.ran_bomb_x2 = 0
        # when the bomb appears, draw a new level to show the bomb
        if Constants.ran_level == Constants.level - 1:
            Constants.min_level_ran = Constants.max_level_ran
            Constants.max_level_ran += 2
            Constants.ran_level = random.randint(Constants.min_level_ran, Constants.max_level_ran)
        # if the bomb is activated, this choosing the number of the bombs
        if Constants.choose_num_bomb:
            if Constants.ran_bomb_x == 0 and Constants.ran_bomb_x2 == 0:
                ran_num_bomb = random.randint(1, 2)
                if ran_num_bomb == 1:
                    Constants.num_bomb_1 = True
                    Constants.ran_bomb_x = random.choice(Constants.list_route)
                if ran_num_bomb == 2:
                    bomb_speed = [1, 2]
                    Constants.speed_bomb_1 = random.choice(bomb_speed)
                    Constants.speed_bomb_2 = random.choice(bomb_speed)
                    Constants.num_bomb_1 = False
                    Constants.ran_bomb_x = random.choice(Constants.list_route)
                    same_x = True
                    while same_x:
                        Constants.ran_bomb_x2 = random.choice(Constants.list_route)
                        if Constants.ran_bomb_x != Constants.ran_bomb_x2:
                            same_x = False
            Constants.bomb_active = True
            Constants.bomb_show = True
            Constants.choose_num_bomb = False
        # if bomb is activated the bomb moving by the vel
        if Constants.bomb_active:
            if Constants.num_bomb_1:
                Constants.starty_bomb_1 += Constants.vel * Constants.speed_bomb_1
            elif not Constants.num_bomb_1:
                Constants.starty_bomb_1 += Constants.vel * Constants.speed_bomb_1
                Constants.starty_bomb_2 += Constants.vel * Constants.speed_bomb_2
        # if one bomb is activated
        if Constants.num_bomb_1:
            # if the bomb pass the character
            if Constants.starty_bomb_1 > 600:
                Constants.starty_bomb_1 = 30
                Constants.starty_bomb_2 = 30
                Constants.bomb_show = False
                Constants.bomb_active = False
            # if the character hit the bomb
            if Constants.startx == Constants.ran_bomb_x and Constants.starty == Constants.starty_bomb_1 and not Constants.isJump:
                Constants.bomb_sound()
                Constants.bomb_touch = True
                Items().draw_bomb(Constants.screen)
                answer_for_ques = Questions(Constants.used_ques, Constants.SCREEN_HEIGHT,
                                            Constants.SCREEN_WIDTH).draw_questions()
                # check the answer and draw it
                Questions(Constants.used_ques, Constants.SCREEN_HEIGHT, Constants.SCREEN_WIDTH).draw_ans(
                    answer_for_ques)
                if not answer_for_ques:
                    Constants.hearts -= 1
                    Constants.fail_sound()
                Constants.starty_bomb_1 = 30
                Constants.starty_bomb_2 = 30
                Constants.bomb_show = False
                Constants.bomb_active = False

        # if two bombs are activated
        if not Constants.num_bomb_1:
            # if the bomb pass the character
            if Constants.starty_bomb_1 > 600 and Constants.starty_bomb_2 > 600:
                Constants.starty_bomb_1 = 30
                Constants.starty_bomb_2 = 30
                Constants.bomb_show = False
                Constants.bomb_active = False
            # if the character hit the bomb number one
            if Constants.startx == Constants.ran_bomb_x and Constants.starty == Constants.starty_bomb_1 and not Constants.isJump:
                Constants.bomb_sound()
                Constants.bomb_touch = True
                Items().draw_bomb(Constants.screen)
                answer_for_ques = Questions(Constants.used_ques, Constants.SCREEN_HEIGHT,
                                            Constants.SCREEN_WIDTH).draw_questions()
                # check the answer and draw it
                Questions(Constants.used_ques, Constants.SCREEN_HEIGHT, Constants.SCREEN_WIDTH).draw_ans(
                    answer_for_ques)
                if not answer_for_ques:
                    Constants.hearts -= 1
                    Constants.fail_sound()
                Constants.starty_bomb_1 = 30
                Constants.starty_bomb_2 = 30
                Constants.bomb_show = False
                Constants.bomb_active = False
            # if the character hit the bomb number two
            if Constants.startx == Constants.ran_bomb_x2 and Constants.starty == Constants.starty_bomb_2 and not Constants.isJump:
                Constants.bomb_sound()
                Constants.bomb_touch = True
                Items().draw_bomb(Constants.screen)
                answer_for_ques = Questions(Constants.used_ques, Constants.SCREEN_HEIGHT,
                                            Constants.SCREEN_WIDTH).draw_questions()
                # check the answer and draw it
                Questions(Constants.used_ques, Constants.SCREEN_HEIGHT, Constants.SCREEN_WIDTH).draw_ans(
                    answer_for_ques)
                if not answer_for_ques:
                    Constants.hearts -= 1
                    Constants.fail_sound()
                Constants.starty_bomb_1 = 30
                Constants.starty_bomb_2 = 30
                Constants.bomb_show = False
                Constants.bomb_active = False
