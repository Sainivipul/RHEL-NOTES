## Bootinng sequence of Rhel 
booting - the process of copying files of OS on RAM from HD drive is known as Booting
booting files locate on /boot dir 


GERNAL booting flow 

POST(powe on self test)----> BIOS ( basic innput output system )------> MBR (master boot record )
--- > GRUB2 (granunified boot loader ) --> Kernal ----> H/W installation ---> /sbin/init execution 
-----> initrd.target execution ---> switches root filesystem ----> systemd looks for default.target 

#POST (POWER ON SELF TEST)
when we power on current flows onn motherboard and give signnal to had over process to bios 

#BIOS (BASIC INPUT OUTPUT)
basic input and output system combinationof hardware annd softeare located in chip in motherboard containing a program
one or two beep if all good otherwise continious beep 
here we can make limited changes which saved on shemos 
now a days it is replaced by UEFI advanced version of bios 

bios contain info of all the booting devices and handover process to MBR 

#MBR (MASTER BOOT RECORD )
64 bytes reserved for the partiton table 

#GRUB 2 (GRAND UNIFIED BOOT Loder )

loads kernal into memory or ram 
provide option to choose kernal for boot ot load automatically with default one if do not get any response
grab 2 loads its configuration from /boot/grub2/grub.cfg file 
loads default VMLinuz kernal image then extract the contents od initramfs image

#KERNAL 
kernal try to mout root file system and this requires moduls and drivers 
kernal get all the drivers and modules in initramfs 

kernal initialises all the #H/W componenets 

#/sbin/init Execution 
kernal execute /sbin/init from the initramfs as the first process with process id (PID=1)
in RHEL 8 systemd is teh first process and start at booting of the machine ad run  till the 
machine run it is also the last process and loads conponenets of othger process 
wx mounting root file system 

#SWITCH ROOT FILE SYSTEM 
kernal root flesystem switched from initramfs to system root file system 

#SYTEMD LOOKS FOR DEFALT TARGET 
systemd reads the file linked to determine the default system target 


there are 7 targets available in RHEL 8 which can be used to boot up the machine in diffrent mode as per the requirement 

ls-l /liv/systemd/system/runlevel*target -- to list all the available targets 


------------(## difrfrent run levels )-------

7 run level 0-6

0-- power off run level , poweroff the system
1-- single user mode wityhout GUI, without networking used for troubleshoot 
2--  multiuser without GUI, without networking 
3-- multiuser mode withour GUi but with networking 
4-- multiuser for reserch only
5-- multiuser graphical mode with neworking (mostly used)
6-- reboot the system 

runlevel -- shows output as previous run level and current runlevel 



