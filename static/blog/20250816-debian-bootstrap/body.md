Steps to bootstrap a minimal debian 13 'Trixie' install onto a spare partition.

1. Allocate the partition using `fdisk`.
2. Make the filesystem.

    ```
    mkfs.ext4 ${partition}
    e2fsck ${partition}
    e2label ${partition} debian_13
    ```

3. Check the debian mirror in `/etc/apt/sources.list.d/debian.sources`.
4. Mount the partition

    ```
    mount ${partition} /mnt
    ```

5. Choose the desired debian distribution.

    ```
    10 - buster
    11 - bullseye
    12 - bookworm
    13 - trixie
    14 - forky
    15 - duke
    ```

6. Bootstrap install base packages into the new partition.

    ```
    debootstrap --variant=minbase ${dist} ${chroot} ${mirror}
    ```

7. Copy apt sources.

    ```
    cp --parents /etc/apt/sources.list.d/debian.sources /mnt
    ```

8. Copy network configuration.

    ```
    cp --parents /etc/network/interfaces /mnt
    cp --parents /etc/hosts /mnt
    ```

9. Copy filesystem table. This is needed, because an empty fstab causes /
to be mounted read-only.

    ```
    cp --parents /etc/fstab /mnt
    ```

10. System dirs are needed by some packages.

    ```
    mount --bind /dev /mnt/dev
    mount --bind /proc /mnt/proc
    mount --bind /sys /mnt/sys
    ```

11. `chroot` into the new partition and update apt.

    ```
    chroot /mnt
    apt-get update
    apt-get upgrade
    ```

12. Install system packages.

    ```
    apt-get install busybox linux-image-amd64 systemd-sysv pciutils usbutils grub-efi
    apt-get install bc bsdmainutils debootstrap file gnupg make less nano time
    apt-get install dosfstools ifupdown isc-dhcp-client iputils-ping netbase
    apt-get install openssh-client openssh-server
    apt-get install git man-db manpages rsync
    ```

    `wireless-tools` is required for wifi. 

13. Set hostname.

    ```
    echo ${host} > /etc/hostname
    ```

14. Set password.

    ```
    passwd
    ```

15. Exit the chroot.

    ```
    exit
    ```

16. Edit `/boot/grub/grub.cfg` to contain, at a minimum:

    ```
    set default=0
    set timeout=5

    menuentry "debian 13" {
        insmod all_video
        search --label --set debian_13
        linux /vmlinuz root=LABEL=debian_13
        initrd /initrd.img
    }
    ```

17. Reinstall grub.

    ```
    mount -L efi /boot/efi
    grub-install --target=x86_64-efi ${device}
    ```

That should, in theory, be enough to reboot into the new installation.

18. Window manager.

    ```
    apt-get install xorg xterm xfce4
    ```

19. Applications.

    ```
    apt-get install firefox-esr texlive
    ```

20. Web development

    ```
    apt-get install pandoc python3-flask python3-git python3-pytz python3-slugify
    ```
 
