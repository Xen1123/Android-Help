#!/bin/bash
echo "Please Make Sure Your Desired Images Are In The Directory That You're Operating In! Click Any Key To Continue!"
read -r -n 1 -s

mv bootloader* bootloader.img >/dev/null 2>&1 || true
mv radio* radio.img >/dev/null 2>&1 || true

adb reboot bootloader >/dev/null 2>&1 || true
timeout 2s fastboot reboot bootloader >/dev/null 2>&1 || true

PS3='Just Android Images Or The Full Firmware Flash?
'
options=("Android" "Full Factory")
select opt in "${options[@]}"
do
    case $opt in
        "Android")
            images=(
                boot
                dtbo
                vendor_boot
                vbmeta_system
                vbmeta
                vbmeta_vendor
            )

            for img in "${images[@]}"; do
                echo "Flashing $img"
                timeout 2s fastboot flash "$img" "$img.img" >/dev/null 2>&1 || echo "Failed To Flash $img"
            done
            fastboot reboot fastboot
            
            logical=(
                system
                system_ext
                system_other
                vendor
                vendor_dlkm
                gsa
                product
            )

            for logic in "${logical[@]}"; do
                echo "Flashing $logic"
                timeout 2s fastboot flash "$logic" "$logic.img" >/dev/null 2>&1 || echo "Failed To Flash $logic"
            done
            break
            ;;
        "Full Factory")
            fastboot flash bootloader bootloader.img >/dev/null 2>&1 || { clear; echo "Bootloader image not found, cannot continue!"; exit 1; }
            timeout 2s fastboot reboot-bootloader >/dev/null 2>&1 || { clear; echo "Failed To Reboot To Bootloader. Not Vital, But Still Not Great!"; }
            fastboot flash radio radio.img >/dev/null 2>&1 || { clear; echo "Radio image not found, cannot continue!"; exit 1; }
            timeout 2s fastboot reboot-bootloader >/dev/null 2>&1 || { clear; echo "Failed To Reboot To Bootloader. Not Vital, But Still Not Great!"; }
            sleep 6
            images=(
                dtbo
                boot
                vendor_boot
                vbmeta_system
                vbmeta
                vbmeta_vendor
                abl
                bl1
                bl2
                bl31
                ldfw
                modem
                pbl
                pvmfw
                tzsw
            )

            for img in "${images[@]}"; do
                echo "Flashing $img"
                timeout 2s fastboot flash "$img" "$img.img" >/dev/null 2>&1 || echo "Failed To Flash $img"
            done
            fastboot reboot fastboot

            logical=(
                system
                product
                system_ext
                system_other
                vendor
                vendor_dlkm
            )

            for logic in "${logical[@]}"; do
                echo "Flashing $logic"
                timeout 2s fastboot flash "$logic" "$logic.img" >/dev/null 2>&1 || echo "Failed To Flash $logic"
            done
            break
            ;;
        *)
            echo "Invalid Option: $REPLY"
            ;;
        esac
    done
