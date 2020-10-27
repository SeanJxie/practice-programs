from pycmd.main import PyCMD

import sys
import os

workingDir = os.path.abspath(os.getcwd())
MACROCHAR = '?'  # For convenience


class Command:
    """

    Parent class for command classes

    """

    def __init__(self, i, default, takes_input=False):  # Don't see use for default param. Might remove.
        if takes_input:
            if i is None:
                self.default_input = default
            else:
                self.default_input = i
        else:
            self.default_input = default

    def function(self):
        ...


class HelpCmd(Command):
    """

    Prints descriptions for all commands

    """

    def __init__(self, i):
        super().__init__(i, default=PyCMD().commandDesc, takes_input=False)  # Special case: takes input from main

    def function(self) -> None:
        print("Available Commands:")
        for k in self.default_input.keys():
            print(f"{k} : {self.default_input[k]['desc']}")


class SortCMD(Command):
    """

    Sorts numbers

    """

    def __init__(self, i):
        super().__init__(i, default=None, takes_input=True)
        self.iter = []

    def _bubble_sort(self) -> list:
        swap = True
        while swap:
            swap = False
            for i in range(1, len(self.iter)):
                if self.iter[i - 1] > self.iter[i]:
                    self.iter[i - 1], self.iter[i] = self.iter[i], self.iter[i - 1]
                    swap = True

        return self.iter

    def function(self) -> None:
        if self.default_input is None:
            print("Error: No input arguments found")
        else:
            self.iter = [float(n) for n in self.default_input.split(' ')]  # Split input by ' ' char
            print(f"Sorted: {self._bubble_sort()}")


class ExitCMD(Command):
    """

    Leave program

    """

    def __init__(self, i):
        super().__init__(i, default=None, takes_input=False)

    def function(self) -> None:
        exit()


class CDirCMD(Command):
    """

    Change working directory

    """

    def __init__(self, i):
        super().__init__(i, default=None, takes_input=True)

    def function(self) -> None:
        global workingDir

        path = str(self.default_input).replace(MACROCHAR, workingDir)

        if os.path.isdir(path):  # '?' is short for cwd
            workingDir = path
        else:
            print("Error: invalid directory change.")


class MDirCMD(Command):
    """

    Make a directory

    """

    def __init__(self, i):
        super().__init__(i, default=None, takes_input=True)

    def function(self) -> None:
        try:
            os.mkdir(os.path.join(workingDir, self.default_input))
        except TypeError:
            print(f"Error: directory name cannot be {self.default_input}.")
        except FileExistsError:
            print("Error: directory already exits.")
        except OSError:
            print(f"Error: MDIR command syntax is incorrect. Note: the '{MACROCHAR}' macro is used for CDIR only.")
