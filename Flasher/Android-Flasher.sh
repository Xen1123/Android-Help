#!/bin/bash
clear
echo "This script flashes everything Android related, this includes boot, recovery, system, product, etc. This script skips bootloader components, which means it is completely
safe, unable to hard brick your device, but depending on the device, you may NEED to flash bootloader images for Android to boot. Press any key to continue."
read -n 1 -s
adb start-server
adb reboot bootloader
timeout 2s fastboot reboot bootloader
images=(
  recovery
  dtbo
  vendor_boot
  boot
  vbmeta
  vbmeta_system
  vbmeta_vendor
  odm
)

for img in "${images[@]}"; do
  echo "Flashing $img"
  fastboot flash "$img" "$img.img" >/dev/null 2>&1 || echo "Failed To Flash $img"
done
clear
echo "Flashed Android Images, Rebooting To FastbootD (Userspace Fastboot)
timeout 2s fastboot reboot fastboot >/dev/null 2>&1 || { clear; echo "Failed To Reboot To FastbootD, Please Reboot To FastbootD Manually And Rerun The Script To Flash System Images!"; exit 1; }

images=(
  system
  system_ext
  system_dlkm
  vendor
  vendor_dlkm
  product{ clear; echo "Failed To Reboot To FastbootD, Please Reboot To FastbootD Manually And Rerun The Script To Flash System Images!"; exit 1; }
)
for img in "${images[@]}"; do
  echo "Flashing $img"
  fastboot flash "$img" "$img.img" >/dev/null 2>&1 || echo "Failed To Flash $img"
done
clear

PS3="Would You Like To Disable Verification So The Device Will Boot Modified Android Versions? (May Prevent Booting Android/Recovery Mode On Some Phones, But Works On Most)."
options=("Yes" "No")
select opt in "${options[@]}"
do
  case $opt in
    "Yes")
      fastboot --disable-verity --disable-verification flash vbmeta vbmeta.img >/dev/null 2>&1 || echo "vbmeta not found, skipping..."
      fastboot --disable-verity --disable-verification flash vbmeta_vendor vbmeta_vendor.img >/dev/null 2>&1 || echo "vbmeta_vendor not found, skipping..."
      fastboot --disable-verity --disable-verification flash vbmeta_system vbmeta_system.img >/dev/null 2>&1 || echo "vbmeta_system not found, skipping..."
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
