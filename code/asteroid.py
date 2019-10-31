"""
Class of asteroid object.

"""

import arcade as acd
from code import settings as st
from code import main
import random as rnd

asteroid_list = []


class Asteroids:
    def __init__(self, ship_pos):
        # (x, y) position is randomized based in player ship position.
        self.sp = int(ship_pos[0]), int(ship_pos[1])

        self.x = rnd.randint(self.sp[0] - st.SCREEN_WIDTH // 2,
                             self.sp[0] + st.SCREEN_WIDTH // 2)

        self.y = rnd.randint(self.sp[1] - st.SCREEN_HEIGHT // 2,
                             self.sp[1] + st.SCREEN_HEIGHT // 2)

        # Velocity, angle, segment number, and size are randomized.
        self.vel_x = rnd.randint(st.ASTEROID_VEL_LOWER, st.ASTEROID_VEL_UPPER)
        self.vel_y = rnd.randint(st.ASTEROID_VEL_LOWER, st.ASTEROID_VEL_UPPER)
        self.rota_vel = rnd.randint(st.ASTEROID_ROTA_LOWER, st.ASTEROID_ROTA_UPPER)
        self.angle = rnd.randint(0, 360)  # [0 degrees, 360 degrees).

        self.segments = rnd.randint(st.ASTEROID_SEGMENT_LOWER, st.ASTEROID_SEGMENT_UPPER)
        self.size = rnd.randint(st.ASTEROID_SIZE_LOWER, st.ASTEROID_SIZE_UPPER)

    def load(self):
        # Appending all asteroids onto the asteroid list.
        if len(asteroid_list) < st.ASTEROID_NUM_CAP:
            # A dictionary would be nice in this situation. But, I don't want to use one.
            asteroid_list.append([self.x, self.y, self.vel_x, self.vel_y,
                                  self.rota_vel, self.angle, self.segments, self.size])
            print(asteroid_list)

    # TODO: fix buggy asteroids.
    def draw(self, camera=False):
        # Notice this is the same technique used for projectile drawing.
        for a in asteroid_list:  # Moving and rendering the asteroids using asteroid list.
            # Conditions for out-of-viewport asteroid.
            x_out = a[0] < 0 or a[0] > st.SCREEN_WIDTH
            y_out = a[1] < 0 or a[1] > st.SCREEN_HEIGHT

            # Asteroid removal is different when camera tracks ship.
            if camera:
                x_out = a[0] < self.x - st.SCREEN_WIDTH / 2 or a[0] > self.x + st.SCREEN_WIDTH / 2
                y_out = a[1] < self.y - st.SCREEN_HEIGHT / 2 or a[1] > self.y + st.SCREEN_HEIGHT / 2

            # Checking if a asteroid moves out of the viewport. If so, it is removed.
            if x_out or y_out:
                asteroid_list.pop(-1)

            a[0] += a[2]  # x-movement.
            a[1] += a[3]  # y-movement.
            a[5] += a[4]  # rotation.

            acd.draw_ellipse_filled(a[0], a[1], a[7], a[7], st.ASTEROID_COLOR, a[5], a[6])
