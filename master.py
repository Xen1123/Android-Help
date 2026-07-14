import os, subprocess, shutil, sys, time, argparse, urllib.request
from pathlib import Path

result_choice = subprocess.run(["adb", "shell", "pm", "list", "packages"], capture_output=True, text=True)
installed_apps_choice = [line.replace("package:", "").strip() for line in result_choice.stdout.splitlines()]


app_mapping = {
    "moe.rukamori.archivetune": "ArchiveTune",
    "org.localsend.localsend_app": "Localsend",
    "com.topjohnwu.magisk": "Maigsk",
    "com.vythera.vyxelapps": "VyxelApps",
}
    
def choice():
    for package, display_name in app_mapping.items():
        if package in installed_apps_choice:
            confirm = input(f"Remove {display_name}? (y/n) ")
            if confirm.lower() != "y":
                verbose_clear()
            else:
                if args.noroot:
                    if args.verbose:
                        subprocess.run(["adb", "shell", "pm", "disable-user", "--user", "0", package])
                    else:
                        print(f"Removing: {package}")
                        subprocess.run(["adb", "shell", "pm", "disable-user", "--user", "0", package], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                if args.root:
                    if args.verbose:
                        subprocess.run(["adb", "shell", "su", "-c", "pm", "uninstall", "--user", "0", package])
                    else:
                        print(f"Removing: {package}")
                    subprocess.run(["adb", "shell", "su", "-c", "pm", "uninstall", "--user", "0", package], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
apps = [
    "com.google.android.apps.bard",
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
    "com.google.android.apps.pixel.nowplaying",
]

gstandard = [
    "com.google.android.apps.photos",
    "com.google.android.apps.nbu.files",
    "com.google.android.calendar",
    "com.google.android.gm",
    "com.google.android.apps.maps",
    "com.google.android.apps.searchlite",
    "com.google.android.apps.mapslite",
    "com.android.chrome",
    "com.chrome.beta",
    "com.chrome.canary",
    "com.chrome.dev",
    "com.google.android.youtube",
    "com.google.android.googlequicksearchbox",
]

gFULL = [
    "com.android.vending",
    "com.google.android.gms",
    "com.google.android.apps.messaging",
    "com.google.android.contacts",
    "com.google.android.dialer",
    "com.google.android.googlequicksearchbox",
    "com.google.android.apps.photos",
    "com.google.android.apps.nbu.files",
    "com.google.android.calendar",
    "com.google.android.gm",
    "com.google.android.apps.maps",
    "com.google.android.apps.searchlite",
    "com.google.android.apps.mapslite",
    "com.android.chrome",
    "com.chrome.canary",
    "com.chrome.dev",
    "com.google.android.youtube",
]

result = subprocess.run(["adb", "shell", "pm", "list", "packages"], capture_output=True, text=True)
installed_apps = [line.replace("package:", "").strip() for line in result.stdout.splitlines()]

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
clear()

print("""
 █████╗ ███╗   ██╗██████╗ ██████╗  ██████╗ ██╗██████╗ 
██╔══██╗████╗  ██║██╔══██╗██╔══██╗██╔═══██╗██║██╔══██╗
███████║██╔██╗ ██║██║  ██║██████╔╝██║   ██║██║██║  ██║
██╔══██║██║╚██╗██║██║  ██║██╔══██╗██║   ██║██║██║  ██║
██║  ██║██║ ╚████║██████╔╝██║  ██║╚██████╔╝██║██████╔╝
╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚═════╝ 
""")

def main():
    parser = argparse.ArgumentParser(
            description="Multi-Device Tool For Debloating And Flashing",
            epilog="Example: python master.py --debloat --noroot --verbose",
    )
    
    main_group = parser.add_mutually_exclusive_group(required=True)
    parser.add_argument("--verbose", action="store_true", help="Shows ALL Logs And Doesn't Clear The Terminal") 
    main_group.add_argument("--debloat", action="store_true", help="Debloat An Android Device With ADB")
    main_group.add_argument("--flash", action="store_true", help="Flash Firmware (or ROMs) To An Android Device With Fastboot")
    parser.add_argument("--root", action="store_true", help="Debloat An Android Device With Root Permissions, Deleting The App")
    parser.add_argument("--noroot", action="store_true", help="Debloat An Android Device Without Root Access, Disables Apps")

    parser.add_argument("--full", action="store_true", help="Flashes ALL Firmware To An Android Device, Includes Bootloader Images")
    parser.add_argument("--logical", action="store_true", help="Flashes JUST Android Partitions To A Phone, Skipping Risky Bootloader Images")

    args = parser.parse_args()
    
    if not args.debloat and not args.flash:
        parser.print_help()
        input("\nClick Any Key To Exit")
        sys.exit(0)
    
    def verbose_clear():
        if args.verbose:
            pass
        else:
            clear()

    adb_path = shutil.which("adb")
    if adb_path:
        print(f"\nADB Found At: {adb_path}")
    else:
        print("\nADB Not Found, It May Not Be Installed Or In Your Path!")
    fastboot_path = shutil.which("fastboot")
    if fastboot_path:
        print(f"\nFastboot Found At: {fastboot_path}")
    else:
        print("\nFastboot Not Found, It May Not Be Installed Or In Your Path!")
    if args.debloat:
        print("\nDebloating Device!")
        if not adb_path:
            input("ADB NOT AVAILABLE ")
            sys.exit(0)
        result = subprocess.run(["adb", "devices"], capture_output=True, text=True, check=True)
        if "device" not in result.stdout.split():
            input("\nNo Device! ")
            sys.exit(0)
        if "unauthorized" in result.stdout:
            input("\nDevice Not Authorized! ")
            sys.exit(0)
        if not "device" in result.stdout:
            input("\nADB Unable To Run! ")
            sys.exit(0)
        if "device" in result.stdout.split():
            pass

        if args.root:
            root_result = subprocess.run(["adb", "shell", "su", "-c", "whoami"], capture_output=True, text=True, check=True)
            if "root" in root_result.stdout:
                verbose_clear()
                for app in apps:
                    if app in installed_apps:
                        if args.verbose:
                            subprocess.run(["adb", "shell", "su", "-c", "pm", "uninstall", "--user", "0", app])
                        else:
                            print(f"\nUninstalling: {app}")
                            subprocess.run(["adb", "shell", "su", "-c", "pm", "uninstall", "--user", "0", app], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    else:
                        pass
                verbose_clear()
                confirm = input("\nRemove The Standard Google Apps? (Photos, Chrome, Google, Gmail, Maps, keeps Play Store and Play Services)  (y/n ")
                if confirm.lower() != "y":
                    verbose_clear()
                if confirm.lower() == "y":
                    verbose_clear()
                    for app in gstandard:
                        if app in installed_apps:
                            if args.verbose:
                                subprocess.run(["adb", "shell", "su", "-c", "pm", "uninstall", "--user", "0", app])
                            else:
                                print(f"\nUninstalling: {app}")
                                subprocess.run(["adb", "shell", "su", "-c", "pm", "uninstall", "--user", "0", app], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                verbose_clear()
                confirm = input("\nRemove The Important Google Apps? (Play Services and Play Store + apps that depend on them) (y/n) ")
                if confirm.lower() != "y":
                    verbose_clear()
                if confirm.lower() == "y":
                    verbose_clear()
                    for app in gFULL:
                        if app in installed_apps:
                            if args.verbose:
                                subprocess.run(["adb", "shell", "su", "-c", "pm", "uninstall", "--user", "0", app])
                            else:
                                print(f"\nUninstalling: {app}")
                                subprocess.run(["adb", "shell", "su", "-c", "pm", "uninstall", "--user", "0", app], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                verbose_clear()
            elif not "root" in root_result.stdout:
                input("\nRoot Not Detected! If You Are Rooted, Please Make Sure You Granted `shell` Root Permissions! ")
                sys.exit(0)

        if args.noroot:
            verbose_clear()
            for app in apps:
                if app in installed_apps:
                    if args.verbose:
                        subprocess.run(["adb", "shell", "pm", "disable-user", "--user", "0", app])
                    else:
                        print(f"\nDisabling: {app}")
                        subprocess.run(["adb", "shell", "pm", "disable-user", "--user", "0", app], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                else:
                    pass
            verbose_clear()
            confirm = input("\nRemove The Standard Google Apps? (Photos, Chrome, Google, Gmail, Maps, keeps Play Store and Play Services)  (y/n ")
            if confirm.lower() != "y":
                verbose_clear()
            elif confirm.lower() == "y":
                verbose_clear()
                for app in gstandard:
                    if app in installed_apps:
                        if args.verbose:
                            subprocess.run(["adb", "shell", "pm", "disable-user", "--user", "0", app])
                        else:
                            print(f"\nDisabling: {app}")
                            subprocess.run(["adb", "shell", "pm", "disable-user", "--user", "0", app], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
                    else:
                        pass
            verbose_clear()
            confirm = input("\nRemove The Important Google Apps? (Play Services and Play Store + apps that depend on them) (y/n) ")
            if confirm.lower() != "y":
                verbose_clear()
            elif confirm.lower() == "y":
                verbose_clear()
                for app in gFULL:
                    if app in installed_apps:
                        if args.verbose:
                            subprocess.run(["adb", "shell", "pm", "disable-user", "--user", "0", app])
                        else:
                            print(f"\nDisabling: {app}")
                            subprocess.run(["adb", "shell", "pm", "disable-user", "--user", "0", app], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
        folder = "APK-Holding"
        if os.path.isdir(folder):
            shutil.rmtree("./APK-Holding")
        else:
            pass
        dir = os.getcwd()
        print(f"\nYou Are In {dir}, Making An APK Folder And Moving Into It.")
        os.mkdir("APK-Holding")
        os.chdir("APK-Holding")
        cdir = os.getcwd()
        print(f"\nYou Are In {cdir}")
        time.sleep(2)
        verbose_clear()

        app_mapping = {
            "moe.rukamori.archivetune": "ArchiveTune",
            "org.localsend.localsend_app": "Localsend",
            "com.topjohnwu.magisk": "Maigsk",
            "com.vythera.vyxelapps": "VyxelApps",
            "org.adaway": "AdAway",
        }
     
        def applist():
            print("\nApplications Installed:")
            result = subprocess.run(["adb", "shell", "pm", "list", "packages"], capture_output=True, text=True)
            installed_apps_str = result.stdout
            for package, display_name in app_mapping.items():
                if package in installed_apps_str:
                    print(f"{display_name} -- {package}")
    
        applist()
        confirm = input("\nInstall Vyxel Apps? It Is An Open Source App Store That Has MANY Sources, Not Just F-Droid! (y/n) ")
        if confirm.lower() != "y":
            verbose_clear()
        else:
            verbose_clear()
            print("\nGrabbing Vyxel APK From Web!")
            url = "https://github.com/NikhilKain/vyxel-apps/releases/download/v1.0.6/Vyxel.Apps.v1.0.6.Foundation.apk"
            file = "Vyxel_Apps.apk"
            urllib.request.urlretrieve(url, file)
    
            print("\nInstalling Vyxel!")
            if args.verbose:
                subprocess.run(["adb", "install", "-r", "Vyxel_Apps.apk"])
            else:
                subprocess.run(["adb", "install", "-r", "Vyxel_Apps.apk"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            verbose_clear()

        subprocess.run(["adb", "devices"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
     
        applist()
        confirm = input("\nInstall ArchiveTune? [Youtube Music Client] (y/n) ")
        if confirm.lower() != "y":
            verbose_clear()
        else:
            verbose_clear()
            print("\nGrabbing ArchiveTune APK From Web!")
            url = "https://github.com/rukamori/ArchiveTune/releases/download/v13.7.0/app-gms-mobile-arm64-release.apk"
            file_name = "ArchiveTune.apk"
            urllib.request.urlretrieve(url, file_name)
    
            print("\nInstalling ArchiveTune!")
            if args.verbose:
                subprocess.run(["adb", "install", "-r", "ArchiveTune.apk"])
            else:
                subprocess.run(["adb", "install", "-r", "ArchiveTune.apk"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            verbose_clear()
    
        applist()
        confirm = input("\nInstall Localsend? [Basically Open Source Android AirDrop] (y/n) ")
        if confirm.lower() != "y":
            verbose_clear()
        else:
            verbose_clear
            print("\nGrabbing Localsend APK From Web!")
            url = "https://github.com/localsend/localsend/releases/download/v1.17.0/LocalSend-1.17.0-android-arm64v8.apk"
            file = "Localsend.apk"
            urllib.request.urlretrieve(url, file)
    
            print("\nInstalling Localsend!")
            if args.verbose:
                subprocess.run(["adb", "install", "-r", "Localsend.apk"])
            else:
                subprocess.run(["adb", "install", "-r", "Localsend.apk"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                verbose_clear()
    
        if root_result.stdout.strip() != "root":
            applist()
            confirm = input("\nInstall Magisk? (For Rooting, If You Don't Have OEM Unlocking, Don't Even Bother. (y/n) ")
            if confirm.lower() != "y":
                verbose_clear()
            else:
                verbose_clear()
                print("\nGrabbing Magisk APK From Web!")
                url = "https://github.com/topjohnwu/Magisk/releases/download/v30.7/Magisk-v30.7.apk"
                file = "Magisk.Apk"
                urllib.request.urlretrieve(url, file)
    
                print("\nInstalling Magisk!")
                if args.verbose:
                    subprocess.run(["adb", "install", "-r", "Magisk.apk"])
                else:
                    subprocess.run(["adb", "install", "-r", "Magisk.apk"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                verbose_clear()
        if "root" in root_result.stdout:
            applist()
            confirm = input("\nInstall AdAway? (An app you can use with root to disable ads at the system level while freeing up your private DNS settings. (y/n) ")
            if confirm.lower() != "y":
                verbose_clear()
            else:
                verbose_clear()
                print("\nGrabbing AdAway APK From Web!")
                url = "https://github.com/AdAway/AdAway/releases/download/v6.1.4/AdAway-6.1.4-20241027.apk"
                file = "AdAway.apk"
                urllib.request.urlretrieve(url, file)

                print("\nInstalling AdAway!")
                if args.verbose:
                    subprocess.run(["adb", "install", "-r", "AdAway.apk"])
                else:
                    subprocess.run(["adb", "install", "-r", "AdAway.apk"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                verbose_clear()
    
        os.chdir("../")
        shutil.rmtree("./APK-Holding")

    if args.flash:
        print("Rebooting Device Into Fastboot!")
        time.sleep(1)
        subprocess.run(["adb", "reboot", "bootloader"])
        if args.verbose:
            subprocess.run(["fastboot", "reboot", "bootloader"], timeout=1)
        else:
            subprocess.run(["fastboot", "reboot", "bootloader"], timeout=1, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        fastboot_devices = subprocess.run(["fastboot", "devices"], timeout=3, capture_output=True, text=True, check=True)
        if "fastboot" in fastboot_devices.stdout:
            print("Fastboot Active!")
            if args.verbose:
                subprocess.run(["fastboot", "--set-active=a"])
            else:
                subprocess.run(["fastboot", "--set-active=a"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
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
                    "system",
                    "product",
                    "vendor",
                    "vendor_dlkm",
                    "system_ext",
                    "system_dlkm",
                    "odm",
                ]
                for part in images:
                    file_path = Path(f"{part}.img")

                    if args.verbose:
                        if file_path.is_file():
                            subprocess.run(["fastboot", "flash", part, file_path])

                        else:
                            pass
                    else:
                        if file_path.is_file():
                            print(f"\nFlashing {part}.img")
                            subprocess.run(["fastboot", "flash", part, file_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                        else:
                            pass
                time.sleep(2)
                verbose_clear()
            
            if args.logical:
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
                ]
            for part in images:
                file_path = Path(f"{part}.img")
                if args.verbose:
                    if file_path.is_file():
                        subprocess.run(["fastboot", "flash", part, file_path])
                    else:
                        pass
                else:
                    if file_path.is_file():
                        print("\nFlashing {part}.img")
                        subprocess.run(["fastboot", "flash", part, file_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    else:
                        pass
                time.sleep(2)
                
    if not args.debloat and not args.flash:
        parser.print_help()

if __name__ == "__main__":
    main()
 
