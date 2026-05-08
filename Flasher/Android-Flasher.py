from pathlib import Path
import shutil
import subprocess
import time
import sys
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
file_path = Path("recovery.img")
if file_path.is_file():
    subprocess.run(["fastboot", "flash", "recovery", file_path])
else:
    print("Error: recovery.img not found. You Either Don't Use A 'recovery.img' Device, Or You Are Missing Files.")

file_path = Path("vendor_boot.img")
if file_path.is_file():
    subprocess.run([
        "fastboot", "flash", "vendor_boot", file_path
    ])
else:
    print("Error: vendor_boot.img not found. You Either Don't Use A 'vendor_boot.img' Device, Or You Are Missing Files.")

file_path = Path("boot.img")
if file_path.is_file():
    subprocess.run([
        "fastboot", "flash", "boot", file_path
    ])
else:
    print("Error: boot.img not found.")

file_path = Path("dtbo.img")
if file_path.is_file():
    subprocess.run([
        "fastboot", "flash", "dtbo", file_path
    ])
else:
    print("Error: dtbo.img not found.")

file_path = Path("vbmeta.img")
if file_path.is_file():
    subprocess.run([
        "fastboot", "flash", "vbmeta", file_path
    ])
else:
    print("Error: vbmeta.img not found.")

file_path = Path("init_boot.img")
if file_path.is_file():
    subprocess.run([
        "fastboot", "flash", "init_boot", file_path
    ])
else:
    print("Error: init_boot.img not found.")

file_path = Path("odm.img")
if file_path.is_file():
    subprocess.run([
        "fastboot", "flash", "odm", file_path
    ])
else:
    print("Error: odm.img not found.")

file_path = Path("system.img")
if file_path.is_file():
    subprocess.run([
        "fastboot", "flash", "system", file_path
    ])
else:
    print("Error: system.img not found.")

file_path = Path("vendor.img")
if file_path.is_file():
    subprocess.run([
        "fastboot", "flash", "vendor", file_path
    ])
else:    
    print("Error: vendor.img not found.")

file_path = Path("system_ext.img")
if file_path.is_file():
    subprocess.run([
        "fastboot", "flash", "system_ext", file_path
    ])
else:
    print("Error: system_ext.img not found.")

file_path = Path("product.img")
if file_path.is_file():
    subprocess.run([
        "fastboot", "flash", "product", file_path
    ])
else:
    print("Error: product.img not found.")

file_path = Path("system_dlkm.img")
if file_path.is_file():
    subprocess.run([
        "fastboot", "flash", "system_dlkm", file_path
    ])
else:
    print("Error: system_dlkm.img not found.")

file_path = Path("vendor_dlkm.img")
if file_path.is_file():
    subprocess.run([
        "fastboot", "flash", "vendor_dlkm", file_path
    ])
else:
    print("Error: vendor_dlkm.img not found.")

file_path = Path("system_ext.img")
if file_path.is_file():
    subprocess.run([
        "fastboot", "flash", "system_ext", file_path
    ])
else:
    print("Error: system_ext.img not found.")

file_path = Path("vbmeta.img")
if file_path.is_file():
    subprocess.run([
        "fastboot", "flash", "vbmeta", file_path
    ])
else:
    print("Error: vbmeta.img not found.")

file_path = Path("vbmeta_vendor.img")
if file_path.is_file():
    subprocess.run([
        "fastboot", "flash", "vbmeta_vendor", file_path
    ])
else:
    print("Error: vbmeta_vendor.img not found.")

file_path = Path("vbmeta_system.img")
if file_path.is_file():
    subprocess.run([
        "fastboot", "flash", "vbmeta_system", file_path
    ])
else:
    print("Error: vbmeta_system.img not found.")

subprocess.run(["fastboot", "reboot"])
sys.exit()