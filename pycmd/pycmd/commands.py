from pycmd.main import PyCMD

import sys
import os

from urllib.request import urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup

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
            print("Error: No input arguments found.")
        else:
            try:
                self.iter = [float(n) for n in self.default_input.split(' ')]  # Split input by ' ' char
                print(f"Sorted: {self._bubble_sort()}")
            except ValueError:  # More specific, custom error message
                print("Error: input syntax incorrect. Numbers should be separated by spaces. Format: {A} {B} {C} ... {N}")


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

        if os.path.isdir(path):  # '?' is macro for cwd
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
        except Exception as e:
            print(e)


class RankCMD(Command):
    """

    Get the rank of a League of Legends player

    """

    def __init__(self, i):
        super().__init__(i, default=None, takes_input=True)
        print("Fetching data...")

    def function(self):
        try:
            region, name = self.default_input.split()

            try:
                http_response_obj = urlopen(f"https://{region}.op.gg/summoner/userName={name}")  # Get HTML object

                html_str = http_response_obj.read().decode("utf-8")  # Take HTML as string
                s = BeautifulSoup(html_str, "html.parser")  # Parse the string

                trueNameTag = str(s.find_all("span", {"class": "Name"}))  # Get correct capitalization
                rankTag = str(s.find_all("div", {"class": "TierRank"}))  # Find string content of <div class=TierRank ... </div> tag

                nameIdx1, nameIdx2 = self._extract(trueNameTag)
                rankIdx1, rankIdx2 = self._extract(rankTag)

                if rankTag[rankIdx1: rankIdx2] == '[':
                    print("Error: player does no exist.")
                else:
                    print(f"{trueNameTag[nameIdx1: nameIdx2]} is currently {rankTag[rankIdx1: rankIdx2].strip()}.")

            except URLError:
                print("Error: invalid region code.")

        except ValueError:
            print("Error: input syntax incorrect. Format: {REGION} {NAME}")

    @staticmethod
    def _extract(tag):
        # In the case of profiles of pro players, format is:
        # [<span class="Name"> OFFICIAL NAME </span> <span class="Name"> ACCOUNT NAME </span>]
        # So, to find the '>' for the ACCOUNT NAME, we reverse search, avoiding the '>' at the end by
        # avoiding the last 2 chars ([:-2] splice)
        idx1 = tag[:-2].rfind('>') + 1
        idx2 = tag.rfind('<')

        return idx1, idx2
