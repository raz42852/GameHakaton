import pygame
import random
import Button

# create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# define fonts
font_size = 32

list_songs = ['songs\song1.mp3', 'songs\song2.mp3', 'songs\song3.mp3', 'songs\song4.mp3']
length_songs = len(list_songs)
ran_song = random.randint(0, length_songs - 1)
curr_song = list_songs[ran_song]
used_songs = []
used_songs.append(list_songs[ran_song])
music_file_path = curr_song

# game variables
run_menu = True
run_end = False
game_running = False
game_paused = False
menu_state = "main"
user_name = ""
active = False
Male_choose = False
Female_choose = False
night = False
day = True
FPS = 40

startx = 360
starty = 500
vel = 5
isJump = False
jumpCount = 10
score = 0
bomb_touch = False
bomb_show = False
bomb_active = False
count_bomb = 0
num_bomb_1 = False
ran_bomb_x = 0
ran_bomb_x2 = 0
speed_bomb_1 = 1
speed_bomb_2 = 1
choose_num_bomb = False
starty_bomb_1 = 30
starty_bomb_2 = 30
min_level_ran = 5
max_level_ran = 7
ran_level = random.randint(min_level_ran, max_level_ran)
level = 1
show_prop = False
ran_prop_x = 0
prop_img = ""
collect_prop = False
move_trash = False
hearts = 5
prop_in = False
ran_prop_path = ""
time = 0

starty_prop = -50
starty_trash = -475
walkCount = 0

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLUE = (0, 255, 255)
TEXT_COL = (255, 255, 255)

# load button images
start_img = pygame.image.load("images/button_start.png").convert_alpha()
how_to_play_img = pygame.image.load("images/button_howtoplay.png").convert_alpha()
resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
options_img = pygame.image.load("images/button_options.png").convert_alpha()
quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
audio_img = pygame.image.load('images/button_audio.png').convert_alpha()
save_img = pygame.image.load('images/button_save.png').convert_alpha()
back_img = pygame.image.load('images/button_back.png').convert_alpha()
boy_img = pygame.image.load('images/button_boy.png').convert_alpha()
girl_img = pygame.image.load('images/button_girl.png').convert_alpha()
logo_img = pygame.image.load('images/LOGO.PNG').convert_alpha()

# create button instances
start_button = Button.Button(285, 60, start_img, 1)
how_to_play_button = Button.Button(240, 250, how_to_play_img, 1)
resume_button = Button.Button(304, 150, resume_img, 1)
options_button = Button.Button(297, 375, options_img, 1)
quit_button = Button.Button(336, 500, quit_img, 1)
audio_button = Button.Button(225, 140, audio_img, 1)
save_button = Button.Button(115, 325, save_img, 1)
back_button = Button.Button(332, 425, back_img, 1)
back2_button = Button.Button(150, 500, back_img, 1)
boy_button = Button.Button(500, 125, boy_img, 1)
girl_button = Button.Button(100, 125, girl_img, 1)

running_male = [pygame.image.load('game\l1m.png'), pygame.image.load('game\l2m.png'), pygame.image.load('game\l3m.png')]

running_female = [pygame.image.load('game\l1f.png'), pygame.image.load('game\l2f.png'),
                  pygame.image.load('game\l3f.png')]

bg = pygame.image.load('game\ibg.jpg')
bg_left_day = pygame.image.load('game\sky_cloud_left.png')
bg_right_day = pygame.image.load('game\sky_sun_right.png')
bg_left_night = pygame.image.load('game\sky_moon_left.png')
bg_right_night = pygame.image.load('game\sky_night_right.png')

how_to_play_exp = pygame.image.load('images/how_to_play.jpg')
background_y = 0
speed = 3

heart_img = pygame.image.load('game/heart.png')

bomb_animation = [pygame.image.load('game/explosienl1.png'), pygame.image.load('game/explosienl2.png'),
                  pygame.image.load('game/explosienl3.png'), pygame.image.load('game/explosienl4.png'),
                  pygame.image.load('game/explosienl5.png')]

bomb_img = pygame.image.load('game/bomb.png')

trash_orange_img = pygame.image.load('game/trash_orange.png')
trash_purple_img = pygame.image.load('game/trash_purple.png')
trash_blue_img = pygame.image.load('game/trash_blue.png')

prop_list = [{"blue": ["game/eggs_blue.png", "game/newspaper_blue.png"]},
             {"orange": ["game/bag_orange.png", "game/milk_orange.png", "game/soap_bottle_orange.png",
                         "game/tin_can_orange.png"]},
             {"purple": ["game/glass_cup_purple.png", "game/glass_jar_purple.png"]}]

prop_list_used = []

list_route = [230, 360, 490]

used_ques = []

# Define the questions and answers
QUESTIONS = [
    {
        "question": "Which of the following is not one of the main materials recycled in Israel?",
        "answers": ["Glass", "Plastic", "Paper", "Styrofoam"],
        "correct_answer": 3
    },
    {
        "question": "What is the penalty for not separating recyclables in Israel?",
        "answers": ["A warningc", "A fine", "Community service", "Imprisonment"],
        "correct_answer": 1
    },
    {
        "question": "What percentage of municipal waste in Israel is recycled?",
        "answers": ["15%", "25%", "35%", "45%"],
        "correct_answer": 1
    },
    {
        "question": "What is the name of the bottle deposit system in Israel?",
        "answers": ["Tmura", "Shvil", "Kupat Cholim", "Zionut"],
        "correct_answer": 0
    },
    {
        "question": "What is the name of the recycling symbol in Hebrew?",
        "answers": ["Cheshbon", "Shikma", "Keshet", "Zman"],
        "correct_answer": 1
    },
    {
        "question": "Which of the following items is not accepted for recycling in Israel?",
        "answers": ["Plastic bottles", "Aluminum cans", "Paper products", "Disposable diapers"],
        "correct_answer": 3
    },
    {
        "question": "Can plastic bags be recycled in Israel?",
        "answers": ["Yes", "No", "Only in designated drop-off locations", "It depends on the type of plastic"],
        "correct_answer": 2
    },
    {
        "question": "What is the main reason for Israel's low recycling rate?",
        "answers": ["Lack of government support", "Lack of public awareness", "Lack of recycling infrastructure",
                    "All of the above"],
        "correct_answer": 3
    },
    {
        "question": "Which of the following is not a benefit of recycling in Israel?",
        "answers": ["Conserving natural resources", "Reducing landfill waste", "Generating revenue for the government",
                    "Decreasing greenhouse gas emissions"],
        "correct_answer": 2
    },
    {
        "question": "What is the name of the Israeli company that produces recycled paper products?",
        "answers": ["Hadera Paper", "Green Paper", "Aviv Recycling", "Tzora Paper"],
        "correct_answer": 0
    },
    {
        "question": "Which of the following is not a type of waste that can be composted in Israel?",
        "answers": ["Vegetable scraps", "Eggshells", "Meat and dairy products", "Yard waste"],
        "correct_answer": 2
    },
    {
        "question": "What is the name of the Israeli program that collects used batteries for recycling?",
        "answers": ["PowerCycle", "Battery Collection Israel", "Eco-Battery", "Green Batteries"],
        "correct_answer": 0
    },
    {
        "question": "Which of the following is not a factor that affects Israel's recycling rate?",
        "answers": ["Population density", "Geographic location", "Political stability",
                    "Availability of recycling infrastructure"],
        "correct_answer": 2
    },
    {
        "question": "What materials should be placed in the green recycling bin in Israel?",
        "answers": ["Food waste", "Plastic bottles", "Glass bottles", "Hazardous waste"],
        "correct_answer": 1
    },
    {
        "question": "What materials should be placed in the blue recycling bin in Israel?",
        "answers": ["Paper", "Glass jars", "Aluminum cans", "Food waste"],
        "correct_answer": 0
    },
    {
        "question": "What materials should be placed in the gray bin for general waste in Israel?",
        "answers": ["Plastic bags", "Metal cans", "Glass bottles", "All of the above"],
        "correct_answer": 3
    },
    {
        "question": "What materials should be placed in the brown bin for organic waste in Israel?",
        "answers": ["Vegetable scraps", "Eggshells", "Meat and dairy products", "All of the above"],
        "correct_answer": 3
    }
]


def bomb_sound():
    bomb_sound_path = pygame.mixer.Sound('sounds/bomb.mp3')
    bomb_sound_path.play()


def click_sound():
    click_sound_path = pygame.mixer.Sound('sounds/button.mp3')
    click_sound_path.play()


def fail_sound():
    bomb_sound_path = pygame.mixer.Sound('sounds/fail.mp3')
    bomb_sound_path.play()


def terminate():
    pygame.quit()


def time_screen(time):
    x = 0
    while x < time:
        x += 1
        pygame.time.delay(1000)


def insert_details_file():
    global user_name, score
    # Write to a file
    with open("Names & Score.txt", "a") as file:
        file.write("{} {}\n".format(user_name, int(score)))


def write_table():
    global score
    # Read from the file and sort the scores
    with open("Names & Score.txt", "r") as file:
        scores = [line.split() for line in file if len(line.split()) == 2]
        sorted_scores = sorted(scores, key=lambda x: int(x[1]), reverse=True)

    # Output the top 10 scores in order of most points up and least points down
    font = pygame.font.SysFont("arialblack", 40)
    top_scores = sorted_scores[:10]
    y = 90
    for i, (name, score) in enumerate(top_scores):
        text = font.render("{}: {}".format(name, score), True, (0, 0, 0))
        screen.blit(text, (200, y))
        y += font_size + 7
