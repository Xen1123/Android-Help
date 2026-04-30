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
                fastboot flash "$img" "$img.img" >/dev/null 2>&1 || echo "Failed To Flash $img"
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
                fastboot flash "$logic" "$logic.img" >/dev/null 2>&1 || echo "Failed To Flash $logic"
            done
            break
            ;;
        "Full Factory")
            images=(
                bootloader
                radio
                boot
                dtbo
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
                fastboot flash "$img" "$img.img" >/dev/null 2>&1 || echo "Failed To Flash $img"
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
                fastboot flash "$logic" "$logic.img" >/dev/null 2>&1 || echo "Failed To Flash $logic"
            done
            break
            ;;
        *)
            echo "Invalid Option: $REPLY"
            ;;
        esac
    done
