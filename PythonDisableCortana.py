import os
from winreg import *


def ask_for_reboot():
    restart = input(
        "Cortana is disabled now! Your computer must be rebooted to apply the setting. Do you wish to restart your computer now? (yes / no): ")
    if restart == 'no':
        exit()
    else:
        os.system("shutdown /r /t 1")

try:
    # If 'Windows Search' key exists, disable Cortana
    aKey = OpenKey(HKEY_LOCAL_MACHINE, r'SOFTWARE\Policies\Microsoft\Windows\Windows Search', 1, KEY_WRITE)
    SetValueEx(aKey, r"AllowCortana", 1, REG_DWORD, 0)
    ask_for_reboot()
except OSError:
    # If 'Windows Search' key doesn't exist - create it
    try:
        CreateKey(HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\Windows Search")
        # Then disable Cortana
        try:
            aKey = OpenKey(HKEY_LOCAL_MACHINE, r'SOFTWARE\Policies\Microsoft\Windows\Windows Search', 1, KEY_WRITE)
            SetValueEx(aKey, r"AllowCortana", 1, REG_DWORD, 0)
            ask_for_reboot()
        except OSError as err1:
            print("Unable to set the key (run the script with Admin privileges): {0}".format(err1))
    except OSError as err2:
        print("Error Creating 'Windows Search' Key (run the script with Admin privileges): {0}".format(err2))
