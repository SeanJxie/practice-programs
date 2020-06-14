import arcade as acd
from pyorbital import engine
from random import randint

WIN_SIZE = (700, 700)
WIN_CAPTION = 'pyorbital test'
UPDATE_TICK = 1 / 60  # Seconds
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize planets
planet_list = [engine.Planet([randint(0, WIN_SIZE[0]), randint(0, WIN_SIZE[1])], randint(10, 100), 50, BLACK) for _ in
               range(10)]

system = engine.PlanetarySystem(planet_list, gravitational_constant=1, new_planet_on_collision=False)


def update(delta_time):
    system.update()
    system.render()


def mouse_click(x, y, button, modifiers):
    if button == acd.MOUSE_BUTTON_LEFT:
        planet_list.append(engine.Planet([x, y], 1000, 50, BLACK))


def main():
    acd.open_window(WIN_SIZE[0], WIN_SIZE[1], WIN_CAPTION)

    acd.schedule(update, UPDATE_TICK)
    acd.set_background_color(WHITE)

    window = acd.get_window()
    window.on_mouse_press = mouse_click

    acd.run()


if __name__ == '__main__':
    main()
