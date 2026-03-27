# How To Root Any Android Phone
- Download Magisk APK At https://github.com/topjohnwu/Magisk/releases/tag/v30.7
- Find The Stock Firmware For Your Device And Pull boot.img Or init_boot.img
- Install The Magisk App
- Patch Your .img File
- Bring The Patched File To Your Flashing Device (PC or Other Android With adb & fastboot)
- 'adb reboot fastboot'
- fastboot flash boot/init_boot magisk_patched*.img 'fastboot flash boot magisk_patched*.img' or 'fastboot flash init_boot magisk_patched*.img'
