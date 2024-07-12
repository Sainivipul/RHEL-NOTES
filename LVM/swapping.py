#SWAP SPACE__

Swap space in Linux and other Unix-like operating systems is a designated area on the storage device (typically a hard disk or SSD) that is used as virtual memory,
 when the physical RAM (Random Access Memory) is fully utilized. Swap space can be configured as a dedicated swap partition or a swap file.

#PAGES__

LINUX manage memory or ram in very effective way it distribute the ram in small chunks knownn as pages , when ever these pages start completely occupying linux,
copy these chunks into harddisk 
they can be filled because of booting process files or some process files which will not be required agter the completion of process 
the space where all these files get stored is known as swap page 

#SWAPPIG 

process of storing these chunnks into swap space is known as swapping and it depends on perameter swapinness perameter(0-100)
more is the value more aggresivl it works 

# STRESS

Linux utility to check system by providing LOAD ( CPU,RAM,I/O,DISK)

# GET STRESS PAKAGE IN OUR SYSTEM 
dnf/yum install -y epel-release 

dnf repolist all --check

dnf install -y stress 

# load on cpu 

stress --cpu 4(no of cpu load ) --timeout 20 

uptime --> check load 

#RAM/memory load

stress -m 1 --vm-bytes 4G 

free --> check 

#check swzappiness value 

cat /proc/sys/vm/swzappiness
#if we will increase value swap partitionn will will aggresivly 

echo X(value(0-100)) > /proc/sys/vm/swapi ness

##### HOW TO USE FILE AS A VIRTUAL HARDISK ####

#create a file of lumpsume 1 GB

dd if=/dev/zero of=VHD.img bs=1M count=1200 

# fomat this file 

mkfs.ext4 VHD.img 

blkid VHD.img --> check 

#create dir 

mkdir /testdata 

#mount dir 

mount -t(type) auto -o(option) loop VHD.img(sourcefile usinng as block device thats why using loop) testdata 

#Fstab entry 

vi /etc/fstab 

VHD.img /testdata ext4 defaults 0 0




 

