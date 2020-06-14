from math import sin, cos, atan2
from arcade import start_render, buffered_draw_commands, render, draw_texture_rectangle, load_texture

"""

2D Planetary motion

"""


class Planet:
    def __init__(self, init_pos, mass, radius, col=None, texture_path=None):
        self.pos = init_pos  # [x, y]
        self.mass = mass
        self.radius = radius
        self.col = col
        self.texture = texture_path

        self.vel_vector = self.acc_vector = self.force_vector = [0, 0]  # [Magnitude, Direction(radians)]

    def apply_force(self, force_vec):
        self.force_vector = force_vec

    def update_pos(self):
        # Acceleration
        # Direction remains the same
        self.acc_vector = [self.second_law_acceleration(self.force_vector[0], self.mass), self.force_vector[1]]

        # Velocity
        # Since v = aΔt and every update tick is an increment of time,
        self.vel_vector[0] += self.acc_vector[0]
        self.vel_vector[1] = self.acc_vector[1]

        # Position
        # Since d = vΔt and every update tick is an increment of time,
        self.pos[0] += self._get_step(self.vel_vector)[0]
        self.pos[1] += self._get_step(self.vel_vector)[1]

    def render(self):
        if self.texture is None:
            circle = buffered_draw_commands.create_ellipse_filled(self.pos[0], self.pos[1], self.radius, self.radius,
                                                                  self.col)
            render(circle)

        elif self.col is None:
            texture = load_texture(self.texture)
            draw_texture_rectangle(self.pos[0], self.pos[1], self.radius * 2, self.radius * 2, texture)

    @staticmethod
    def second_law_acceleration(f, m):
        # F = ma
        # a = F / m
        return f / m

    @staticmethod
    def _get_step(vector):
        return cos(vector[1]) * vector[0], sin(vector[1]) * vector[0]


class PlanetarySystem:
    def __init__(self, planets, gravitational_constant, new_planet_on_collision=True):
        self.planets = planets
        self.G_CONST = gravitational_constant
        self.NEW_PLANET_COLLISION = new_planet_on_collision

    def update(self):
        for p1 in self.planets:
            for p2 in self.planets:
                if p1 != p2:

                    # Calculate and apply force
                    temp_force_vector = [
                        self._gravitational_force(p1.mass, p2.mass, self._dist_between(p1.pos, p2.pos)),
                        self._radians_between(p1.pos, p2.pos)
                    ]

                    # On impact, form a planet which is the sum of the two planets
                    if self._dist_between(p1.pos, p2.pos) <= p1.radius + p2.radius and self.NEW_PLANET_COLLISION:
                        self.planets.remove(p2)

                        collision_pos = self._midpoint(p1.pos, p2.pos)

                        p1.mass += p2.mass
                        p1.radius += p2.radius

                        p1.pos = collision_pos

                    p1.apply_force(temp_force_vector)
                    p1.update_pos()

    def render(self):
        start_render()
        for p in self.planets:
            p.render()

    def _gravitational_force(self, m1, m2, r):
        return (self.G_CONST * m1 * m2) / r ** 2

    @staticmethod
    def _midpoint(p1, p2):
        return [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]

    @staticmethod
    def _dist_between(p1, p2):
        return ((p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2) ** 0.5

    @staticmethod
    def _radians_between(p1, p2):
        return atan2(p2[1] - p1[1], p2[0] - p1[0])
