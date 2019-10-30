# Game settings
import arcade as acd

SCREEN_WIDTH = 825
SCREEN_HEIGHT = 825
SCREEN_TITLE = "Asteroids!"
MAX_FRAME_RATE = 60
BACKGROUND_COLOR = (255, 255, 255)  # White

# There is no color for ship as it is a texture.
PLAYER_SHIP_SPEED = 2
PLAYER_SHIP_WIDTH = 50
PLAYER_SHIP_HEIGHT = 50
PLAYER_SHIP_TEXTURE = acd.load_texture("assets/space_ship.png")

# These do not have the "PLAYER" because they apply to all ships (which may be added in the future).
SHIP_TURN_SPEED = 3
SHIP_ACCELERATION = 1
SHIP_DECELERATION = 0.5
SHIP_TERMINAL_SPEED = 10

PROJECTILE_SPEED = 10
PROJECTILE_WIDTH = 5
PROJECTILE_HEIGHT = 5
PROJECTILE_COLOR = (0, 0, 0)  # Black

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
