from pathlib import Path
import shutil
import subprocess
import sys
import os
import time

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

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

print("Rebooting To Bootloader Fastboot Mode . . .")
time.sleep(2)

subprocess.run([
    "adb", "reboot", "fastboot"
], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
subprocess.run([
    "fastboot", "reboot", "bootloader"
], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

subprocess.run([
    "fastboot", "devices"
])

time.sleep(2)

images = [
    "boot", "abl", "xbl", "aop", "aop_config", "featenabler", "bluetooth", "modem", "cpucp", "cpucp_dtb", "devcfg", "init_boot", "vendor_boot", "recovery", "vbmeta", 
    "vbmeta_vendor", "vbmeta_system", "xbl_ramdump", "xbl_config", "dsp", "dtbo", "keymaster", "imagefv", "tz", "shrm", "pvmfw", "odm", "hyp", "uefi", 
    "uefisecapp", "qupfw", "bootloader", "radio", "bl1", "bl2", "bl31", "gsa", "ldfw", "pbl", "tzsw", "multiimgoem"
]
for part in images:
    file_path = Path(f"{part}.img")

    if file_path.is_file():
        print(f"\nFlashing {part}_a . . .")
        subprocess.run([
            "fastboot", "flash", f"{part}_a", file_path
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"\nFlashing {part}_b . . .")
        subprocess.run([
            "fastboot", "flash", f"{part}_b", file_path
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        print(f"{part} Not Found Or Unable To Flash!")

subprocess.run([
    "fastboot", "reboot", "fastboot"
])

time.sleep(2)

logicals = [
    "system", "product", "vendor", "vendor_dlkm", "system_dlkm", "system_ext"
]
for logic in logicals:
    file_path = Path(f"{logic}.img")

    if file_path.is_file():
        print(f"\nFlashing {logic}_a . . .")
        subprocess.run([
            "fastboot", "flash", f"{logic}_a", file_path
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"\nFlashing {logic}_b . . .")
        subprocess.run([
            "fastboot", "flash", f"{logic}_b", file_path
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        print(f"{logic} Not Found")

confirm = input("Wipe Cache, User Data, & Metadada? (yes/no): ")

if confirm.lower() != "yes":
    print("Okay, Stopping Here!")
    sys.exit()
subprocess.run([
    "fastboot", "-w"
], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

subprocess.run([
    "fastboot", "erase", "metadata"
], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

subprocess.run([
    "fastboot", "erase", "misc"
], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

sys.exit(0)