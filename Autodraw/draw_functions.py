import math
import numpy
from pyautogui import click, size
from keyboard import press_and_release
from PIL import Image
from time import sleep

"""

A while bunch of image to pixel array interpreters

"""


def circle(x, y, radius, angle_step, filled=False):
    # Kinda scuffed; will do.
    point_set = []

    if not filled:
        for theta in numpy.arange(0, 2 * math.pi, angle_step):
            point_set.append([math.cos(theta) * radius + x, math.sin(theta) * radius + y])

    elif filled:
        current_radius = 0
        while current_radius != radius:
            for theta in numpy.arange(0, 2 * math.pi, angle_step):
                point_set.append([math.cos(theta) * current_radius + x, math.sin(theta) * current_radius + y])

            current_radius += 1

    print('Processing finished')
    return point_set


def change_col(rgb_col):
    """Manually changes paint colour"""
    button_pos = (size()[0] / 1.598, size()[1] / 12.414)
    click(button_pos[0], button_pos[1])

    # Change keypress sequence
    tabs = 7  # The amount of times tab is pressed to get to the RGB settings
    for press in range(tabs):
        press_and_release('TAB')

    for col in rgb_col:
        for char in str(col):
            press_and_release(char)

        press_and_release('TAB')

    # Exit sequence
    press_and_release('TAB')
    press_and_release('ENTER')

    sleep(0.1)


def image_scan_col(x, y, step: int, file):
    im = Image.open(file).convert('RGB')
    pixels = im.load()

    # Get dimensions of image for scanning
    wt, ht = im.size

    # Determine offset compensation
    offset_x = x - wt / 2
    offset_y = y - ht / 2

    # Return
    point_set = []

    # Scanner moves left to right, up to down
    for x in range(0, wt, step):

        for y in range(0, ht, step):
            if pixels[x, y] != (0, 0, 0) and pixels[x, y]:  # STRICT
                point_set.append([x + offset_x, y + offset_y, pixels[x, y]])

    print('Processing finished')

    return point_set


def image_scan_black(x, y, step: int, file):
    # Open file and read get access to pixel values
    im = Image.open(file)
    pixels = im.load()

    black_range = [0, 1]

    # Get dimensions of image for scanning
    wt, ht = im.size

    # Determine offset compensation
    offset_x = x - wt / 2
    offset_y = y - ht / 2

    # Return
    point_set = []

    # Scanner moves left to right, up to down
    for x in range(0, wt, step):

        for y in range(0, ht, step):

            if in_greyscale_range(pixels[x, y], black_range):
                point_set.append([x + offset_x, y + offset_y])

    print('Processing finished')

    return point_set


def in_greyscale_range(rgb, black_range):
    """Checks if an RGB tuple (R = G = B since it's greyscale) is in a given range of black shades"""

    on_track = 0

    if is_integer(rgb):
        if rgb in black_range:
            return True

        else:
            return False

    else:
        for val in rgb:
            if val not in black_range:
                on_track += 1

        if on_track > 0:
            return False

        else:
            return True


def is_integer(obj):
    if obj != 0:
        try:
            # Python's range only allows integer steps
            range(0, 1, obj)

        except TypeError:
            return False

        else:
            return True

    else:
        return True
