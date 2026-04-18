#!/bin/bash
if ! command -v adb >/dev/null 2>&1 && ! command -v fastboot >/dev/null 2>&1; then
    echo "ADB & Fastboot Are Not Available, Installing Them Now!"
        if command -v pacman >/dev/null 2>&1; then
            sudo pacman -S android-tools --noconfirm
            clear
        elif command -v apt >/dev/null 2>&1; then
            if command -v nala >/dev/null 2>&1; then
                sudo nala install adb fastboot -y
            else
                sudo apt install adb fastboot -y
            fi
            clear
        elif command -v dnf >/dev/null 2>&1; then
            sudo dnf install android-tools -y
            clear
        fi
fi

echo "Please Make Sure You Have Your Images In The Same Folder You're Running The Script From! (Press Any Key To Continue)"
read -r -n 1 -s
adb reboot fastboot >/dev/null 2>&1
timeout 2s fastboot reboot fastboot >/dev/null 2>&1
clear
until fastboot devices | grep -q "fastboot"; do
    echo "Waiting for device in fastbootd..."
    sleep 2
done
PS3="Did You Unlock The Critical Partitions For Your Bootloader?
"
options=("Yes" "No")
select opt in "${options[@]}"
do
case $opt in
    "Yes")
        fastboot set_active a
        images=(
            abl
            aop
            aop_config
            bluetooth
            boot
            cpucp
            cpucp_dtb
            devcfg
            dsp
            dtbo
            featenabler
            hyp
            imagefv
            init_boot
            keymaster
            modem
            multiimgoem
            odm
            product
            pvmfw
            qupfw
            recovery
            shrm
            system
            system_dlkm
            system_ext
            tz
            uefi
            uefisecapp
            vbmeta
            vbmeta_system
            vbmeta_vendor
            vendor
            vendor_boot
            vendor_dlkm
            xbl
            xbl_config
            xbl_ramdump
            )

        for img in "${images[@]}"; do
            if [[ -f "$img.img" ]]; then
                fastboot flash "$img" "$img.img"
            else
                echo "Skipping $img: Image File Not Found."
            fi
        done
        fastboot reboot
        exit
        ;;
    "No")
        adb reboot bootloader
        timeout 2s fastboot reboot bootloader
        fastboot flashing unlock_critical || exit
        echo "Your Phone Is Now Ready For This Script! Re-Run The Script To Continue!"
        ;;
    esac
done
