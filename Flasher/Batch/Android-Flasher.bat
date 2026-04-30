@echo off
Title Android Flasher
echo This Script Flashes All of Your Android Images Via Fastboot, Leaving Out Bootloader Components To Prevent A Hard Brick.
pause
adb reboot bootloader
fastboot reboot bootloader
set "img=recovery dtbo vendor_boot boot vbmeta vbmeta_vendor vbmeta_system"
for %%i in (%img%) do (
	fastboot flash %%i %%i.img
)
cls
fastboot reboot fastboot
set "img=system system_ext system_dlkm odm vendor product vendor_dlkm"
for %%i in (%img%) do (
	fastboot flash %%i %%i.img
)
cls
echo Press 1 To Reboot
echo Press 1 To Exit Script
set /p command=
if "%command%" == "1" goto reboot
if "%command%" == "2" goto exit
:reboot
fastboot reboot
exit
:exit
exit
