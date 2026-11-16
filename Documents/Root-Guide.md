<h1 align=center>How To Root Your Android Phone!</h1>
<h2 align=center>Prerequisites</h2>
<h4 align=center>Just See The ADB Installation Script In The Scripts Folder Instead If You Don't Want To Read All Of This Install Stuff</h4>

- Enable OEM Unlocking On Your Android Device (Some Devices Do Not Support This Feature)
  - Go To Settings --> About Phone --> Software Information --> Click The Build Number Many Times Until It Asks For Your Pin Or Says You're A Developer
  - Go Back To The Main Settings Page --> System --> Developer Options
  - Toggle **OEM Unlocking**, THIS WILL ERASE ALL OF YOUR DATA LATER ON!!!
- Get A Computer With Platform Tools Installed (ADB & Fastboot)
  - Windows
    - Click [This](https://raw.githubusercontent.com/Xen1123/Android-Help/main/Platform%20Tools.tar.gz) To Download Platform Tools
      - Unzip It
      - When You Have A Terminal In The Directory Of Platform Tools, You Can Run ADB & Fastboot Commands
  - Linux
    - Download ADB & Fastboot Via Your Distribution's Package Manager
      - Pacman
        - `sudo pacman -S android-tools`
      - Debian
        - `sudo apt install adb fastboot`
      - Fedora
        - `sudo dnf install android-tools`
    - If Your Distro Does Not Use One Of These Package Managers, Either Try Typing `adb`, `fastboot`, or `android-tools` Into Your Package Manager's Installation Command, or Follow This Guide, This Following Guide Works Without Sudo Permissions
      - Click [This](https://dl.google.com/android/repository/platform-tools-latest-linux.zip)
        - Unzip It
        - When You Have A Terminal In The Directory Of Platform Tools, You Can Run ADB & Fastboot Commands
    - macOS
      - Open Your Terminal
        ```bash
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        brew install --cask android-platform-tools -y
        ```
      
<h2 align=center>Getting To The Root of The Topic</h2>

- First, Find The Stock Firmware For Your Device [Here](./Stock-Firmware.md)
  - Find the `init_boot.img` and pull it to the Downloads folder
- Second, Download [Magisk](https://github.com/topjohnwu/Magisk)
- `adb install magisk*.apk`

**Linux🐧 / macOS**🍎
```bash
adb push ~/Downloads/init_boot.img /sdcard/Download
```

**Windows**🪟
```bash
adb push "%USERPROFILE%\Downloads\init_boot.img" /sdcard/Download
```
- Patch the image in Magisk, then pull it back to your computer

**Linux🐧 / macOS**🍎
```bash
adb pull /sdcard/Download/magisk-patched* ~/Downloads/root_init_boot.img
```

**Windows**🪟
```bash
adb pull /sdcard/Download/magisk-patched* "\%USERPROFILE%\Downloads\root_init_boot.img"
```

<h2 align=center>The Finale</h2>

- It Is Now Time To Unlock Your Bootloader, Please Make Sure You Enabled OEM Unlocking Earlier
- Reboot Into Your Bootloader Interface And Proceed With The Unlock, Confirming On Your Device With Volume Buttons & Power Key

```bash
adb reboot bootloader && fastboot flashing unlock
```
- If This Did Not Activate The Prompt But OEM Unlocking Is Enabled And You're In Fastboot, Try This

```bash
fastboot flashing oem unlock
```

- If This Failed, Stop Here, You May Be Missing Fastboot Drivers, Does Your Device Show Up When You Type `fastboot devices`?

- Once Your Bootloader Is Unlocked, The Phone Will Factory Reset And Boot Into Android Setup, You're Close! Turn Off The Phone And Hold The Power Button With The Volume Key Until You Boot Back Into The Bootloader (Key Combination May Be Different On Select Devices)
- Flash Your Patched Image

```bash
fastboot flash init_boot root_init_boot.img && fastboot reboot
```
- Congratulations! You're Done! You're Semi-Rooted And Free To Do Anything On Android Now! When You Setup Your Phone, There Will Be A System App For Magisk In Your App Drawer, This Is Called A Stub, Once You Try To Open It, It Will Install The Full Magisk App And Then Fully Patch Your Device To Give You Full Root Access!

<h2 align=center>Post Root Help</h2>

- These Are Just Some Things You Can Use After Rooting To Make Your Android Experience With Root Worth It!
  - [The Android Debloat And Flasher Script](../Scripts/master.py) is a script I have made in Python for cross platform stability that lets you debloat or flash to an Android device!
  - LSPosed/Vector Is A Very Good Implementation of Xposed, Which Uses Root To Allow The User To Hook Apps Into System Processes, Download It [Here!](https://github.com/JingMatrix/Vector/)
  - [Droidify](https://droidify.app/) Is An App Store Of A Collection Of Free And Open Source (FOSS) Apps That You Can Download, Some Apps Available In Droidify Are Directly Reliant On LSPosed/Vector
  - Play Integrity
    - When you unlock an Android bootloader, root the device, or flash a custom ROM, your device is considered "bad" to Google's servers. Apps that rely on Play Integrity will fail to work (signing in may not work or the app will just not open), this is device dependent, Google Pixels are typically very good at Play Integrity, even with unlocked, modded devices. Although Pixels are typically safe, other phones tend to have broken integrity just from unlocking the bootloader - Magisk modules do exist to help you, though, but on select devices, you'll need to flash all of these.
      - [Play Integrity Fix](https://github.com/KOWX712/PlayIntegrityFix)
      - [Rezygisk (Use Instead of Magisk Zygisk)](https://github.com/PerformanC/ReZygisk)
      - [Tricky Store](https://github.com/5ec1cff/TrickyStore/)
      - [YuriKey Manager](https://github.com/Yurii0307/yurikey/)
      - [Vector (LSPosed)](https://github.com/JingMatrix/Vector/)

