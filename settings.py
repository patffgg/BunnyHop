# game options/settings
TITLE = "Jumpy!"
WIDTH = 480
HEIGHT = 600
FPS = 60
FONT_NAME = 'arial'
HS_FILE = "highscore.txt"
#SPRITESHEET = "spritesheet_jumper.png"



#PADDLE_WIDTH = 100
#PADDLE_HEIGHT = 20
#PADDLE_COLOR = WHITE
#PADDLE_ACC = 1.2
#PADDLE_FRICTION = -0.1

#BALL_SIZE = 15
#BALL_COLOR = WHITE
#BALL_SPEED = 9

#BRICK_WIDTH = 50
#BRICK_HEIGHT = 20
#BRICK_ROWS = 5
#BRICK_COLS = 14
#BRICK_SPACING = 5
#BRICK_COLOR = [BLUE, GREEN, YELLOW, ORANGE, RED]

# Player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 20

# Game properties
#BOOST_POWER = 60
#POW_SPAWN_PCT = 7
#MOB_FREQ = 5000
#PLAYER_LAYER = 2
#PLATFORM_LAYER = 1
#POW_LAYER = 1
#MOB_LAYER = 2
#CLOUD_LAYER = 0

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 60),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4 - 50),
                 (125, HEIGHT - 350),
                 (350, 200),
                 (175, 100)]

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
BGCOLOR = LIGHTBLUE

