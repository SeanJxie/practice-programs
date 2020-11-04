from pycmd import commands, ui_utils

from time import sleep


# TODO: Update commandDesc dict to include "format" key so there is no need to reference with string literals
# TODO: Generalize errors


class PyCMD:
    def __init__(self):
        while 1:  # Main loop
            user_input = input(f"<{commands.workingDir}> COMMAND: ")
            command = user_input[:4].upper()  # Commands are always 4 letters

            try:
                if commands.commandDesc[command]["func"](None).takesInput:

                    try:
                        command_input = user_input[user_input.index(' '):].strip()
                        commands.commandDesc[command]["func"](command_input).function()

                    except ValueError:
                        print(ui_utils.NO_INPUT_ERROR)

                else:
                    commands.commandDesc[command]["func"](None).function()

            except KeyError:
                print(ui_utils.INVALID_COMMAND_ERROR)

            print("-----")  # End of sequence


if __name__ == '__main__':
    print(ui_utils.INTRO + '\n')

    try:
        PyCMD()

    except Exception as e:
        ui_utils.raise_unaccounted_error(e)
        sleep(2)
