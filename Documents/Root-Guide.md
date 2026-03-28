## How To Root Any Android Phone
- Download Magisk APK At [Magisk Releases](https://github.com/topjohnwu/Magisk/releases)
- Find The Stock Firmware For Your Device And Pull boot.img Or init_boot.img
- Install The Magisk App
- Patch Your .img File
- Bring The Patched File To Your Flashing Device (PC or Other Android With ADB & Fastboot)
- 'adb reboot fastboot'
- fastboot flash boot/init_boot magisk_patched*.img 'fastboot flash boot magisk_patched*.img' or 'fastboot flash init_boot magisk_patched*.img'

## If You Can NOT Find Your Stock Firmware
- Again, Download The Magisk APK At [Magisk Releases](https://github.com/topjohnwu/Magisk/releases)
- On Your Computer or Android Device With With ADB & Fastboot, Rename The 'Magisk*.apk' To 'Magisk.zip'
- Go Find A Custom Recovery For Your Device, Like TWRP, OrangeFox, or A Custom ROM Recovery
- Flash The Recovery, Typically With 'fastboot flash recovery recovery.img' or 'fastboot flash vendor_boot recovery.img'
- Reboot Into The Custom Recovery
- Find 'Apply Update Via ADB', On Custom ROM Recoveries, It Is A Button Right In Front Of You, In TWRP, Click 'Advanced', Then 'ADB Sideload', When You're In Either Of These, Type 'adb sideload magisk*.zip'
- For Above, If In OrangeFox, Click The Menu Button, Select Toolbox, Select 'ADB Sideload', And Then Confirm.

# Linux Guide (Copy & Paste Into Terminal)
- Please make sure you have wget, adb+fastboot, and the mtp tool so you can transfer files from the phone, the package name varies between distros (gvfs-mtp
, mtp-tools, etc.)
```
wget https://github.com/topjohnwu/Magisk/releases/download/v30.7/Magisk-v30.7.apk
```
```
adb install ~/Downloads/Magisk-v30.7.apk
```
```
adb push /path/to/init_boot.img /sdcard/Download
```
**Go Into Magisk And Patch The File, Then Continue**
```
adb shell "ls /sdcard/Download/magisk_patched*.img" | xargs -I {} adb pull "{}" ~/Downloads
```
```
adb reboot fastboot
```
```
mv magisk_patched* root_init_boot.img
```
```
fastboot flash init_boot root_init_boot.img && fastboot reboot
```
