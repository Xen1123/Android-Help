#!/bin/bash
echo "This Script Fully Flashes Your Nothing Phone Firmware And Re-Locks The Device To Restore It To A Stock State! Press Any Key To Continue."
read -r -n 1 -s

if ! command -v adb >/dev/null 2>&1 && command -v fastboot >/dev/null 2>&1; then
    if command -v nala >/dev/null 2>&1; then
        sudo nala install adb fastboot -y
    elif command -v apt >/dev/null 2>&1; then
        sudo apt install adb fastboot -y
    fi

    if command -v dnf >/dev/null 2>&1; then
        sudo dnf install android-tools -y
    elif command -v pacman >/dev/null 2>&1; then
        sudo pacman -S android-tools --noconfirm
    fi
fi

adb reboot bootloader
timeout 2s fastboot reboot bootloader

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
    pvmfw
    qupfw
    shrm
    tz
    uefi
    uefisecapp
    vbmeta
    vbmeta_system
    vbmeta_vendor
    vendor_boot
    xbl
    xbl_config
    xbl_ramdump
)

for img in "${images[@]}"; do
    echo "Flashing $img"
    fastboot flash --slot-all "$img" "$img.img" >/dev/null 2>&1 || { echo "You Don't Have $img.img"; exit 1; }
done

fastboot flash recovery recovery.img
fastboot reboot fastboot

logical=(
    product
    system
    system_dlkm
    system_ext
    vendor
    vendor_dlkm
)

for log in "${logical[@]}"; do
    echo "Flashing $log"
    fastboot flash --slot-all "$log" "$log.img" >/dev/null 2>&1 || { echo "You Don't Have $log.img"; exit 1; }
done

fastboot reboot bootloader
echo "*--------------------------------*"
echo "*  Your Device Bootloader Needs  *"
echo "*     To Be Locked To Finish!    *"
echo "*--------------------------------*"

read -p "Type 'LOCK' to confirm: " confirm
if [ "$confirm" == "LOCK" ]; then
    fastboot flashing lock
else
    echo "Locking cancelled. Please reboot and check your device."
fi
