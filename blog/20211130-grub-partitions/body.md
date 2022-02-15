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

For partitioning, modern systems use a GPT partition table and
require a small (256MB) vfat-formatted EFI partition. A boot
partition is not required. I recommend one partition per installed
operating system, a swap partition, and a home partition. The separate
home partition is common to both operating systems and is preserved
when upgrading either operating system.

    # fdisk -l
    Device             Start       End   Sectors  Size Type
    /dev/nvme0n1p1      2048    262143    260096  127M EFI System
    /dev/nvme0n1p2    262144   4194303   3932160  1.9G Linux filesystem
    /dev/nvme0n1p3   4194304  16777215  12582912    6G Linux swap
    /dev/nvme0n1p4  16777216  50331647  33554432   16G Linux filesystem
    /dev/nvme0n1p5  50331648  83886079  33554432   16G Linux filesystem
    /dev/nvme0n1p8 201326592 369098751 167772160   80G Linux filesystem

Here on `p2` I have installed a small, console-only rescue operating system,
with swap space on `p3` and two operating systems on `p4` and `p5`. The
home partition is on `p8`.