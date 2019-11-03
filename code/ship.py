"""
Class of the "spaceship" object.

"""
import arcade as acd
from code import settings as st
import math

# Global list of projectile positions and directions.
projectile_list = []


class PlayerShip:
    """
    Logic for movement of ship. Notice that the class does not manipulate velocity. Only position.
    Velocity manipulation is done in the main file.

    """

    def __init__(self, x, y, velocity, angle):
        self.x = x
        self.y = y
        self.vel = velocity
        self.angle = angle

    def draw(self):
        # Rendering ship texture at given (x, y) coordinate, height, width, and angle.
        acd.draw_texture_rectangle(
            self.x, self.y,
            st.PLAYER_SHIP_WIDTH, st.PLAYER_SHIP_HEIGHT,
            st.PLAYER_SHIP_TEXTURE, self.angle
        )

    def translation(self):
        # Notice 90 degrees is added to the angle to compensate for the fact
        # that 0 degrees points the ship north (on a "regular" cartesian system 0 degrees is east).
        # Adds correct quantities of xy-values at the current velocity to allow non-axis movement.
        self.x += math.cos(math.radians(self.angle + 90)) * self.vel
        self.y += math.sin(math.radians(self.angle + 90)) * self.vel

    def shoot(self):  # Manages position and rendering of projectiles.
        # The initial (x, y) position of the projectile.
        x = math.cos(math.radians(self.angle + 90)) + self.x
        y = math.sin(math.radians(self.angle + 90)) + self.y

        # (step_x, step_y) acts as a direction vector for the projectile. It stays constant.
        step_x = math.cos(math.radians(self.angle + 90)) * st.PROJECTILE_SPEED
        step_y = math.sin(math.radians(self.angle + 90)) * st.PROJECTILE_SPEED

        # The orientation of the projectile.
        angle = self.angle

        # Adding data to projectile list.
        projectile_list.append([x, y, step_x, step_y, angle])

    def draw_projectiles(self, camera=False):  # No matter what, projectiles are always on screen and moving.
        for p in projectile_list:  # Moving and rendering the projectiles using projectile list.

            # Conditions for out-of-viewport projectile.
            x_out = p[0] < 0 or p[0] > st.SCREEN_WIDTH
            y_out = p[1] < 0 or p[1] > st.SCREEN_HEIGHT

            # Projectile removal is different when camera tracks ship.
            if camera:
                x_out = p[0] < self.x - st.SCREEN_WIDTH / 2 or p[0] > self.x + st.SCREEN_WIDTH / 2
                y_out = p[1] < self.y - st.SCREEN_HEIGHT / 2 or p[1] > self.y + st.SCREEN_HEIGHT / 2

            # Checking if a projectile moves out of the viewport. If so, it is removed.
            if x_out or y_out:
                projectile_list.pop(0)

            p[0] += p[2]  # Increase x by x_step.
            p[1] += p[3]  # Increase y by y_step.
            acd.draw_rectangle_filled(p[0], p[1], st.PROJECTILE_WIDTH, st.PROJECTILE_HEIGHT, st.PROJECTILE_COLOR, p[4])

    def get_velocity(self):
        return self.vel

    def get_pos(self):
        return self.x, self.y
