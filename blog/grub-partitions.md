title: GRUB and partitioning
author: David Houseman
date: 2021-11-30

This is a minimal `grub.cfg` config file for the GRUB bootloader
for a PC with two installed operating systems, `rescue` and `root`.
GRUB only needs to be installed in one OS (probably `rescue`).
Remember to run `grub-install` after making changes to `grub.cfg`.

    set default=1
    set timeout=5

    menuentry "rescue" {
        insmod all_video
        search --set --label rescue
        linux /vmlinuz root=LABEL=rescue
        initrd /initrd.img 
    }	      

    menuentry "root" {
        insmod all_video
        search --set --label root
        linux /vmlinuz root=LABEL=root
        initrd /initrd.img 
    }

Use `e2label` to add labels to the root partitions and `lsblk -f` to
confirm that the labels are present.

For partitioning, modern systems require a small (256MB) vfat-formatted
EFI partition. A boot partition is not required on modern systems.
I recommend one partition per installed operating system, a swap partition,
and a home partition. The separate home partition helps when upgrading
the operating system.
