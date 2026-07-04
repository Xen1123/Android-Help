<h1 align="center">Android-Help</h1>
<h3 align="center">A Simple Repository To Help With Android Tweaking</h3>

<img src="./Android-Logo.png" width="384">

<h4 align=center>Install Python from www.python.org or via your distribution's package manager.</h4>

## Repository Contents
- **Debloaters**: Multi-Platform Python automation modules that use ADB (Android Debug Bridge) to remove unnecessary apps that are pre-installed on your Android device.
- **Flashers**: Multi-Platform Python automation scripts that use the Fastboot executable to flash images to a device compatible with bootloader and userspace Fastboot (Fastbootd) -- As a result, these automation modules are not compatible with devices like Samsungs, as they use their proprietary Download Mode.
- **Guides**: Instructions written in Markdown.

## Repository Hierarchy
```
Android-Help/
├── Android-Logo.png
├── Android-Tools.py
├── Debloaters
│   └── Debloat.py
├── Documents
│   ├── Root-Guide.md
│   └── Stock-Firmware.md
├── Flasher
│   └── Flasher.py
└── README.md
```

## Help
- [How To Flash Custom ROM](https://www.youtube.com/watch?v=gSRxThnfY8M)
- [How To Root Your Android Phone](https://www.youtube.com/watch?v=qkuXl6m6Ghs)
- [Simple Root Guide](./Documents/Root-Guide.md)
- [Stock Firmware Finder With Links](./Documents/Stock-Firmware.md)

# System Prerequisites & Host Environment
To run these scripts, please make sure you meet all of these requirements.
  - Host
    - Python 3.8 or later is installed and in your PATH
    - You have `adb` and `fastboot` installed and in your PATH
    - Your user has sufficient permissions to communicate to external USB devices
  - Device Requirements
    - USB Debugging enabled (see [Root-Guide.md](./Documents/Root-Guide.md) for instructions)
    - You have OEM Unlocking enabled (see [Root-Guide.md](./Documents/Root-Guide.md))
  
  <details>
  <summary><b>ADB & Fastboot Installation</b></summary>
  
  - ## ADB & Fastboot Utilities On Your PC
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

    - Termux (On a separate device)
      - Assuming the device isn't rooted:
        - ```bash
          pkg install curl termux-api -y && curl -s https://raw.githubusercontent.com/nohajc/termux-adb/master/install.sh | bash
          ```
      - Usage:
        - ```bash
          termux-adb <command>
          ```
        - ```bash
          termux-fastboot <command>
          ```
      - The process on a rooted device:
        - ```bash
          pkg install android-tools && su
          ```
      - Usage:  
        - ```bash
          adb devices
          ```
        - ```bash
          fastboot devices
          ```

    - If your system is not included here or you are having issues, please see [Android-Tools.py](./Android-Tools.py) and run it with Python.
  </details>
  

