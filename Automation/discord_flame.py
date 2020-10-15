import subprocess
import keyboard
import random
import time
from win32gui import GetWindowText, GetForegroundWindow

from Automation import insults
import getpass
import os

# Limited to users with this specific file structure
subprocess.Popen(rf"C:\Users\{getpass.getuser()}\AppData\Local\Discord\Update.exe --processStart Discord.exe")
# os.system("start Discord:") buggy startup call

TIME_INTERVAL = 2  # Time in seconds between each call


def send_flame():  # Keypress sequence for sending insult
    keyboard.send("ENTER")
    keyboard.send("BACKSPACE")
    keyboard.write(random.choice(insults.flame_list))
    keyboard.send("ENTER")


cont_on_next_call = True  # Condition to continue

sTime = time.time()  # Start time
timeDiff = 0  # Time difference
while cont_on_next_call:
    if GetWindowText(GetForegroundWindow())[-7:] == "Discord" and timeDiff >= TIME_INTERVAL:  # Check if it's time to send
        send_flame()
        sTime = time.time()  # Reset start time on send

    eTime = time.time()  # End time
    timeDiff = eTime - sTime  # Calculate difference

    if keyboard.is_pressed("SPACE"):  # Exit on keypress
        cont_on_next_call = False
