# Game settings
import arcade as acd

# Window constants.
SCREEN_WIDTH = 825
SCREEN_HEIGHT = 825
SCREEN_TITLE = "Asteroids!"
MAX_FRAME_RATE = 60  # This is actually the maximum for the arcade library.
BACKGROUND_COLOR = (0, 0, 0)  # Black

# There is no color for ship as it is a texture.
PLAYER_SHIP_SPEED = 2
PLAYER_SHIP_WIDTH = 30
PLAYER_SHIP_HEIGHT = 50
PLAYER_SHIP_SAFE_RADIUS = 100  # The radius around the ship in which asteroids cannot spawn.

# Texture. It's easier to manipulate this texture than define a 3-point triangle
PLAYER_SHIP_TEXTURE = acd.load_texture("code/space_ship.png")

# These do not have the "PLAYER" because they apply to all ships (which may be added in the future).
SHIP_TURN_SPEED = 5
SHIP_ACCELERATION = 1
SHIP_DECELERATION = 0.2
SHIP_TERMINAL_SPEED = 20

# Projectile constants.
PROJECTILE_SPEED = 20
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
ASTEROID_NUM_CAP = 10  # I love playing with this.

# Controls are WASD or Arrow Keys and Space Bar. There is no "down" (moving backwards).
W = acd.key.W
A = acd.key.A
D = acd.key.D

UP = acd.key.UP
LEFT = acd.key.LEFT
RIGHT = acd.key.RIGHT

SPACE = acd.key.SPACE
