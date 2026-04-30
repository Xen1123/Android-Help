#!/bin/bash
echo "This Script Automatically Roots Your Android Device."
read -n 1 -s -r -p "Press any key to continue"

cd "/home/$USER" || true
if ! [ -d "Auto-Root" ]; then
    mkdir Auto-Root
fi
cd Auto-Root || true



if ! command -v adb >/dev/null 2>&1 && ! command -v fastboot >/dev/null 2>&1; then
    if command -v pacman >/dev/null 2>&1; then
        sudo pacman -S android-tools wget --noconfirm >/dev/null 2>&1
    elif command -v apt >/dev/null 2>&1; then
        sudo apt install adb fastboot wget -y >/dev/null 2>&1
    elif comamnd -v nala >/dev/null 2>&1; then
        sudo nala install adb fastboot wget -y >/dev/null 2>&1
    elif command -v dnf >/dev/null 2>&1; then
        sudo dnf install android-tools wget -y >/dev/null 2>&1
    else
        echo "No supported package manager found. Please install adb and fastboot manually."
        exit 1
    fi
fi


if fastboot oem device-info | grep -q "Device unlocked: true"; then
    echo "Your device is already unlocked. Proceeding with rooting..."
else
    echo "Your device is locked. Please unlock it first before running this script."
    exit 1
fi

if command -v wget >/dev/null 2>&1; then
    wget -q https://github.com/topjohnwu/Magisk/releases/download/v30.7/Magisk-v30.7.apk -O Magisk.zip
else
    echo "Wget is not installed. Please install wget and run this script again."
    exit 1
fi

PS3="Do You Have A Custom Recovery Installed? 
"
options=("Yes" "No")
select opt in "${options[@]}"
do
    case $opt in
        "Yes")
            fastboot reboot recovery
            echo "Please Select 'Apply Update from ADB' in the Recovery Menu and click any key to continue once your device is waiting."
            read -n 1 -s -r -p "Press any key to continue"
            adb sideload Magisk.zip
            echo "Magisk has been installed. Please reboot your device and enjoy root access!"
            break
            ;;
        "No")
            echo "Please Install A Custom Recovery (TWRP, OrangeFox, etc.) And Run This Script Again."
            exit 1
            ;;
        *)
            echo "Invalid Option: $REPLY"
            ;;g
        esac
    done

