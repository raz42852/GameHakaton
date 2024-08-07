import Constants
import pygame
import random


class Menu():
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("arialblack", 40)

    def menu_run(self):
        # game loop
        while Constants.run_menu:
            self.screen.fill(Constants.BLUE)  # (52, 78, 91)
            # check if game is paused
            if Constants.game_paused or not Constants.game_running:
                # check menu state
                self.screen.blit(Constants.logo_img, (10, -20))
                if Constants.menu_state == "main":
                    # draw start screen button
                    if not Constants.game_running:
                        if Constants.start_button.draw(self.screen):
                            Constants.click_sound()
                            Constants.menu_state = "Type_name"
                    # draw pause screen button
                    if Constants.game_running:
                        if Constants.resume_button.draw(self.screen):
                            Constants.click_sound()
                            Constants.game_paused = False
                            break
                    # draw how to play screen button
                    if Constants.how_to_play_button.draw(self.screen):
                        Constants.click_sound()
                        Constants.menu_state = "how_to_play"
                    # draw options screen button
                    if Constants.options_button.draw(self.screen):
                        Constants.click_sound()
                        Constants.menu_state = "options"
                    # draw quit screen button
                    if Constants.quit_button.draw(self.screen):
                        Constants.click_sound()
                        Constants.run_menu = False
                        Constants.terminate()
                # check if the how to play is open
                if Constants.menu_state == "how_to_play":
                    self.screen.blit(Constants.how_to_play_exp, (0, 0))
                    # draw back screen button
                    if Constants.back2_button.draw(self.screen):
                        Constants.click_sound()
                        Constants.menu_state = "main"
                # check if the options menu is open
                if Constants.menu_state == "options":
                    # draw audio settings screen button
                    if Constants.audio_button.draw(self.screen):
                        Constants.click_sound()
                        Menu(Constants.screen).music()
                    # draw back screen button
                    if Constants.back_button.draw(self.screen):
                        Constants.click_sound()
                        Constants.menu_state = "main"
                # check if the type name is open
                if Constants.menu_state == "Type_name":
                    self.screen.fill(Constants.BLUE)  # (52, 78, 91)
                    Menu(Constants.screen).input_name()
                # check if the choose character is open
                if Constants.menu_state == "Choose_char":
                    self.screen.fill(Constants.BLUE)
                    text_choose = self.font.render('Choose boy or girl : ', True, Constants.BLACK)
                    self.screen.blit(text_choose, (200, 30))
                    # draw boy screen button
                    if Constants.boy_button.draw(self.screen):
                        Constants.click_sound()
                        Constants.game_running = True
                        Constants.menu_state = "main"
                        Constants.Male_choose = True
                        break
                    # draw girl screen button
                    if Constants.girl_button.draw(self.screen):
                        Constants.click_sound()
                        Constants.game_running = True
                        Constants.menu_state = "main"
                        Constants.Female_choose = True
                        break
            # event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Constants.terminate()

            pygame.display.update()

    def music(self):
        pygame.display.set_caption("Main Menu")
        # Set up the volume slider
        slider_x = 320
        slider_y = 200
        slider_width = 200
        slider_height = 20
        slider_knob_radius = 10
        slider_knob_x = slider_x + int(slider_width * pygame.mixer.music.get_volume())
        slider_knob_y = slider_y + int(slider_height / 2)
        dragging = False

        def draw_slider():
            # Draw the slider track
            pygame.draw.rect(self.screen, Constants.BLACK, (slider_x, slider_y, slider_width, slider_height), 2)
            # Draw the slider knob
            pygame.draw.circle(self.screen, Constants.BLACK, (slider_knob_x, slider_knob_y), slider_knob_radius)

        def update_volume():
            # Update the music volume based on the slider position
            volume = (slider_knob_x - slider_x) / slider_width
            pygame.mixer.music.set_volume(volume)

        # Main game loop
        running_music = True
        while running_music:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Constants.terminate()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Check if the user clicked on the slider knob
                    if pygame.Rect(slider_knob_x - slider_knob_radius, slider_knob_y - slider_knob_radius,
                                   slider_knob_radius * 2, slider_knob_radius * 2).collidepoint(event.pos):
                        dragging = True
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    dragging = False
                elif event.type == pygame.MOUSEMOTION and dragging:
                    # Move the slider knob
                    slider_knob_x = min(max(event.pos[0], slider_x), slider_x + slider_width)
                    update_volume()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                running_music = False
            # Clear the screen
            self.screen.fill(Constants.WHITE)

            if Constants.back2_button.draw(self.screen):
                Constants.click_sound()
                Constants.menu_state = "options"
                break
            # Draw the slider
            draw_slider()

            # Draw the music title
            sound_file_text = self.font.render('Music', True, Constants.BLACK)
            self.screen.blit(sound_file_text, (350, 70))

            # Update the screen
            pygame.display.flip()

    def input_name(self):
        user_name_check = ""
        name_taken_bool = False
        name_valid_bool = False
        base_font = pygame.font.Font(None, 32)
        input_rect = pygame.Rect(200, 160, 400, 32)
        color_active = (127, 0, 255)
        color_passive = Constants.BLACK
        input_name_run = True
        # input run loop
        while input_name_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Constants.terminate()
                # if the user want to type a name
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        Constants.active = True
                    else:
                        Constants.active = False
                # if the user typed a character
                if event.type == pygame.KEYDOWN:
                    if Constants.active:
                        # if the user wat to remove a character
                        if event.key == pygame.K_BACKSPACE:
                            Constants.user_name = Constants.user_name[:-1]
                        else:
                            Constants.user_name += event.unicode
                    # if event.key == pygame.K_ESCAPE or event.key == pygame.K_TAB:            Optional
                    # user_name = user_name[:-1]
                    # if the username is more than one character
                    if len(Constants.user_name) > 1:
                        if event.key == pygame.K_RETURN:
                            Constants.user_name = Constants.user_name[:-1]
                            Constants.active = False
            self.screen.fill(Constants.BLUE)
            # enter on the screen a command
            text_type_name = self.font.render('Enter your name : ', True, Constants.BLACK)
            self.screen.blit(text_type_name, (200, 60))
            # if the username is more than one character
            if len(Constants.user_name) > 1:
                # put save button
                if Constants.save_button.draw(self.screen):
                    Constants.click_sound()
                    # check if the name already taken
                    if Menu(Constants.screen).check_name_taken(Constants.user_name):
                        user_name_check = Constants.user_name
                        name_taken_bool = True
                    # check if the name build from only numbers
                    elif Constants.user_name.isnumeric():
                        user_name_check = Constants.user_name
                        name_valid_bool = True
                    # if the name is good
                    else:
                        input_name_run = False
                        Constants.menu_state = "Choose_char"
            # put a message if the name taken
            if name_taken_bool:
                text_name_taken = self.font.render('The name ' + Constants.user_name + ' already taken', True,
                                                   Constants.BLACK)
                self.screen.blit(text_name_taken, (100, 250))
                if user_name_check != Constants.user_name:
                    name_taken_bool = False
            # put a message if the name is illegal
            if name_valid_bool:
                text_name_valid = self.font.render('The name ' + Constants.user_name + ' is illegal', True,
                                                   Constants.BLACK)
                self.screen.blit(text_name_valid, (120, 250))
                if user_name_check != Constants.user_name:
                    name_valid_bool = False
            # if the user want to type
            if Constants.active:
                color = color_active
            else:
                color = color_passive
            pygame.draw.rect(self.screen, color, input_rect, 2)
            text_surface = base_font.render(Constants.user_name, True, color)
            self.screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

            input_rect.w = max(400, text_surface.get_width() + 10)

            pygame.display.flip()

    def check_name_taken(self, user_name):
        # check if the name in the text file
        with open("Names & Score.txt", "r") as file:
            for line in file:
                if user_name in line:
                    return True
            return False

    def switch_song(self):
        # if all the songs have been used, then play them all over again
        if len(Constants.list_songs) == len(Constants.used_songs):
            Constants.used_songs = []
        # if the song end it move the next one
        if not pygame.mixer.music.get_busy():
            cnt = 0
            while cnt == 0:
                Constants.ran_song = random.randint(0, Constants.length_songs - 1)
                if Constants.list_songs[Constants.ran_song] not in Constants.used_songs:
                    Constants.used_songs.append(Constants.list_songs[Constants.ran_song])
                    Constants.curr_song = Constants.list_songs[Constants.ran_song]
                    Constants.music_file_path = Constants.curr_song
                    pygame.mixer.music.load(Constants.music_file_path)
                    pygame.mixer.music.play()
                    cnt = 1

    def end_game(self):
        scoreSurf = self.font.render('Your score is : %s' % int(Constants.score), True, Constants.WHITE)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (200, 10)
        recordSurf = self.font.render('Table of records : ', True, Constants.BLACK)
        recordRect = recordSurf.get_rect()
        recordRect.topleft = (200, 50)
        run_end = True
        Constants.insert_details_file()
        while run_end:
            self.screen.fill(Constants.BLUE)
            self.screen.blit(scoreSurf, scoreRect)
            self.screen.blit(recordSurf, recordRect)
            Constants.write_table()
            # (52, 78, 91)
            # draw quit screen button
            if Constants.quit_button.draw(self.screen):
                Constants.click_sound()
                Constants.terminate()

            # event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Constants.terminate()
            pygame.display.update()
