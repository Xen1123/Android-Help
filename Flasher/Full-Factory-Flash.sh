#!/bin/bash
echo "This script flashes every single factory image file in your Android phone via Fastboot, depending on your phone, you may have to run
'fastboot flashing unlock_critical' first."
sleep 12
cp bootloader* ./bootloader.img || true
cp radio* ./radio.img || true
img=(
boot
xbl
abl
aop
aop_config
bluetooth
cpucp
cpucp_dtb
devcfg
modem
init_boot
recovery
vendor_boot
vbmeta
vbmeta_system
vbmeta_vendor
xbl_ramdump
xbl_config
dsp
dtbo
keymaster
imagefv
tz
shrm
pvmfw
odm
hyp
uefi
uefisecapp
qupfw
bootloader
radio
bl1
bl2
bl31
gsa
ldfw
pbl
tzsw
)
for image in "${img[@]}"; do
fastboot flash "$image" "$image.img"
done
fastboot reboot fastboot
android=(
system
product
vendor
vendor_dlkm
system_dlkm
system_ext
system_other
)
for image in "${android[@]}"; do
fastboot flash "$image" "$image.img"
done
