from pathlib import Path
import shutil
import subprocess
import sys
import os
print("Hello, This Is A Factory Image Flasher Script For Fastboot Androids!")
print("Please Make Sure Fastboot Is Installed And All Images Are In The Working Directory!")
print("This Script Has A Chance Of HARD BRICKING Your Device, Meaning That It Is Unable To Be Fixed!")
confirm = input("Continue? (yes/no): ")

if confirm.lower() != "yes":
    print("Okay, If You Want To Actually Run This, Just Re-Run And Type `yes`")
    sys.exit()
fastboot_path = shutil.which("fastboot")
if not fastboot_path:
    print("Fastboot Not Found In Your PATH!")
    sys.exit()
else:
    print(f"Fastboot Found At: {fastboot_path}")

adb_path = shutil.which("adb")
if not adb_path:
    print("ADB Not Found In Your PATH")
    sys.exit()
else:
    print(f"ADB Found At: {adb_path}")

subprocess.run([
    "adb", "reboot", "fastboot"
], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
subprocess.run([
    "fastboot", "reboot", "fastboot"
], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

subprocess.run([
    "fastboot", "devices"
])

images = [
    "boot", "abl", "xbl", "aop", "aop_config", "bluetooth", "modem", "cpucp", "cpucp_dtb", "devcfg", "init_boot", "vendor_boot", "recovery", "vbmeta", 
    "vbmeta_vendor", "vbmeta_system", "xbl_ramdump", "xbl_config", "dsp", "dtbo", "keymaster", "imagefv", "tz", "shrm", "pvmfw", "odm", "hyp", "uefi", 
    "uefisecapp", "qupfw", "bootloader", "radio", "bl1", "bl2", "bl31", "gsa", "ldfw", "pbl", "tzsw", "multiimgoem"
]
for part in images:
    file_path = Path(f"{part}.img")

    if file_path.is_file():
        print(f"\nFlashing {part} . . .")
        subprocess.run([
            "fastboot", "flash", part, file_path
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        print(f"{part} Not Found . . .")

subprocess.run([
    "fastboot", "reboot", "fastboot"
])

logicals = [
    "system", "product", "vendor", "vendor_dlkm", "system_dlkm", "system_ext"
]
for logic in logicals:
    file_path = Path(f"{logic}.img")

    if file_path.is_file():
        print(f"\nFlashing {logic} . . .")
        subprocess.run([
            "fastboot", "flash", logic, file_path
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        print(f"{logic} Not Found")

confirm = input("Wipe Cache, User Data, & Metadada? (yes/no)")

if confirm.lower() != "yes":
    print("Okay, Stopping Here!")
    sys.exit()
subprocess.run([
    "fastboot", "-w"
], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

subprocess.run([
    "fastboot", "reboot", "bootloader"
])