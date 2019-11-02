"""
Class of asteroid object.
"""

import arcade as acd
from code import settings as st
from code import ship
import random as rnd

asteroid_list = []


class Asteroids:
    def __init__(self, ship_pos):
        # (x, y) position is randomized based in player ship position.
        self.spf = ship_pos[0], ship_pos[1]
        self.spi = int(ship_pos[0]), int(ship_pos[1])

        # This whole chunk of code just makes sure that asteroids don't spawn in st.PLAYER_SHIP_SAFE_RADIUS of the ship.
        # TODO: Should be temporary, I don't like putting while loops in games.
        self.x = rnd.randint(self.spi[0] - st.SCREEN_WIDTH // 2,
                             self.spi[0] + st.SCREEN_WIDTH // 2)

        self.y = rnd.randint(self.spi[1] - st.SCREEN_HEIGHT // 2,
                             self.spi[1] + st.SCREEN_HEIGHT // 2)
        dist_from_ship = ((self.x - ship_pos[0]) ** 2 + (self.y - ship_pos[1]) ** 2) ** 0.5  # Good ol' Pythagoras.

        while dist_from_ship <= st.PLAYER_SHIP_SAFE_RADIUS:  # Keep resetting until asteroid is out of safe radius.
            self.x = rnd.randint(self.spi[0] - st.SCREEN_WIDTH // 2,
                                 self.spi[0] + st.SCREEN_WIDTH // 2)

            self.y = rnd.randint(self.spi[1] - st.SCREEN_HEIGHT // 2,
                                 self.spi[1] + st.SCREEN_HEIGHT // 2)

            dist_from_ship = ((self.x - ship_pos[0]) ** 2 + (self.y - ship_pos[1]) ** 2) ** 0.5  # Good ol' Pythagoras.

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
            # A dictionary would be nice in this situation. But, I don't want to use one. Time to memorize indices!
            asteroid_list.append([self.x, self.y, self.vel_x, self.vel_y,
                                  self.rota_vel, self.angle, self.segments, self.size])

    # TODO: Asteroids are flashing. Fix. Some projectiles are still there after collision.
    def exist(self, camera=False):  # "exist" ¯\_(ツ)_/¯
        # Notice this is the same technique used for projectile drawing.
        for a in asteroid_list:  # Moving and rendering the asteroids using asteroid list.
            # Conditions for out-of-viewport asteroid.
            x_out = a[0] < 0 or a[0] > st.SCREEN_WIDTH
            y_out = a[1] < 0 or a[1] > st.SCREEN_HEIGHT

            # Asteroid removal is different when camera tracks ship.
            if camera:
                x_out = a[0] < self.spf[0] - st.SCREEN_WIDTH / 2 or a[0] > self.spf[0] + st.SCREEN_WIDTH / 2
                y_out = a[1] < self.spf[1] - st.SCREEN_HEIGHT / 2 or a[1] > self.spf[1] + st.SCREEN_HEIGHT / 2

            # Checking if a asteroid moves out of the viewport. If so, it is removed.
            if x_out or y_out:
                asteroid_list.pop(list_find(asteroid_list, a))

            a[0] += a[2]  # x-movement.
            a[1] += a[3]  # y-movement.
            a[5] += a[4]  # rotation.

            acd.draw_ellipse_filled(a[0], a[1], a[7], a[7], st.ASTEROID_COLOR, a[5], a[6])

            # Collision detection ---
            # Since asteroids are more circular than rectangular, we will take its side length / 1.3 as a radius.
            # Circles are much easier to deal with for collision handling.
            rc = a[7] / 1.2  # Define radius of current asteroid.

            # We check that the distance of every other asteroid (from the current one) are not touching.
            for b in asteroid_list:
                if a != b:  # Make sure we aren't comparing an asteroid to itself.
                    ro = b[7] / 1.3  # Define radius of other asteroid.
                    dist = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5  # Good ol' Pythagoras.
                    touch_dist = rc + ro  # The distance for a collision is the sum of the 2 radii.

                    if dist <= touch_dist:  # Detect collision.
                        # For collision resolution, the velocities are simply swapped.
                        temp_x_vel = a[2]
                        temp_y_vel = a[3]
                        a[2] = b[2]
                        b[2] = temp_x_vel
                        a[3] = b[3]
                        b[3] = temp_y_vel

            # Detecting bullet collision.
            for c in ship.projectile_list:
                dist = ((c[0] - a[0]) ** 2 + (c[1] - a[1]) ** 2) ** 0.5  # Good ol' Pythagoras.

                if dist <= rc:  # On collision, asteroid velocity becomes projectile velocity * mass.
                    # It is also assumed that all asteroids have mass 1.
                    a[2] = c[2] * st.PROJECTILE_MASS
                    a[3] = c[3] * st.PROJECTILE_MASS
                    ship.projectile_list.pop(0)


# find() doesn't work with 2-dimensional arrays. Here's a temporary fix.
def list_find(l, f):
    index = None
    for i in range(len(l)):
        if l[i] == f:
            index = i
            break

    return index
