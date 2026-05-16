import shutil
import subprocess
import sys
import time
import os
import platform
print(r"""
 █████╗ ███╗   ██╗██████╗ ██████╗  ██████╗ ██╗██████╗ 
██╔══██╗████╗  ██║██╔══██╗██╔══██╗██╔═══██╗██║██╔══██╗
███████║██╔██╗ ██║██║  ██║██████╔╝██║   ██║██║██║  ██║
██╔══██║██║╚██╗██║██║  ██║██╔══██╗██║   ██║██║██║  ██║
██║  ██║██║ ╚████║██████╔╝██║  ██║╚██████╔╝██║██████╔╝
╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚═════╝ 
           ADB & Fastboot On Your PC
""")
time.sleep(2)
if not shutil.which('adb') or not shutil.which('fastboot'):
    if platform.system() == 'Windows':
        os.system('winget install Google.PlatformTools --silent --accept-source-agreements --accept-package-agreements')
        os.system('cls')
        print("ADB & Fastboot Are Now On Your System! :)")
        input("\nPress Enter To Close The Terminal, ADB & Fastboot Only Really Work After Re-Opening.")
    elif platform.system() == 'Linux':
        print('Linux Detected!')
        if shutil.which("pacman"):
            os.system('sudo pacman -S android-tools --noconfirm')
            os.system('clear')
            print('ADB & Fastboot Are Now Installed!')
        elif shutil.which("apt"):
            os.system('sudo apt install adb fastboot -y')
            os.system('clear')
            print('ADB & Fastboot Are Now Installed!')
        elif shutil.which("dnf"):
            os.system('sudo dnf install android-tools -y')
            os.system('clear')
            print('ADB & Fastboot Are Now Installed!')
        elif shutil.which("apk"):
            os.system('sudo apk add android-tools')
            os.system('clear')
            print('ADB & Fastboot Are Now Installed!')
        elif shutil.which("xbps-install"):
            os.system('sudo xbps-install -y android-tools')
            os.system('clear')
            print('ADB & Fastboot Are Now Installed!')
        elif shutil.which("zyppr"):
            os.system('sudo zypper install android-tools')
            os.system('clear')
        elif shutil.which("emerge"):
            os.system('sudo emerge --ask=n dev-util/android-tools')
            os.system('clear')
        else:
            print("Sorry, Your Package Manager Is Not Supported")
            sys.exit()
        print("You Now Have ADB & Fastboot! Depending On Your Distro, You May Need To Run ADB & Fastboot As Root Or With Sudo!")
    elif platform.system() == 'Darwin':
        print("MacOS Detected!")
        if not shutil.which("brew"):
            os.system('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
        os.system('brew install --cask android-platform-tools')
        os.system('clear')
        print("ADB & Fastboot Are Now Installed!")

    elif 'BSD' in current_os or current_os == 'FreeBSD':
        print(f"{current_os} Detected!")
        if shutil.which("pkg"):
            os.system('sudo pkg install -y android-tools')
        elif shutil.which("pkg_add"):
            os.system("sudo pkg_add android-tools")
    else:
        print("Your OS Is NOT Supported, If You Can't Get Android Tools, How Are You Even Able To Get Python??")
        sys.exit()
else:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print("ADB & Fastboot Are Already Installed! :)")
    sys.exit()