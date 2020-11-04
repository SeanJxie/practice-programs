from pycmd import ui_utils

import os

from urllib.request import urlopen
from bs4 import BeautifulSoup

workingDir = os.path.abspath(os.getcwd())
MACROCHAR = '?'  # For convenience


class Command:
    """

    Parent class for command classes

    """

    def __init__(self, i, call_name, takes_input=False):
        self.takesInput = takes_input
        self.call_name = call_name

        if self.call_name not in commandDesc.keys():  # For debug
            print("Command has not been implemented in commandDesc.")
            exit()

        if takes_input:
            self.input = i

    @property
    def accepts_input(self):
        return self.takesInput

    def function(self):
        ...


class HelpCmd(Command):
    """

    Prints descriptions for all commands

    """

    def __init__(self, i):
        super().__init__(i, "HELP", takes_input=False)  # Special case: takes input from main

    def function(self) -> None:
        print("Available Commands:")
        for k in commandDesc.keys():
            print(f"{k}: {commandDesc[k]['desc']}")
            print(f"      Format: {commandDesc[k]['form']}\n")


class SortCMD(Command):
    """

    Sorts numbers

    """

    def __init__(self, i):
        super().__init__(i, "SORT", takes_input=True)
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
        if self.input is None:
            ui_utils.raise_syntax_error(self)
        else:
            try:
                self.iter = [float(n) for n in self.input.split(' ')]  # Split input by ' ' char
                print(f"Sorted: {self._bubble_sort()}")
            except ValueError:
                ui_utils.raise_syntax_error(self)  # Try to eliminate use of both error calls


class ExitCMD(Command):
    """

    Leave program

    """

    def __init__(self, i):
        super().__init__(i, "EXIT", takes_input=False)

    def function(self) -> None:
        exit()


class CDirCMD(Command):
    """

    Change working directory

    """

    def __init__(self, i):
        super().__init__(i, "CDIR", takes_input=True)

    def function(self) -> None:
        global workingDir

        path = str(self.input).replace(MACROCHAR, workingDir)

        if os.path.isdir(path):  # '?' is macro for cwd
            workingDir = path
        else:
            print(ui_utils.INVALID_DIR_ERROR)


class MDirCMD(Command):
    """

    Make a directory

    """

    def __init__(self, i):
        super().__init__(i, "MDIR", takes_input=True)

    def function(self) -> None:
        try:
            os.mkdir(os.path.join(workingDir, self.input))
        except Exception as e:  # No
            print(e)


class RankCMD(Command):
    """

    Get the rank of a League of Legends player

    """

    def __init__(self, i):
        super().__init__(i, "RANK", takes_input=True)

    def function(self) -> None:
        try:
            print("Fetching data...")
            http_response_obj = urlopen(f"https://na.op.gg/summoner/userName={self.input}")  # Get HTML object

            html_str = http_response_obj.read().decode("utf-8")  # Take HTML as string
            s = BeautifulSoup(html_str, "html.parser")  # Parse the string

            trueNameTag = str(s.find_all("span", {"class": "Name"}))  # Get correct capitalization
            rankTag = str(s.find_all("div", {"class": "TierRank"}))  # Find string content of <div class=TierRank ... </div> tag

            nameIdx1, nameIdx2 = self._extract(trueNameTag)
            rankIdx1, rankIdx2 = self._extract(rankTag)

            if rankTag[rankIdx1: rankIdx2] == '[':
                print(ui_utils.PLAYER_DNE_ERROR)
            else:
                print(f"{trueNameTag[nameIdx1: nameIdx2].strip()} is currently {rankTag[rankIdx1: rankIdx2].strip()}.")

        except AttributeError:
            ui_utils.raise_syntax_error(self)

    @staticmethod
    def _extract(tag) -> (int, int):
        # In the case of profiles of pro players, format is:
        # [<span class="Name"> OFFICIAL NAME </span> <span class="Name"> ACCOUNT NAME </span>]
        # So, to find the '>' for the ACCOUNT NAME, we reverse search, avoiding the '>' at the end by
        # avoiding the last 2 chars ([:-2] splice)
        idx1 = tag[:-2].rfind('>') + 1
        idx2 = tag.rfind('<')

        return idx1, idx2


# Command info -----
commandDesc = {
    "HELP": {
        "desc": "Show all commands.",
        "func": HelpCmd,
        "form": "{NONE}"
    },
    "SORT": {
        "desc": "Sort an input list of space separated numbers.",
        "func": SortCMD,
        "form": " {A} {B} {C} ... {N}"
    },
    "EXIT": {
        "desc": "Exit the program.",
        "func": ExitCMD,
        "form": "{NONE}"
    },
    "CDIR": {
        "desc": f"Change the working directory to the input directory (absolute path). (Macro '{MACROCHAR}' for CWD)",
        "func": CDirCMD,
        "form": "{FULL DIR PATH}"
    },
    "MDIR": {
        "desc": "Make a new input directory in the working directory.",
        "func": MDirCMD,
        "form": "{DIR PATH FROM CWD}"
    },
    "RANK": {
        "desc": "Find the rank of a League of Legends player.",
        "func": RankCMD,
        "form": "{NAME}"
    }
}
