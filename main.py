import arcade as acd
from code import ship
from code import asteroid as ast
from code import settings as st
from code import camera as cam

# Player variables.
player_ship_pos = [st.SCREEN_WIDTH / 2, st.SCREEN_HEIGHT / 2]  # Ship spawns at screen center.
player_ship_angle = 0  # In degrees (ship points north at 0).
player_ship_velocity = 0
# Control variables.
moving_up = 0
moving_down = 0
moving_left = 0
moving_right = 0
shooting = 0


def update(delta_time):  # Might use delta_time in future for frame-rate independence.
    acd.start_render()  # Rendering starts here instead of deep within some other function.
    player_ship()
    asteroids()
    camera(delta_time)


def player_ship():
    global player_ship_angle, player_ship_velocity, player_ship_pos, shooting
    # Initializing, ship.
    p_ship = ship.PlayerShip(player_ship_pos[0], player_ship_pos[1], player_ship_velocity, player_ship_angle)

    # Shooting.
    p_ship.draw_projectiles(camera=True)  # Always draw and move projectiles.
    if shooting:
        p_ship.shoot()
        shooting = 0  # Shooting is reset so the ship fires semi-automatic.

    # Allowing ship to move and rendering.
    p_ship.draw()
    p_ship.translation()

    # Manipulating position variable.
    player_ship_pos = p_ship.get_pos()  # Updating positions.
    player_ship_velocity = p_ship.get_velocity()  # Updating velocity.

    if moving_up:  # Ship can't move backwards.
        if player_ship_velocity < st.SHIP_TERMINAL_SPEED:
            player_ship_velocity += st.SHIP_ACCELERATION

    # Deceleration of ship.
    if player_ship_velocity > 0:
        player_ship_velocity -= st.SHIP_DECELERATION
    if player_ship_velocity < 0:
        player_ship_velocity += st.SHIP_DECELERATION

    # Using the control variables.
    if moving_left:
        player_ship_angle += st.SHIP_TURN_SPEED
    if moving_right:
        player_ship_angle -= st.SHIP_TURN_SPEED


def asteroids():
    #  # Initializing, loading, drawing, and allowing asteroid movement.
    asts = ast.Asteroids(player_ship_pos)
    asts.load()
    asts.draw(camera=True)


def camera(dt):
    # Creating camera and tracking player.
    ship_cam = cam.Camera(player_ship_pos[0], player_ship_pos[1])
    ship_cam.track()

    # Drawing frame rate.
    cam_center = ship_cam.get_camera_center()
    fps_x = cam_center[0] - st.SCREEN_WIDTH / 2
    fps_y = cam_center[1] + st.SCREEN_HEIGHT / 2 - 20

    # Dividing 1 by time between frames (in seconds) to get FPS.
    acd.draw_text(f"{int(round(1 / dt))} FPS", fps_x, fps_y, acd.color.BLACK, 20)


# key_release() basically does the opposite of key_press().
def on_key_press(symbol, modifiers):
    global moving_up, moving_down, moving_left, moving_right, shooting
    # Rotation of ship.
    if symbol == st.LEFT or symbol == st.A:
        moving_left = 1
    if symbol == st.RIGHT or symbol == st.D:
        moving_right = 1
    # Translation of ship.
    if symbol == st.UP or symbol == st.W:
        moving_up = 1
    # Shoot.
    if symbol == st.SPACE:
        shooting = 1


def on_key_release(symbol, modifiers):
    global moving_up, moving_down, moving_left, moving_right, shooting
    # Rotation of ship.
    if symbol == st.LEFT or symbol == st.A:
        moving_left = 0
    if symbol == st.RIGHT or symbol == st.D:
        moving_right = 0
    # Translation of ship.
    if symbol == st.UP or symbol == st.W:
        moving_up = 0
    # Note there is no key release detection for space bar (shooting). It is reset every time a shot is made.
    # So, there is no need to know when space bar is released.


def main():
    # Opening window.
    acd.open_window(st.SCREEN_WIDTH, st.SCREEN_HEIGHT, st.SCREEN_TITLE)
    # Updating all functions in update() at a frame interval of 1 / 60 seconds between frames (60 FPS).
    acd.schedule(update, 1 / st.MAX_FRAME_RATE)
    # Setting background color.
    acd.set_background_color(st.BACKGROUND_COLOR)
    # Getting controls via arcade window commands file.
    window = acd.get_window()
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    # Running program.
    acd.run()


if __name__ == '__main__':
    main()