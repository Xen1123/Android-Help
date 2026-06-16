<h1 align="center">Android-Help</h1>
<h3 align="center">A Simple Repository To Help With Android Tweaking</h3>

<img src="./Android-Logo.png" width="384">

<h4 align=center>Install Python from www.python.org or via your distribution's package manager.</h4>

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
- [x] Create guides for rooting Android phones
- [x] Create Firmware Finder for select devices
- [x] Make Firmware Finder support more devices
- [x] Make Debloat & Flasher Scripts support more devices
- [x] Make Python equivalents for scripts so Windows, Mac, BSD, and More can run the scripts.
- [x] Make Python scripts BETTER!!!
