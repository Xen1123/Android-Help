import argparse
import os
import shutil
import subprocess
import sys
import time
import urllib.request

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
    "com.google.android.apps.pixel.nowplaying",
]


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


clear()

print(r"""

██████╗ ███████╗██████╗ ██╗      ██████╗  █████╗ ████████╗
██╔══██╗██╔════╝██╔══██╗██║     ██╔═══██╗██╔══██╗╚══██╔══╝
██║  ██║█████╗  ██████╔╝██║     ██║   ██║███████║   ██║
██║  ██║██╔══╝  ██╔══██╗██║     ██║   ██║██╔══██║   ██║
██████╔╝███████╗██████╔╝███████╗╚██████╔╝██║  ██║   ██║
╚═════╝ ╚══════╝╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝

""")


def main():

    parser = argparse.ArgumentParser(
        description="Multi-Device ADB Debloater - Root Or No Root",
        epilog="Example: python Debloat.py --root --verbose",
    )
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument(
        "--noroot",
        action="store_true",
        help="Disable apps - DOESN'T remove them from the device storage, can be re-enabled in settings",
    )
    group.add_argument(
        "--root",
        action="store_true",
        help="Removes apps from your system completely - Apps that are removed will need to be reinstalled.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Makes script show EVERYTHING, including errors - Without '--verbose', errors and other outputs will be silent.",
    )

    args = parser.parse_args()

    if not args.root and not args.noroot:
        parser.print_help()
        input("\nClick Any Key To Exit . . .")
        sys.exit()
    try:
        result = subprocess.run(
            ["adb", "devices"], capture_output=True, text=True, check=True
        )

        if "unauthorized" in result.stdout:
            print("\nDevice Not Authorized")
            sys.exit(1)

        if "device" not in result.stdout.split():
            print("\nNo Device!")
            sys.exit(1)
    except subprocess.CalledProcessError:
        print("Failed To Run ADB! Is It In Your PATH?")
        sys.exit(1)

    root_check = subprocess.run(
        ["adb", "shell", "su -c whoami"], capture_output=True, text=True
    )

    if args.noroot:
        adb_path = shutil.which("adb")

        if not adb_path:
            print("\nYou do not have ADB installed or in your system PATH!")
            sys.exit(0)
        else:
            print(f"\nADB Found At: {adb_path}")
            time.sleep(2)
        if args.verbose:
            for app in apps:
                subprocess.run(
                    ["adb", "shell", "pm", "disable-user", "--user", "0", app]
                )
        else:
            for app in apps:
                print(f"\nDISABLING: {app}")
                subprocess.run(
                    ["adb", "shell", "pm", "disable-user", "--user", "0", app],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )

    if args.root:
        adb_path = shutil.which("adb")

        if not adb_path:
            print("\nYou do not have ADB installed or in your system PATH!")
            sys.exit(0)
        else:
            print(f"\nADB Found At: {adb_path}")
            time.sleep(2)
        if args.verbose:
            pass
        else:
            clear()
        if root_check.stdout.strip() != "root":
            if args.verbose:
                pass
            else:
                clear()
            print("\nRoot Not Detected!")
            input("\nClick Any Key To Exit . . .")
            sys.exit()
        for app in apps:
            if args.verbose:
                pm_uninstall = f"pm uninstall --user 0 {app}"
                subprocess.run(["adb", "shell", "su", "-c", pm_uninstall])
            else:
                pm_uninstall = f"pm uninstall --user 0 {app}"
                print(f"\nUNINSTALLING: {app}")
                subprocess.run(
                    ["adb", "shell", "su", "-c", pm_uninstall],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )

    if args.verbose:
        pass
    else:
        clear()

    # APK Folder Creation
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

    confirm = input(
        "\nInstall Vyxel Apps? It Is An Open Source App Store That Has MANY Sources, Not Just F-Droid! (y/n) "
    )
    if confirm.lower() != "y":
        if args.verbose:
            pass
        else:
            clear()
    else:
        if args.verbose:
            pass
        else:
            clear()
        print("\nGrabbing Vyxel APK From Web!")
        url = "https://github.com/NikhilKain/vyxel-apps/releases/download/v1.0.5/Vyxel.Apps.v1.0.5.Foundation.apk"
        file = "Vyxel_Apps.apk"
        urllib.request.urlretrieve(url, file)

        print("\nInstalling Vyxel!")
        if args.verbose:
            subprocess.run(["adb", "install", "-r", "Vyxel_Apps.apk"])
        else:
            subprocess.run(
                ["adb", "install", "-r", "Vyxel_Apps.apk"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        if args.verbose:
            pass
        else:
            clear()

    subprocess.run(
        ["adb", "devices"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )

    confirm = input("\nInstall ArchiveTune? [Youtube Music Client] (y/n) ")
    if confirm.lower() != "y":
        if args.verbose:
            pass
        else:
            clear()
    else:
        if args.verbose:
            pass
        else:
            clear()
        print("\nGrabbing ArchiveTune APK From Web!")
        url = "https://github.com/ArchiveTuneApp/ArchiveTune/releases/download/v13.6.0/app-mobile-arm64-release.apk"
        file_name = "ArchiveTune.apk"
        urllib.request.urlretrieve(url, file_name)

        print("\nInstalling ArchiveTune!")
        if args.verbose:
            subprocess.run(["adb", "install", "-r", "ArchiveTune.apk"])
        else:
            subprocess.run(
                ["adb", "install", "-r", "ArchiveTune.apk"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        if args.verbose:
            pass
        else:
            if args.verbose:
                pass
            else:
                clear()

    confirm = input(
        "\nInstall Localsend? [Basically Open Source Android AirDrop] (y/n) "
    )
    if confirm.lower() != "y":
        if args.verbose:
            pass
        else:
            clear()
    else:
        if args.verbose:
            pass
        else:
            clear()
        print("\nGrabbing Localsend APK From Web!")
        url = "https://github.com/localsend/localsend/releases/download/v1.17.0/LocalSend-1.17.0-android-arm64v8.apk"
        file = "Localsend.apk"
        urllib.request.urlretrieve(url, file)

        print("\nInstalling Localsend!")
        if args.verbose:
            subprocess.run(["adb", "install", "-r", "Localsend.apk"])
        else:
            subprocess.run(
                ["adb", "install", "-r", "Localsend.apk"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            if args.verbose:
                pass
            else:
                clear()

    if root_check.stdout.strip() != "root":
        confirm = input(
            "\nInstall Magisk? (For Rooting, If You Don't Have OEM Unlocking, Don't Even Bother. (y/n) "
        )
        if confirm.lower() != "y":
            if args.verbose:
                pass
            else:
                clear()
        else:
            if args.verbose:
                pass
            else:
                clear()
            print("\nGrabbing Magisk APK From Web!")
            url = "https://github.com/topjohnwu/Magisk/releases/download/v30.7/Magisk-v30.7.apk"
            file = "Magisk.Apk"
            urllib.request.urlretrieve(url, file)

            print("\nInstalling Magisk!")
            if args.verbose:
                subprocess.run(["adb", "install", "-r", "Magisk.apk"])
            else:
                subprocess.run(
                    ["adb", "install", "-r", "Magisk.apk"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
            if args.verbose:
                pass
            else:
                clear()

        os.chdir("../")
        shutil.rmtree("./APK-Holding")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
