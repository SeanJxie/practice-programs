import arcade as acd
import math

"""

Gravitational simulation

TODO: Collision

"""

# Data storage
position = []
acceleration = []
force = []
velocity = []
mass = []
radius = []

# Constants
G = 6.6  # Universal gravitational constant

# Window constants
WIN_WT = 750
WIN_HT = 750
WIN_TT = "Gravity Simulation"

UPDATE_RATE = 1 / 60  # Update every 60th of a second.


def get_xy_component(angle):
    # Get x and y "step"
    return math.cos(math.radians(angle)), math.sin(math.radians(angle))


def get_acceleration(f, m):
    # By Newton's 2nd law f = ma,
    return f / m


def get_dist(p1, p2):
    # By Pythagoras' theorem a^2 + b^2 = c^2,
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


# Add a body to the simulation
def add_body(pos, a, f, v, m, r):
    position.append(pos)
    force.append(f)
    acceleration.append(a)
    velocity.append(v)
    mass.append(m)
    radius.append(r)


def render_bodies():
    acd.start_render()
    for i in range(len(position)):
        acd.draw_circle_filled(position[i][0], position[i][1], radius[i], (255, 255, 255))


def move_bodies():
    bod_count = len(position)

    for i in range(bod_count):  # Using any of our arrays will work as they're all the same length

        for j in range(bod_count):

            if i != j:
                # Important part: calculating force vector
                # By gravitational force formula F_g = GMm/r^2
                force_magnitude = (G * mass[i] * mass[j]) / get_dist(position[i], position[j]) ** 2
                force_direction = math.degrees(math.atan2(position[j][1] - position[i][1], position[j][0] - position[i][0]))

                force[i] = [force_magnitude, force_direction]

                acceleration[i] = [get_acceleration(force_magnitude, mass[i]), get_xy_component(force_direction)]

                # Soft collision detection
                if get_dist(position[i], position[j]) > radius[i] + radius[j]:
                    velocity[i][0] += acceleration[i][0] * acceleration[i][1][0]
                    velocity[i][1] += acceleration[i][0] * acceleration[i][1][1]

                    position[i][0] += velocity[i][0]
                    position[i][1] += velocity[i][1]


# Earth and moon
add_body([350, 350], [0, 0], [0, 0], [0, 0], 81, 40)
add_body([600, 350], [0, 0], [0, 0], [0, 1.5], 1, 10)


def update(delta_time):
    move_bodies()
    render_bodies()


def mouse_click(x, y, button, modifiers):
    if button == acd.MOUSE_BUTTON_LEFT:
        add_body([x, y], [0, 0], [0, 0], [0, 0], 1000, 10)


def main():
    acd.open_window(WIN_WT, WIN_HT, WIN_TT, True)
    acd.schedule(update, UPDATE_RATE)

    window = acd.get_window()
    window.on_mouse_press = mouse_click

    acd.run()


if __name__ == '__main__':
    main()
