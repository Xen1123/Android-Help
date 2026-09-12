import shutil, subprocess, os, argparse, time, sys
from pathlib import Path

def clear():
    print("\033[2J]\033[3J]\033[1;1H")
clear()

print("""
██████╗ ███████╗██████╗ ██╗      ██████╗  █████╗ ████████╗
██╔══██╗██╔════╝██╔══██╗██║     ██╔═══██╗██╔══██╗╚══██╔══╝
██║  ██║█████╗  ██████╔╝██║     ██║   ██║███████║   ██║   
██║  ██║██╔══╝  ██╔══██╗██║     ██║   ██║██╔══██║   ██║   
██████╔╝███████╗██████╔╝███████╗╚██████╔╝██║  ██║   ██║   
╚═════╝ ╚══════╝╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
""")


print("\nThis script is different from master.py, it should be obvious from its name. It's boring. It doesn't really automate much, let you install anything, or have much error handling. It's small and efficient. It will basically read what apps you have installed, then ask 'do you want to remove this app?' for every app while giving you the package name.")
confirm = input("""\nContinue? (y/N)
""")
if confirm.lower() in ("n", "no", "na", "nah", "nn", "noo", "nno"):
    clear()
    sys.exit(0)
else:
    def main():
        parser = argparse.ArgumentParser(
                description="A stupid tool that just automates your ADB debloating (sort of)",
                epilog="Example: python ./genericDebloater.py --root",
        )
        main_group = parser.add_mutually_exclusive_group(required=True)
        main_group.add_argument("--root", action="store_true", help="Debloat An Android Device With Root Permissions, Deleting The App")
        main_group.add_argument("--noRoot", action="store_true", help="Debloat An Android Device Without Root, Just Disables Selected Apps")
        args = parser.parse_args()
        if not args.root and not args.noRoot:
            parser.print_help()
            input("\nClick Any Key To Exit")
            sys.exit(1)
        adbPath = shutil.which("adb")
        if adbPath:
            print(f"\nADB Found: {adbPath}")
            time.sleep(2)
        else:
            input("\nADB was not found as an executable! Please make sure it is installed and/or in your path, then click to continue! ")
            sys.exit(1)
        deviceCheck = subprocess.run(["adb", "devices"], capture_output=True, text=True)
        if not "device" in deviceCheck:
            print("Your device was not detected! Please make sure USB Debugging is enabled and allowed, your cable may also just not be connecting to the phone/tablet!")
            time.sleep(3)
            sys.exit(1)
        elif "unauthorized" in deviceCheck:
            print("Device is unauthorized! Please make sure your device has accepted your computer!")
            time.sleep(2)
            sys.exit(1)
        else:
            pass
        result = subprocess.run(["adb", "shell", "pm", "list", "packages"], capture_output=True, text=True)
        installed_apps = [line.replace("package:", "").strip() for line in result.stdout.splitlines()]
        if args.noRoot:
            for app in result:
                appDis = input(f"""\nRemove {app}? (y/N)
                """)
                if appDis.lower() in ("y", "ye", "ys", "yeah", "yes"):
                    subprocess.run(["adb", "shell", "pm", "disable-user", "--user", "0", app])
                else:
                    pass
                    
        elif args.root:
            rootCheck = subprocess.run(["adb", "shell", "su", "-c", "whoami"], capture_output=True, text=True)
            if "root" in rootCheck.stdout:
                for app in result:
                    rootRemove = input(f"""\nRemove {app}? (y/N)
                    """)
                    if rootRemove.lower() in ("y", "ye", "ys", "yeah", "yes"):
                        subprocess.run(["adb", "shell", "su", "-c", "pm", "uninstall", "--user", "0", app])
                    elif:
                        pass
            else:
                confirm = input("""You do not have an accessible root interface! Would you like to switch to disabling? (Y/n)
                """)
                if confirm.lower() in ("y", "", "ye", "ys", "yeah", "yea", "yy", "yeas"):
                    appDis = input(f"""\nRemove {app}? (y/N)
                    """)
                    if appDis.lower() in ("y", "ye", "ys", "yeah", "yes"):
                        subprocess.run(["adb", "shell", "pm", "disable-user", "--user", "0", app])
                    else:
                        pass
                else:
                    sys.exit(1)

if __name__ == "__main__":
    main()
