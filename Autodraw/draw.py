from Autodraw import draw_functions
from time import sleep
from subprocess import Popen
import keyboard
import pyautogui

"""

Drawing things with PyAutoGUI

"""

# Open MS paint. How nice!
Popen('MSPAINT')

# Get screen dimensions
sc_width, sc_height = pyautogui.size()

# Set up a list of pixel_draw_list[i]s to be coloured in.
pixel_draw_list = draw_functions.image_scan_col(sc_width / 2, sc_height / 2, 10,
                                                'Colorwheel_sixcolor.svg.png')

# Fill the draw list
sleep(3)


def auto_draw():
    success = True
    current_col = (0, 0, 0)  # For coloured drawing

    for i in range(len(pixel_draw_list)):

        if keyboard.is_pressed('TAB'):
            print('Render halted')
            success = False
            break

        if len(pixel_draw_list[i]) == 3:  # Change colour if colour specification is available
            if current_col != pixel_draw_list[i][2] != (255, 255, 255):
                draw_functions.change_col(pixel_draw_list[i][2])

        print(pixel_draw_list[i])

        pyautogui.click(pixel_draw_list[i][0], pixel_draw_list[i][1])

    if success:
        print('Rendering finished')

    print("Program ended")


if __name__ == '__main__':
    auto_draw()
