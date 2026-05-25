<h1 align="center">Android-Help</h1>
<h3 align="center">A Simple Repository To Help With Android Tweaking</h3>

<img src="https://github.com/Xen1123/Android-Help/blob/main/Android-Logo.png" width="384">

<h3 align=center>DISCLAIMER: If There Is A Python Variant Of Something Here, Use That Instead, It Is Newer, More Refined, And More Compatible With Other Devices.</h3>

<h4 align=center>Install Python At www.python.org Or Install Via Your Distribution's Package Manager</h4>

## ITEMS IN REPOSITORY
- **Debloaters**
- **Flashers**
- **Guides**

## Tools That Can Assist You
- [How To Flash Custom ROM](https://www.youtube.com/watch?v=gSRxThnfY8M)
- [How To Root Your Android Phone](https://www.youtube.com/watch?v=qkuXl6m6Ghs)
- [EZ Root Guide](./Documents/Root-Guide.md)
- [Stock Firmware Finder w/ Links](./Documents/Stock-Firmware.md)

# Prerequisites
- `adb` and `fastboot` Installed
- Unlocked Bootloader
- USB Debugging enabled
  <details>
  <summary><b>ADB & Fastboot Installation</b></summary>
  
  - ## ADB/Fastboot On Your PC
    - Linux
      - Arch/Pacman -  `android-tools`
      - Debian/APT - `adb` and `fastboot`
      - Fedora/DNF - `android-tools`
    
    - Windows
      ```bash
      winget install Google.PlatformTools --silent --accept-source-agreements --accept-package-agreements
      ```

    - MacOS
      ```bash
      /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
      brew install --cask android-platform-tools
      ```

## TO-DO:
- [x] Create Guides For Rooting Android Phones
- [x] Create Firmware Finder For Select Devices
- [x] Make Firmware Finder Support More Devices
- [x] Make Debloat & Flasher Scripts Support More Devices
- [x] Make Python Equivalents For Scripts So Windows, Mac, BSD, And More Can Run Scripts.
- [x] Make Python Scripts BETTER!!!