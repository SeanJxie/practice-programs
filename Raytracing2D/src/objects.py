import math
import arcade as acd

"""

Defining our objects.

"""


class Ray:
    """

    Represents a single ray of light, defined by a linear equation.

    """

    def __init__(self, source, gradient, max_length, hit=False):
        self.source = self.end_point = source

        self.gradient = gradient
        self.max_length = max_length

        self.hit = hit

    def set_endpoint(self, point):
        self.end_point = point

    def set_hit_state(self, state):
        self.hit = state


class CircleBarrier:
    """

    Represents a circle barrier that rays stop upon meeting.

    """

    def __init__(self, position, radius):
        self.position = position
        self.radius = radius


class RayTraceEngine:
    """

    The numerical ray collision processing is managed here.

    """

    def __init__(self, rays, circle_barriers, trace_speed=1):
        self.rays = rays
        self.circle_barriers = circle_barriers
        self.trace_speed = trace_speed

    def proccess_endpoints(self):
        # Process all the endpoints based on the given amount of rays and barriers.
        for ray in self.rays:

            for circle_barrier in self.circle_barriers:
                if get_dist(ray.end_point, circle_barrier.position) <= circle_barrier.radius:
                    ray.set_hit_state(True)

            if get_dist(ray.source, ray.end_point) >= ray.max_length:
                ray.set_hit_state(True)

            if not ray.hit:
                angle = math.atan(ray.gradient)

                ray.set_endpoint([ray.end_point[0] + math.cos(angle) * self.trace_speed, ray.end_point[1] + math.sin(angle) * self.trace_speed])


class Renderer:
    """

    Rendering of rays and objects are managed here.

    """

    def __init__(self, rays, circle_barriers):
        self.rays = rays
        self.circle_barriers = circle_barriers

    def render_rays(self):
        acd.start_render()
        for ray in self.rays:
            to_render = acd.create_line(ray.source[0], ray.source[1], ray.end_point[0], ray.end_point[1], acd.color.WHITE)

            acd.render(to_render)

    def render_circle_barriers(self):
        for circle_barrier in self.circle_barriers:
            to_render = acd.create_ellipse_filled(circle_barrier.position[0], circle_barrier.position[1], circle_barrier.radius,
                                                  circle_barrier.radius, acd.color.GREEN)
            acd.render(to_render)


# Helpful funtions -----
def get_dist(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

print(get_dist([0, 0], [800, 800]))