from cv2 import circle

"""

Useful functions for motion detection

"""


def all_rgb_step(image, step, window_size):
    """Simply returns all the RGB values from pixels on an interval step and returns as a 2D list"""
    image_array = []

    for x in range(0, window_size['wt'], step):
        for y in range(0, window_size['ht'], step):
            image_array.append(image[y, x])

    return image_array


def list_int_greater_than_2d(lst, n):
    """Check if any values in a 2D list l are greater than n"""
    res = False

    for i in range(len(lst)):
        if list_int_greater_than_1d(lst[i], n):
            res = True

    return res


def list_int_greater_than_1d(lst, n):
    """Check if any values in a 1D list l are greater than n"""
    res = False

    for i in range(len(lst)):
        if lst[i] >= n:
            res = True

    return res


def subtract_rgb_arrays(prev, curr):
    difference = []

    for i in range(len(prev)):
        difference.append(subtract_rgb(prev[i], curr[i]))

    return difference


def subtract_rgb(prev, curr):
    return [abs(int(a) - int(b)) for a, b in zip(prev, curr)]


# Functions for visualization
def draw_detection_step(frame, step, window_size):
    """Draw the distribution of detection pixels on an interval step"""
    for x in range(0, window_size['wt'] + 1, step):
        for y in range(0, window_size['ht'] + 1, step):
            circle(frame, (x, y), 1, (0, 0, 0), 1)
