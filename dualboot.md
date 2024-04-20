1. Mount windows efi partition. You can find the name of it with:

```sh
sudo fdisk -l

Disk /dev/nvme0n1: 953.87 GiB, 1024209543168 bytes, 2000409264 sectors
Disk model: HFM001TD3JX013N
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 1E84BC84-5B22-4A76-AF82-D788FDE027AB

Device              Start        End    Sectors   Size Type
/dev/nvme0n1p1       2048     206847     204800   100M EFI System
/dev/nvme0n1p2     206848     239615      32768    16M Microsoft reserved
/dev/nvme0n1p3     239616 1684473855 1684234240 803.1G Microsoft basic data
/dev/nvme0n1p4 1999046656 2000406527    1359872   664M Windows recovery enviro
/dev/nvme0n1p5 1684473856 1685497855    1024000   500M EFI System
/dev/nvme0n1p6 1685497856 1999046655  313548800 149.5G Linux filesystem

Partition table entries are not in disk order.
```

**_/den/nvme0n1p1_** is windows efi partition.

I mounted it in /mnt/boot to make it distinguishable from the arch boot directory.

2. Add windows boot partition to fstab file in /etc/fstab
   it should be something like this.
   You can find UUID with `blkid`

```
UUID=5218-B6DB /mnt/boot vfat rw,relatime,fmask=0022,dmask=0022,codepage=437,iocharset=ascii,shortname=mixed,utf8,errors=remount-ro 0 2
```

3. Install sbctl and os-prober.

4. Go to bios and go to secure boot and turn on user mode or something like it in secure boot.

5. Run these commands.

```sh
sbctl create-keys
sbctl enroll-keys --microsoft
# Run 'sbctl verify' and add all efi files which sbctl says.
# you can add them like this:
sbctl sign -s /boot/EFI/Linux/linux.efi
# Check if all files are signed.
sbctl list-files
# pacman -S linux <-- I'm not sure this is neccesery or not.
```

6. Configure grub for dualboot.

```sh
nvim /etc/default/grub
```

Uncomment this line:
`GRUB_DISABLE_OS_PROBER=false`

Run `os-prober` command.

And rerun `grub-mkconfig` command

7. When you reboot and boot to windows boot partition for first time you need to enter bitlocker
   keys for the first time you can find it from ***https://account.microsoft.com/devices/recoverykey***
