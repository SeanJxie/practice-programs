import arcade as acd
import math
import numpy

"""

Simple real-time 2D ray tracing.

Bug: High trace velocities allow rays to overextend their intended maximum length and/or pass through barriers.

"""

from Raytracing2D.src.objects import Ray, CircleBarrier, RayTraceEngine, Renderer

# Window constants -----
WINDOW_SIZE = [800, 800]
UPDATE_TICK = 1 / 60  # A sixtyth of a second

# Ray trace constants -----
RAY_DENSITY = 6
LIGHT_ANGLE_RANGE = [0, 90]  # Degrees
TRACE_SPEED = 50
MAX_RAY_LENGTH = 1131

light_source = [0, 0]
ray_list = [Ray(light_source, math.tan(math.radians(theta)), 1000) for theta in numpy.arange(LIGHT_ANGLE_RANGE[0], LIGHT_ANGLE_RANGE[1], 1 / RAY_DENSITY)]
barriers = [CircleBarrier([400, 400], 150), CircleBarrier([200, 200], 50), CircleBarrier([200, 500], 20)]

ray_tracer = RayTraceEngine(ray_list, barriers, TRACE_SPEED)
renderer = Renderer(ray_list, barriers)


def update(delta_time):
    ray_tracer.proccess_endpoints()
    renderer.render_rays()
    renderer.render_circle_barriers()


def main():
    acd.open_window(WINDOW_SIZE[0], WINDOW_SIZE[1], "Ray Tracing")
    acd.set_background_color(acd.color.BLACK)

    acd.schedule(update, UPDATE_TICK)

    acd.run()


if __name__ == '__main__':
    main()
