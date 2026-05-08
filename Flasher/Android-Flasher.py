from pathlib import Path
import shutil
import subprocess
import sys
import platform
import os
import time
print("This is an Android Flasher script.")
print("Please make sure you have the necessary tools installed, such as ADB and Fastboot.")
input("Make Sure You Are Operating In The Directory Of Your Images, Press Enter To Continue")
fastboot_path = shutil.which("fastboot")
if not fastboot_path:
    print("Error: Fastboot not found. Please make sure it is installed and in your PATH.")
else:
    print(f"Fastboot found at: {fastboot_path}")
adb_path = shutil.which("adb")
if not adb_path:
    print("Error: ADB Not Found. Please Make Sure It Is Installed And In Your PATH.")
else:
    print(f"ADB found at: {adb_path}")

subprocess.run(["adb", "reboot", "fastboot"])
subprocess.run(["fastboot", "reboot", "fastboot"])

subprocess.run(["fastboot", "devices"])
time.sleep(2)

partitions = [
    "recovery", "vendor_boot", "boot", "dtbo", "vbmeta", "init_boot", "odm", "system", "vendor", "product", "system_dlkm", "vendor_dlkm", "system_ext", "vbmeta_vendor", "vbmeta_system"
]
for part in partitions:
    file_path = Path(f"{part}.img")

    if file_path.is_file():
        print(f"\nFlashing {part}. . . ")
        subprocess.run([
            "fastboot", "flash", part, file_path
        ])
    else:
        print(f"{part} Not Found . . .")

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

subprocess.run(["fastboot", "reboot"])
sys.exit()