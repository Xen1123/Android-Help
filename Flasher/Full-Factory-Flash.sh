#!/bin/bash
echo "This script flashes every single factory image file in your Android phone via Fastboot, depending on your phone, you may have to run
'fastboot flashing unlock_critical' first. This script only works with fastboot devices, so special phones like Samsungs won't flash. Press any key to continue."
read -n 1 -s
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

clear

PS3="Would You Like To Disable Verification So The Device Will Boot Modified Android Versions? (May Prevent Booting Android/Recovery Mode On Some Phones, But Works On Most)."
options=("Yes" "No")
select opt in "${options[@]}"
do
  case $opt in
    "Yes")
      fastboot --disable-verity --disable-verification flash vbmeta vbmeta.img
      fastboot --disable-verity --disable-verification flash vbmeta_vendor vbmeta_vendor.img || echo "vbmeta_vendor not found, skipping..."
      fastboot --disable-verity --disable-verification flash vbmeta_system vbmeta_system.img || echo "vbmeta_system not found, skipping..."
      fastboot -w
      break
    ;;
    "No")
      break
    ;;
    *)
      echo "Invalid Option: $REPLY"
    ;;
    esac
  done

PS3="What Now?"
options=("Reboot To System" "Reboot To Recovery" "Reboot To Bootloader" "Exit Script For Extended Flashing")
select opt in "${options[@]}"
do
  case $opt in
    "Reboot To System")
      fastboot reboot
      exit
    ;;
    "Reboot To Recovery")
      fastboot reboot recovery
      exit
    ;;
    "Reboot To Bootloader")
      fastboot reboot bootloader
      exit
    ;;
    "Exit Script For Extended Flashing")
      exit
    ;;
    *)
      echo "Invalid Option: $REPLY"
    ;;
  esac
done
