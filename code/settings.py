# Game settings
import arcade as acd
import os

# Window constants.
SCREEN_WIDTH = 825
SCREEN_HEIGHT = 825
SCREEN_TITLE = "Asteroids!"
MAX_FRAME_RATE = 60  # This is actually the maximum for the arcade library.
BACKGROUND_COLOR = (255, 255, 255)  # White

# There is no color for ship as it is a texture.
PLAYER_SHIP_SPEED = 2
PLAYER_SHIP_WIDTH = 50
PLAYER_SHIP_HEIGHT = 50

# Getting path of assets directory
dir_path = (os.getcwd().replace("\\", "/")).replace("code", "/assets/")
PLAYER_SHIP_TEXTURE = acd.load_texture(dir_path + "space_ship.png")

# These do not have the "PLAYER" because they apply to all ships (which may be added in the future).
SHIP_TURN_SPEED = 3
SHIP_ACCELERATION = 1
SHIP_DECELERATION = 0.5
SHIP_TERMINAL_SPEED = 10

# Projectile constants.
PROJECTILE_SPEED = 8
PROJECTILE_WIDTH = 4
PROJECTILE_HEIGHT = 10
PROJECTILE_COLOR = (255, 0, 0)  # Red

# Asteroid constants. This will be longer than the others as everything is randomised on a custom range.
# The number of segments is in range [ASTEROID_SEGMENT_LOWER, ASTEROID_SEGMENT_UPPER).
ASTEROID_SEGMENT_LOWER = 4
ASTEROID_SEGMENT_UPPER = 9
# The width and length of an asteroid are in range [ASTEROID_SIZE_LOWER, ASTEROID_SIZE_UPPER).
ASTEROID_SIZE_UPPER = 50
ASTEROID_SIZE_LOWER = 25
# The velocity of an asteroid are in range [ASTEROID_VEL_LOWER, ASTEROID_VEL_UPPER).
ASTEROID_VEL_UPPER = 2
ASTEROID_VEL_LOWER = -2
# The rotational of an asteroid are in range [ASTEROID_ROTA_LOWER, ASTEROID_ROTA_UPPER).
ASTEROID_ROTA_UPPER = 3
ASTEROID_ROTA_LOWER = -3
# Notice there is no (x, y) position range because it may vary depending in ship position.
ASTEROID_COLOR = (100, 100, 100)  # Gray
# The maximum number of asteroids allowed on screen at once.
ASTEROID_NUM_CAP = 10

# Controls are WASD or Arrow Keys and Space Bar.
W = acd.key.W
A = acd.key.A
S = acd.key.S
D = acd.key.D

Up = acd.key.UP
Left = acd.key.LEFT
Down = acd.key.DOWN
Right = acd.key.RIGHT

Space = acd.key.SPACE
