import shutil, subprocess, argparse, time, sys
from pathlib import Path

def clear():
    print("\033[2J]\033[3J]\033[1;1H")
clear()

print("""
███████╗██╗      █████╗ ███████╗██╗  ██╗
██╔════╝██║     ██╔══██╗██╔════╝██║  ██║
█████╗  ██║     ███████║███████╗███████║
██╔══╝  ██║     ██╔══██║╚════██║██╔══██║
██║     ███████╗██║  ██║███████║██║  ██║
╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
""")

print("This is a simple script for flashing firmware to your Android device, just make sure it isn't a Samsung!")
confirm = input("Continue? (y/N)\n")
if confirm.lower() in ("n", "no", "na", "nah", "nn", "noo", "nno", ""):
    clear()
    sys.exit(0)
elif confirm.lower() == "y":
    def main():
        parser = argparse.ArgumentParser(
                description="A stupid tool that just automates your Fastboot flashing (sort of)",
                epilog="Example: python ./genericFlasher.py --full",
        )
        main_group = parser.add_mutually_exclusive_group(required=True)
        main_group.add_argument(
          "--full",
          action="store_true",
          help="Flashes all firmware to your Android phone/tablet",
        )
        main_group.add_argument(
          "--android",
          action="store_true",
          help="Flashes JUST Android Partitions To A Phone, Skipping Risky Bootloader Images",
        )
        args = parser.parse_args()
        if not args.full and not args.android:
            parser.print_help()
            input("You must select an option when running the script to continue!\n")
            sys.exit(1)
        fastbootPath = shutil.which("fastboot")
        if not fastbootPath:
            input("Fastboot not found in your PATH!\n")
        else:
            print(f"Fastboot Found: {fastbootPath}")
            time.sleep(1)
        f1 = subprocess.run(
            [
                "fastboot",
                "devices",
            ],
            capture_output=True,
            text=True,
        )
        if "fastboot" in f1.stdout:
            pass
        else:
            adbPath = shutil.which("adb")
            if not adbPath:
                input("You don't have ADB in your PATH! Please install it manually or run Android-Tools.py!\n")
                sys.exit(1)
            else:
                adbCheck = subprocess.run(
                    [
                        "adb",
                        "devices",
                    ],
                    capture_output=True,
                    text=True,
                )
                if "device" in adbCheck.stdout.split():
                    pass
                elif "unauthorized" in adbCheck.stdout:
                    input("Your device still needs to allow your computer!\n")
                elif not "device" in adbCheck.stdout.split():
                    input("You either need to plug in your device or enable USB debugging in developer options!\n")
                    sys.exit(1)

                subprocess.run(
                    [
                        "adb",
                        "devices",
                    ],
                )
                adbChoice = input("Select your device by copying the ID and pasting it!\nDEVICE: ")
                subprocess.run(
                    [
                        "adb",
                        "-s",
                        adbChoice,
                        "shell",
                        "reboot",
                        "bootloader",
                    ],
                )
                time.sleep(15)
                if "fastboot" in subprocess.run(
                    [
                        "fastboot",
                        "devices",
                    ],
                    capture_output=True,
                    text=True,
                ):
                    clear()
                    subprocess.run(
                        [
                            "fastboot",
                            "devices",
                        ],
                    )
                    fastbootChoice = input("Select your device by copying the ID and pasting it!\nDEVICE: ")
                    blUnlock = subprocess.run(
                      [
                        "fastboot",
                        "-s",
                        fastbootChoice,
                        "getvar",
                        "all",
                      ],
                      capture_output=True,
                      text=True,
                    )
                    if "unlocked" in blUnlock.stdout:
                      pass
                    else:
                      input("Your device does not have an unlocked bootloader! Please click any key, then enter, to exit!\n")
                      sys.exit(1)
                    subprocess.run(
                        [
                            "fastboot",
                            "-s",
                            fastbootChoice,
                            "--set-active=a",
                        ],
                    )
                    if args.full:
                        images = [
                            "boot",
                            "abl",
                            "xbl",
                            "aop",
                            "aop_config",
                            "featenabler",
                            "bluetooth",
                            "modem",
                            "cpucp",
                            "cpucp_dtb",
                            "devcfg",
                            "init_boot",
                            "vendor_boot",
                            "recovery",
                            "vbmeta",
                            "vbmeta_vendor",
                            "vbmeta_system",
                            "xbl_ramdump",
                            "xbl_config",
                            "dsp",
                            "dtbo",
                            "keymaster",
                            "imagefv",
                            "tz",
                            "shrm",
                            "pvmfw",
                            "hyp",
                            "uefi",
                            "uefisecapp",
                            "qupfw",
                            "bootloader",
                            "radio",
                            "bl1",
                            "bl2",
                            "bl31",
                            "gsa",
                            "ldfw",
                            "pbl",
                            "tzsw",
                            "multiimgoem",
                            "vendor_kernel_boot",
                        ]
                        for part in images:
                            filePath = Path(f"{part}.img")
                            if filePath.is_file:
                                subprocess.run(
                                    [
                                        "fastboot",
                                        "-s",
                                        fastbootChoice,
                                        "flash",
                                        part,
                                        filePath,
                                    ],
                                )
                            else:
                                pass
                        time.sleep(2)
                        subprocess.run(
                            [
                                "fastboot",
                                "-s",
                                fastbootChoice,
                                "reboot",
                                "fastboot",
                            ],
                        )
                        logicals_full = [
                            "product",
                            "vendor",
                            "vendor_dlkm",
                            "system_ext",
                            "system_dlkm",
                            "system",
                            "odm",
                            "vendor_kernel_boot",
                        ]
                        for log in logicals_full:
                            filePath = Path(f"{log}.img")
                            if filePath.is_file():
                                subprocess.run(
                                    [
                                        "fastboot",
                                        "-s",
                                        fastbootChoice,
                                        "flash",
                                        log,
                                        filePath,
                                    ],
                                )
                            else:
                                pass
                    if args.logical:
                        subprocess.run(
                            [
                                "fastboot",
                                "-s",
                                fastbootChoice,
                                "reboot",
                                "fastboot",
                            ],
                        )
                        images = [
                            "boot",
                            "dtbo",
                            "vendor_boot",
                            "recovery",
                            "init_boot",
                            "vbmeta",
                            "vbmeta_vendor",
                            "vbmeta_system",
                            "system",
                            "product",
                            "vendor",
                            "vendor_dlkm",
                            "system_ext",
                            "system_dlkm",
                            "odm",
                            "vendor_kernel_boot",
                        ]
                        for part in images:
                            filePath = Path(f"{part}.img")
                            if filePath.is_file():
                                subprocess.run(
                                    [
                                        "fastboot",
                                        "-s",
                                        fastbootChoice,
                                        "flash",
                                        part,
                                        filePath,
                                    ],
                                )
                            else:
                                pass

if __name__ == "__main__":
    main()
