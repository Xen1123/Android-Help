@echo off
title Android Factory Firmware Flasher
echo This Script Flashes Your Device Factory Firmware Via Fastboot.
pause
echo Please Make Sure Your Images Are In Their Standard Form, For Example, Rename "bootloader-bluejay-39-1ls.img" to "bootloader.img" and make sure all of your images are in the directory that you're running the script in.
pause
adb reboot fastboot
fastboot reboot fastboot
set "img=boot xbl abl aop aop_config Bluetooth cpucp cpucp_dtb devcfg modem init_boot recovery vendor_boot vbmeta vbmeta_system vbmeta_vendor xbl_ramdump xbl_config dsp dtbo keymaster imagefv tz shrm pvmfw odm hyp uefi uefisecapp qupfw bootloader radio bl1 bl2 bl31 gsa ldfw pbl tzsw"
for %%i in (%img%) do (
	fastboot flash %%i %%i.img
)
cls
echo Press 1 To Reboot
echo Press 2 To Exit The Script
set /p command=
if "%command%" == "1" goto reboot
if "%command%" == "2" goto exit
:reboot
fastboot reboot
exit
:exit
exit
