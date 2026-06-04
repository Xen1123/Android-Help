from pathlib import Path
import argparse, shutil, subprocess, sys, time, os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear()

print(r"""
 █████╗ ███╗   ██╗██████╗ ██████╗  ██████╗ ██╗██████╗ 
██╔══██╗████╗  ██║██╔══██╗██╔══██╗██╔═══██╗██║██╔══██╗
███████║██╔██╗ ██║██║  ██║██████╔╝██║   ██║██║██║  ██║
██╔══██║██║╚██╗██║██║  ██║██╔══██╗██║   ██║██║██║  ██║
██║  ██║██║ ╚████║██████╔╝██║  ██║╚██████╔╝██║██████╔╝
╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚═════╝ 
""")

fastboot_path = shutil.which("fastboot")
if not fastboot_path:
    clear()
    print("Fastboot Not Installed Or In Your Path!")
    input("Click Anywhere To Continue ")
    sys.exit()
else:
    pass

adb_path = shutil.which("adb")
if not adb_path:
    clear()
    print("ADB Not Installed Or In Your Path!")
    input("Click Anywhere To Continue ")
    sys.exit()
else:
    pass

def main():

    parser = argparse.ArgumentParser(
        description="Multi-Device Android Flasher Utility",
        epilog="Example: python flasher.py --full"
    )

    parser.add_argument("--full", action ="store_true", help="Flash All Factory Firmare")
    parser.add_argument("--android", action="store_true", help="Flash Just Android Partitions (VERY Low Chance of A Hard Brick)")
    parser.add_argument("--verbose", action="store_true", help="Stops Commands From Being Silent So You Can See Outputs (Add This Flag With A Flashing Flag Or Nothing Will Happen)")

    args = parser.parse_args()

    if args.full:
        print("\n>> - FULL FACTORY FLASH - <<")
        time.sleep(3)
        print("\nRebooting To Bootloader Fastboot (ABL)")
        if args.verbose:
            subprocess.run(["adb", "reboot", "bootloader"])
            subprocess.run(["fastboot", "reboot", "bootloader"])
        else:
            subprocess.run(["adb", "reboot", "bootloader"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run(["fastboot", "reboot", "bootloader"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        time.sleep(2)

        images = [
            "boot", "abl", "xbl", "aop", "aop_config", "featenabler", "bluetooth", "modem", "cpucp", "cpucp_dtb", "devcfg", "init_boot", "vendor_boot", "recovery", "vbmeta", 
            "vbmeta_vendor", "vbmeta_system", "xbl_ramdump", "xbl_config", "dsp", "dtbo", "keymaster", "imagefv", "tz", "shrm", "pvmfw", "odm", "hyp", "uefi", 
            "uefisecapp", "qupfw", "bootloader", "radio", "bl1", "bl2", "bl31", "gsa", "ldfw", "pbl", "tzsw", "multiimgoem"
        ]
        for part in images:
            file_path = Path(f"{part}.img")

            if args.verbose:
                    if file_path.is_file():
                        subprocess.run(["fastboot", "flash", "--slot=all", part, file_path])

                    else:
                        print(f"\nFILE NOT FOUND: {part}.img")
            else:
                    if file_path.is_file():
                        print(f"\nFlashing {part}.img")
                        subprocess.run(["fastboot", "flash", "--slot=all", part, file_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    else:
                        print(f"\nFILE NOT FOUND: {part}.img")

        time.sleep(2)
        clear()
        print("\nRebooting To Fastbootd")
        time.sleep(2)
        if args.verbose:
            subprocess.run(["fastboot", "reboot", "fastboot"])
        else:
            subprocess.run(["fastboot", "reboot", "fastboot"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        time.sleep(2)

        clear()

        images = [
            "system", "product", "vendor", "vendor_dlkm", "system_ext", "system_dlkm"
        ]

        for logic in images:
            file_path = Path(f"{logic}.img")
            
            if args.verbose:
                if file_path.is_file():
                    subprocess.run(["fastboot", "flash", "--slot=all", logic, file_path])
                else:
                    print(f"\nFILE NOT FOUND: {logic}.img")
            else:
                if file_path.is_file():
                    print(f"\nFlashing {logic}.img")
                    subprocess.run(["fastboot", "flash", logic, file_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                else:
                    print(f"\nFILE NOT FOUND: {logic}.img")

        time.sleep(2)
        clear()

        confirm = input("Reboot? (You may be prompted by the android system to factory reset first, that is normal) (y/n) ")
        if confirm.lower() != 'y':
            print("Exiting The Script!")
            time.sleep(1.5)
            input("Click A Key To Close The Script ")
        else:
            if args.verbose:
                print("Rebooting Now!")
                subprocess.run(["fastboot", "reboot"])
                input("Click A Key To Close The Script ")
            else:
                print("Rebooting Now!")
                subprocess.run(["fastboot", "reboot"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                input("Click A Key To Close The Script ")

    if args.android:
        print("\n>> - ANDROID SYSTEM FLASH - <<")
        time.sleep(3)
        if args.verbose:
            print("\nRebooting To Bootloader Fastboot (ABL)")
            subprocess.run(["adb", "reboot", "bootloader"])
            subprocess.run(["fastboot", "reboot", "bootloader"])
        else:
            print("\nRebooting To Bootloader Fastboot (ABL)")
            subprocess.run(["adb", "reboot", "bootloader"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run(["fastboot", "reboot", "bootloader"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        time.sleep(2)

        images = [
            "boot", "dtbo", "vendor_boot", "recovery", "init_boot", "odm", "vbmeta", "vbmeta_vendor", "vbmeta_system"
        ]

        for part in images:
            file_path = Path(f"{part}.img")
            
            if args.verbose:
                if file_path.is_file():
                    subprocess.run(["fastboot", "flash", "--slot=all", part, file_path])
                else:
                    print(f"\nFAILED TO FLASH: {part}.img")
            else:
                if file_path.is_file():
                    print(f"\nFlashing {part}.img")
                    subprocess.run(["fastboot", "flash", "--slot=all", part, file_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                else:
                    print(f"\nFAILED TO FLASH: {part}.img")

        time.sleep(2)
        clear()
        print("\nRebooting To Fastbootd")
        time.sleep(2)

        if args.verbose:
            subprocess.run(["fastboot", "reboot", "fastboot"])
        else:
            subprocess.run(["fastboot", "reboot", "fastboot"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        time.sleep(2)

        clear()

        images = [
            "system", "product", "vendor", "vendor_dlkm", "system_ext", "system_dlkm"
        ]

        for logic in images:
            file_path = Path(f"{logic}.img")
            
            if args.verbose:
                if file_path.is_file():
                    subprocess.run(["fastboot", "flash", "--slot=all", logic, file_path])
                else:
                    print(f"\nFILE NOT FOUND: {logic}.img")
            else:
                if file_path.is_file():
                    print(f"\nFlashing {logic}.img")
                    subprocess.run(["fastboot", "flash", "--slot=all", logic, file_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                else:
                    print(f"\nFILE NOT FOUND: {logic}.img")

        time.sleep(2)
        clear()

        confirm = input("Reboot? (You may be prompted by the android system to factory reset first, that is normal) (y/n) ")
        if confirm.lower() != 'y':
            print("Exiting The Script!")
            time.sleep(1.5)
            input("Click A Key To Close The Script ")
        else:
            if args.verbose:
                print("Rebooting Now!")
                subprocess.run(["fastboot", "reboot"])
                input("Click A Key To Close The Script ")
            else:
                print("Rebooting Now!")
                subprocess.run(["fastboot", "reboot"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                input("Click A Key To Close The Script ")
    else:
        pass

if __name__ == "__main__":
    main()