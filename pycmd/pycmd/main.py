from pycmd import commands


class PyCMD:
    def __init__(self):

        self.commandDesc = {
            "HELP": {
                "desc": "Show all commands. Format: {NONE}",
                "func": commands.HelpCmd
            },
            "SORT": {
                "desc": "Sort an input list of space separated numbers. Format: {A} {B} {C} ... {N}",
                "func": commands.SortCMD
            },
            "EXIT": {
                "desc": "Exit the program. Format: {NONE}",
                "func": commands.ExitCMD
            },
            "CDIR": {
                "desc": "Change the working directory to the input directory (absolute path). "
                        f"'{commands.MACROCHAR}' can be used as a macro for the working directory path. "
                        "Format: {DIR NAME}",
                "func": commands.CDirCMD
            },
            "MDIR": {
                "desc": "Make a new input directory in the working directory. Format: {DIR NAME}",
                "func": commands.MDirCMD
            },
            "RANK": {
                "desc": "Find the rank of a League of Legends player. Format: {REGION} {NAME}",
                "func": commands.RankCMD
            }
        }

    def main(self):
        while 1:
            user_input = input(f"<{commands.workingDir}> COMMAND: ")

            try:
                try:
                    command_input = user_input[user_input.index(' '):].strip()  # index() raises error whereas find() returns -1
                    command = user_input[:user_input.index(' ')].strip().upper()
                except ValueError:
                    command = user_input.upper()
                    self.commandDesc[command]["func"](None).function()
                else:
                    self.commandDesc[command]["func"](command_input).function()
            except KeyError:
                print("Error: invalid command.")

            print("-----")  # End of sequence


if __name__ == '__main__':
    print('Welcome to PyCMD! Enter the command "HELP" to get started.\n')
    programInstance = PyCMD()
    programInstance.main()
