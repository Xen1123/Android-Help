import os
import platform
import shutil
import sys
import time
import urllib.request

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

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
if not shutil.which("adb") or not shutil.which("fastboot"):
    if platform.system() == "Windows":
        winget_path = shutil.which("winget")
        if not winget_path:
            print("This System Does Not Have Winget Installed Or In The Path! I'll Try To Just Go Grab The Zip From The Web, You Can Extract That And Use ADB And Fastboot When You're In The Folder!")
            url = "https://dl.google.com/android/repository/platform-tools-latest-windows.zip"
            file_name = "ADB_Fastboot.zip"
            urllib.request.urlretrieve(url, file_name)
            
        os.system(
            "winget install Google.PlatformTools --silent --accept-source-agreements --accept-package-agreements"
        )
        os.system("cls")
        print("ADB & Fastboot Are Now On Your System! :)")
        input(
            "\nPress Enter To Close The Terminal, ADB & Fastboot Only Really Work After Re-Opening."
        )

    elif platform.system() == "Linux":
        print("Linux Detected!")
        if shutil.which("pacman"):
            os.system("sudo pacman -S android-tools erofs-utils --noconfirm")
            os.system("clear")
            print("ADB & Fastboot Are Now Installed!")

        elif shutil.which("apt"):
            os.system("sudo apt install adb fastboot erofs-utils -y")
            os.system("clear")
            print("ADB & Fastboot Are Now Installed!")

        elif shutil.which("dnf"):
            os.system("sudo dnf install android-tools erofs-utils -y")
            os.system("clear")
            print("ADB & Fastboot Are Now Installed!")

        elif shutil.which("apk"):
            os.system("sudo apk add android-tools erofs-utils")
            os.system("clear")
            print("ADB & Fastboot Are Now Installed!")

        elif shutil.which("xbps-install"):
            os.system("sudo xbps-install -y android-tools erofs-utils")
            os.system("clear")
            print("ADB & Fastboot Are Now Installed!")

        elif shutil.which("zypper"):
            os.system("sudo zypper install android-tools erofs-utils")
            os.system("clear")
            print("ADB & Fastboot Are Now Installed!")

        elif shutil.which("emerge"):
            os.system("sudo emerge --ask=n dev-util/android-tools")
            os.system("sudo emerge --ask=n dev-util/erofs-utils")
            os.system("clear")
            print("ADB & Fastboot Are Now Installed!")

        else:
            os.system("clear")
            print("Sorry, Your Package Manager Is Not Supported")
            sys.exit()
        print(
            "You Now Have ADB & Fastboot! Depending On Your Distro, You May Need To Run ADB & Fastboot As Root Or With Sudo!"
        )
    elif platform.system() == "Darwin":
        print("MacOS Detected!")
        if not shutil.which("brew"):
            os.system(
                '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'
            )
        os.system("brew install android-platform-tools")
        os.system("brew install erofs-utils")
        os.system("clear")
        print("ADB & Fastboot Are Now Installed!")

    elif "BSD" in platform.system() or platform.system() == "FreeBSD":
        print(f"{platform.system()} Detected!")
        if shutil.which("pkg"):
            os.system("sudo pkg install -y android-tools")
        elif shutil.which("pkg_add"):
            os.system("sudo pkg_add android-tools")
    else:
        print(
            "Your OS Is NOT Supported, If You Can't Get Android Tools, How Are You Even Able To Get Python??"
        )
        sys.exit()
else:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    print("ADB & Fastboot Are Already Installed! :)")
    sys.exit()
