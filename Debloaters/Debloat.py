from pathlib import Path
import shutil
import os
import subprocess
import time
import os
import sys
import urllib.request

apps = [
    
    "com.samsung.sree",
    "com.samsung.kidsplay",
    "com.samsung.android.kidsinstaller",
    "com.samsung.android.homemade",
    "com.samsung.aasaservice",
    "com.samsung.android.app.updatecenter",
    "com.samsung.android.mapsagent",
    "com.samsung.android.bbc.bbcagent",
    "android.autoinstalls.config.samsung",
    "com.samsung.android.app.omcagent",
    "com.samsung.android.livestickers",
    "com.samsung.android.rubin.app",
    "com.samsung.android.sdm.config",
    "com.samsung.android.game.gametools",
    "com.samsung.android.game.gamehome",
    "com.samsung.android.game.gos",
    "com.samsung.gpuwatchapp",
    "com.samsung.android.app.spage",
    "com.sec.spp.push",
    "com.samsung.android.stickercenter",
    "com.sec.android.app.ve.vebgm",
    "com.sec.android.widgetapp.samsungapps",
    "com.audible.application",
    "com.google.ar.core",
    "com.sec.android.preloadinstaller",
    "com.microsoft.skydrive",
    "com.sec.android.daemonapp",
    "com.google.android.music",
    "com.sec.android.app.popupcalculator",
    "com.microsoft.office.officehubrow",
    "com.samsung.android.galaxy",
    "com.sec.android.app.sbrowser",
    "com.samsung.android.email.provider",
    
    "com.google.android.googlequicksearchbox",
    "android.overlay.gms.region.all",
    "android.overlay.gms.region.row",
    "com.android.egg",
    "com.android.microdroid.empty_payload",
    "com.android.providers.partnerbooks",
    "com.android.settings.overlay.personalsafety",
    "com.android.settings.overlay.turbo",
    "com.android.setupwizard.overlay",
    "com.android.systemui.overlay.gms",
    "com.aura.oobe.solutions",
    "com.goodfix.fingerprint.setting",
    "com.google.ambient.streaming",
    "com.google.android.accessibility.switchaccess",        
    "com.google.android.adservices.api",
    "com.google.android.apps.docs",
    "com.google.android.apps.restore",
    "com.google.android.apps.tachyon",
    "com.google.android.apps.youtube.music",
    "com.google.android.calculator",
    "com.google.android.federatedcompute",
    "com.google.android.feedback",
    "com.google.android.gms.location.history",
    "com.google.android.keep",
    "com.google.android.ondevicepersonalization.services",
    "com.google.android.onetimeinitializer",
    "com.google.android.overlay.gmsconfig.healthconnect",
    "com.google.android.overlay.gmsconfig.tetheringentitlement",
    "com.google.android.videos",
    "com.google.mainline.adservices",
    "com.nothing.agreement",
    "com.nt.android.overlay.gmsconfig.safetycenter",
    "com.nt.android.overlay.gmsconfig.settings",
    "com.nt.android.overlay.gmsconfig.settingsprovider",
    "com.nt.diagswitch",
    "com.qti.dcf",
    "com.qti.qcc",
    "com.qualcomm.location",
    "com.qualcomm.qti.biometrics.fingerprint.service",
    "com.qualcomm.qti.qms.serivce.connectionsecurity",
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
    "com.google.android.apps.walletnfcrel",
    "com.fitbit.FitbitMobile",
    "com.google.android.apps.adm",
    "com.google.ar.core",
    "com.google.pixel.livewallpaper",
    "org.lineageos.audiofx",
    "org.lineageos.jelly",
    "com.google.android.apps.healthdata",
    "com.android.calculator2",
    "org.lineageos.etar",
    "com.google.android.apps.tips",
    "com.google.android.apps.chromecast.app",
    "org.fossify.gallery",
    "com.google.android.apps.subscriptions.red",
    "com.google.android.apps.magazines",
    "com.google.android.apps.docs.editors.docs",
    "org.lineageos.twelve",
    "uk.akane.accord",
    "com.google.android.apps.work.cloudpc",
    "com.google.android.apps.wearables.maestro.companion",
    "com.google.android.apps.recorder",
    "org.lineageos.recorder",
    "com.google.android.apps.safetyhub",
    "com.google.android.marvin.talkback",
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

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
clear()

print(r"""
                                                          
██████╗ ███████╗██████╗ ██╗      ██████╗  █████╗ ████████╗
██╔══██╗██╔════╝██╔══██╗██║     ██╔═══██╗██╔══██╗╚══██╔══╝
██║  ██║█████╗  ██████╔╝██║     ██║   ██║███████║   ██║   
██║  ██║██╔══╝  ██╔══██╗██║     ██║   ██║██╔══██║   ██║   
██████╔╝███████╗██████╔╝███████╗╚██████╔╝██║  ██║   ██║   
╚═════╝ ╚══════╝╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
                                                          
""")

adb_path = shutil.which("adb")

confirm = input("""\nHello! This script will debloat your Android device! 
If you have root, apps will be fully removed, if not, apps will just be disabled! Continue? (yes/no) """)

if confirm.lower() != "yes":
    clear()
    print("\nOkay! Have a nice day! :) ")
    sys.exit(0)
else:
    pass

if not adb_path:
    print("\nYou do not have ADB installed or in your system PATH!")
    sys.exit(0)
else:
    print(f"\nADB Found At: {adb_path}")
    time.sleep(2)

try:
    result = subprocess.run([
        "adb", "devices"
    ], capture_output=True, text=True, check=True)

    if "unauthorized" in result.stdout:
        print("\nDevice Not Authorized")
        sys.exit(1)
    
    if "device" not in result.stdout.split():
        print("\nNo Device!")
        sys.exit(1)
except subprocess.CalledProcessError:
    print("Failed To Run ADB! Is It In Your PATH?")
    sys.exit(1)

root_check = subprocess.run(["adb", "shell", "su -c whoami"], capture_output=True, text=True)

if root_check.stdout.strip() != "root":
    print("\nRoot Not Detected! Disabling Apps!")
    time.sleep(2)
    clear()
    for app in apps:
        print(f"\nDisabling {app}")
        subprocess.run([
            "adb", "shell", "pm", "disable-user", "--user", "0", app
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    clear()
    try:
        os.mkdir("APKs")
    except FileExistsError:
        pass
    print(f"\nYou're In {os.getcwd()}, Chamging To APK Folder!")
    os.chdir("APKs")

    confirm = input("\nInstall Vyxel Apps? It Is An Open Source App Store That Has MANY Sources, Not Just F-Droid! (y/n) ")
    if confirm.lower() != "y":
        clear()
    else:
        clear()
        print("\nGrabbing Vyxel APK From Web!")
        url = "https://github.com/NikhilKain/vyxel-apps/releases/download/v1.0.2/VyxelApps-v1.0.2.apk"
        file = "Vyxel_Apps.apk"
        urllib.request.urlretrieve(url, file)

        print("\nInstalling Vyxel!")
        subprocess.run([
            "adb", "install", "Vyxel_Apps.apk"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        clear()

    confirm = input("\nInstall ArchiveTune? [Youtube Music Client] (y/n) ")
    if confirm.lower() != "y":
        clear()
    else:
        clear()
        print("\nGrabbing ArchiveTune APK From Web!")
        url = "https://github.com/koiverse/ArchiveTune/releases/download/v13.4.0/app-mobile-universal-release.apk"
        file_name = "ArchiveTune.apk"
        urllib.request.urlretrieve(url, file_name)

        print("\nInstalling ArchiveTune!")
        subprocess.run([
            "adb", "install", "ArchiveTune.apk"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        clear()

    confirm = input("\nInstall Localsend? [Basically Open Source Android AirDrop] (y/n) ")
    if confirm.lower() != "y":
        clear()
    else:
        clear()
        print("\nGrabbing Localsend APK From Web!")
        url = "https://github.com/localsend/localsend/releases/download/v1.17.0/LocalSend-1.17.0-android-arm64v8.apk"
        file = "Localsend.apk"
        urllib.request.urlretrieve(url, file)

        print("\nInstalling Localsend!")
        subprocess.run([
            "adb", "install", "Localsend.apk"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        clear()

    confirm = input("\nInstall Magisk? (For Rooting, If You Don't Have OEM Unlocking, Don't Even Bother. (y/n) ")
    if confirm.lower() != "y":
        clear()
    else:
        clear()
        print("\nGrabbing Magisk APK From Web!")
        url = "https://github.com/topjohnwu/Magisk/releases/download/v30.7/Magisk-v30.7.apk"
        file = "Magisk.Apk"
        urllib.request.urlretrieve(url, file)

        print("\nInstalling Magisk!")
        subprocess.run([
            "adb", "install", "Magisk.apk"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        clear()

else:
    clear()
    print("\nRoot Detected! Removing Applications From System!")
    time.sleep(2)
    clear()
    for app in apps:
        print(f"\nUninstalling {app}")
        pm_uninstall = f"pm uninstall --user 0 {app}"
        subprocess.run([
            "adb", "shell", "su", "-c", pm_uninstall
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    clear()
    try:
        os.mkdir("APKs")
    except FileExistsError:
        pass
    print(f"\nYou're In {os.getcwd()}, Chamging To APK Folder!")
    os.chdir("APKs")

    confirm = input("\nInstall Vyxel Apps? It Is An Open Source App Store That Has MANY Sources, Not Just F-Droid! (y/n) ")
    if confirm.lower() != "y":
        clear()
    else:
        clear()
        print("\nGrabbing Vyxel APK From Web!")
        url = "https://github.com/NikhilKain/vyxel-apps/releases/download/v1.0.2/VyxelApps-v1.0.2.apk"
        file = "Vyxel_Apps.apk"
        urllib.request.urlretrieve(url, file)

        print("\nInstalling Vyxel!")
        subprocess.run([
            "adb", "install", "Vyxel_Apps.apk"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        clear()

    confirm = input("\nInstall ArchiveTune? [Youtube Music Client] (y/n) ")
    if confirm.lower() != "y":
        clear()
    else:
        clear()
        print("\nGrabbing ArchiveTune APK From Web!")
        url = "https://github.com/koiverse/ArchiveTune/releases/download/v13.4.0/app-mobile-universal-release.apk"
        file_name = "ArchiveTune.apk"
        urllib.request.urlretrieve(url, file_name)

        print("\nInstalling ArchiveTune!")
        subprocess.run([
            "adb", "install", "ArchiveTune.apk"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        clear()

    confirm = input("\nInstall Localsend? [Basically Open Source Android AirDrop] (y/n) ")
    if confirm.lower() != "y":
        clear()
    else:
        clear()
        print("\nGrabbing Localsend APK From Web!")
        url = "https://github.com/localsend/localsend/releases/download/v1.17.0/LocalSend-1.17.0-android-arm64v8.apk"
        file = "Localsend.apk"
        urllib.request.urlretrieve(url, file)

        print("\nInstalling Localsend!")
        subprocess.run([
            "adb", "install", "Localsend.apk"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        clear()

def reboot_menu():
    options = [
    "Reboot Now",
    "End The Script"
]

    while True:
        print("\nPlease Select Your Choice: ")
        for i, opt in enumerate(options, 1):
            print(f"{i}) {opt}")

        choice = input("\nEnter Choice Number: ")

        if choice == "1":
            subprocess.run([
                "adb", "reboot"
            ])
            clear()
            sys.exit()
        elif choice == "2":
            clear()
            sys.exit()
        else:
            print(f"Invalid Choice: {choice}")
clear()
reboot_menu()
