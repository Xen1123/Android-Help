import shutil
import subprocess
import sys
import os
import urllib.request
from pathlib import Path
print("This Script Will Debloat Your Android Device!")
print("Please Make Sure You Have ROOT Access So Apps Will Actually Be Deleted!")
input("Press Enter To Continue...")
adb_path = shutil.which("adb")
if not adb_path:
    print("Error: ADB Not Found. Please Make Sure It Is Installed And In Your PATH.")
    input("Press Enter To Exit . . .")
    sys.exit()
else:
    result = subprocess.run(["adb", "shell", "su -c whoami"], capture_output=True, text=True)
    if result.stdout.strip() != "root":
        print("Error: You aren't root! Exiting.")
        sys.exit(1)
    else:
        print(f"ADB found at: {adb_path}")
        apps = [
            "com.google.android.googlequicksearchbox",
            "com.google.android.youtube",
            "com.google.android.odad",
            "com.microsoft.appmanager",
            "com.microsoft.skydrive",
            "com.samsung.android.beaconmanager",
            "com.samsung.android.app.omcagent",
            "com.samsung.android.app.reminder",
            "com.sec.android.app.billing",
            "com.samsung.android.app.spage",
            "com.sec.android.app.sbrowser",
            "com.samsung.android.samsungpass",
            "com.sec.spp.push",
            "com.samsung.android.stickercenter",
            "com.google.android.game.gamehome",
            "com.samsung.android.game.gametools",
            "com.samsung.android.aremoji",
            "com.samsung.android.samsungpassautofill",
            "com.sec.android.mimage.avatarstickers",
            "io.chaldeaprjkt.gamespace",
            "com.google.android.apps.betterbug",
            "com.android.yadayada",
            "com.google.android.safetycore",
            "com.google.android.contactkeys",
            "org.lineageos.glimpse",
            "com.android.dialer",
            "com.google.android.apps.walletnfcrel",
            "com.fitbit.FitbitMobile",
            "com.google.android.apps.adm",
            "com.google.ar.core",
            "com.google.pixel.livewallpaper",
            "com.google.android.apps.restore",
            "org.lineageos.audiofx",
            "org.lineageos.jelly",
            "com.google.android.apps.healthdata",
            "com.android.calculator2",
            "org.lineageos.etar",
            "com.google.android.apps.tips",
            "com.google.android.apps.tachyon",
            "com.google.android.apps.chromecast.app",
            "org.fossify.gallery",
            "com.google.android.videos",
            "com.google.android.apps.subscriptions.red",
            "com.google.android.apps.magazines",
            "com.google.android.apps.docs.editors.docs",
            "com.google.android.apps.youtube.music",
            "org.lineageos.twelve",
            "uk.akane.accord",
            "com.google.android.calculator",
            "com.google.android.apps.work.cloudpc",
            "com.google.android.apps.wearables.maestro.companion",
            "com.google.android.apps.recorder",
            "org.lineageos.recorder",
            "com.google.android.apps.safetyhub",
            "com.google.android.marvin.talkback",
            "com.gogole.ambient.streaming",
            "com.google.android.calendae",
            "com.google.android.apps.emojiwallpaper",
            "com.google.android.apps.aiwallpapers",
            "com.google.android.apps.carrier.log",
            "com.google.android.apps.pixel.familyspace",
            "com.google.android.apps.pixel.creativeassistant",
            "com.google.android.apps.pixel.relationships",
            "com.google.android.apps.pixel.support",
            "com.google.android.apps.wallpaper.pixel",
            "com.android.adservices.api",
            "com.android.backupconfirm",
            "com.google.audio.hearing.visualization.accessibility.scribe",
            "com.google.android.accessibility.soundamplifier",
            "com.google.android.apps.accessibility.voiceaccess",
            "com.android.companiondevicemanager",
            "com.android.providers.telephony.auto_generated_characteristics_rro",
            "com.android.providers.settings.auto_generated_rro_vendor__",
            "com.google.android.apps.weather",
            "com.google.android.apps.diagnosticstool",
    ]

    for app in apps:
        print(f"\nDELETING {app}")
        subprocess.run([
            "adb", "shell", "pm", "uninstall", "--user", "0", app
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def install_stuff():
    options = [
        "Install Droidfy And Outertune",
        "Skip Installing Droidfy And Outertune",
        "Install Droidfy Only",
        "Install Outertune Only"
    ]

    while True:
        print("Please Select Your Choice:")
        for i, opt in enumerate(options, 1):
            print(f"{i}) {opt}")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            url = "https://github.com/Droid-ify/client/releases/download/v0.7.1/app-release.apk"
            file_name = "Droidify.apk"
            urllib.request.urlretrieve(url, file_name)

            url = "https://github.com/OuterTune/OuterTune/releases/download/v0.10.1/OuterTune-0.10.1-full-release-71.apk"
            file_name = "Outertune.apk"
            urllib.request.urlretrieve(url, file_name)

            subprocess.run([
                "adb", "install", "Droidify.apk"
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run([
                "adb", "install", "Outertune.apk"
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            break
        elif choice == "2":
            break
        elif choice == "3":
            url = "https://github.com/Droid-ify/client/releases/download/v0.7.1/app-release.apk"
            file_name = "Droidify.apk"
            urllib.request.urlretrieve(url, file_name)
            
            subprocess.run([
                "adb", "install", "Droidify.apk"
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            break
        elif choice == "4":
            url = "https://github.com/OuterTune/OuterTune/releases/download/v0.10.1/OuterTune-0.10.1-full-release-71.apk"
            file_name = "Outertune.apk"
            urllib.request.urlretrieve(url, file_name)
            subprocess.run([
                "adb", "install", "Outertune.apk"
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            break
        else:
            print(f"Invalid Choice: {choice}")

install_stuff()

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

    def reboot_menu():
        options = [
            "Reboot Now",
            "End The Script"
        ]

        while True:
            print("Please Select Your Choice:")
            for i, opt in enumerate(options, 1):
                print(f"{i}) {opt}")

            choice = input("Enter Choice Number: ")

            if choice == "1":
                subprocess.run([
                    "adb", "reboot"
                ])
                sys.exit()
            elif choice == "2":
                sys.exit()
            else:
                print(f"Invalid Choice: {choice}")
    reboot_menu()