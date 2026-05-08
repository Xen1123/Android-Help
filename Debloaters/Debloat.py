from pathlib import Path
import shutil
import subprocess
import time
import sys
import platform
print("This Script Will Debloat Your Android Device!")
input("Press Enter To Continue...")
adb_path = shutil.which("adb")
if not adb_path:
    print("Error: ADB Not Found. Please Make Sure It Is Installed And In Your PATH.")
    sys.exit()
else:
    print(f"ADB found at: {adb_path}")
    apps = [
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
        "com.google.android.apps.wellbeing",
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
        "com.google.android.apps.safetyhub",
        "com.google.android.projection.gearhead",
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
    subprocess.run([
        print(f"Removing {app}")
        "adb", "shell", "pm", "disable-user", "--user", "0", app
    ])

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
        print("\nPlease Select Your Choice:")
        for i, opt in enumerate(options, 1):
            print(f"{i}) {opt}")

        choice = input("\nEnter Choice Number: ")

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