#!/bin/bash -xe

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
BOOTDISK=./bootdisk
ROOTFS=./rootfs

cd ${DIR}
mkdir -p ${BOOTDISK}
apt clean

systemctl stop pve-cluster.service

rsync -av --one-file-system --delete --exclude=/proc/* --exclude=/dev/* \
--exclude=/sys/* --exclude=/tmp/* --exclude=/lost+found --exclude=/var/tmp/* \
--exclude=/boot/grub/* --exclude=/var/mail/* --exclude=/media/* \
--exclude=/etc/fstab --exclude=/etc/mtab --exclude=/etc/hosts \
--exclude=/var/log/pve/tasks/* \
--exclude=${DIR} / ${ROOTFS}

systemctl start pve-cluster.service

find ${ROOTFS}/var/log -type f | while read file
do
        cat /dev/null | tee $file
done

mount --bind /dev/ ${ROOTFS}/dev
mount -t proc proc ${ROOTFS}/proc
mount -t sysfs sysfs ${ROOTFS}/sys
mount --bind /run ${ROOTFS}/run

cat << EOF | chroot ${ROOTFS}
LANG=
depmod -a $(uname -r)
update-initramfs -u -k $(uname -r)
apt clean
EOF

umount ${ROOTFS}/run
umount ${ROOTFS}/sys
umount ${ROOTFS}/proc
umount ${ROOTFS}/dev

