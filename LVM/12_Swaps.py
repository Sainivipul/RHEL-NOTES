# what is  swap ?
# swap partition used by data as virtual memory when our physical memory is fully occupied 



check- lsblk 
 
 # CREATE SWAP PARTITION
# to do so first we need to chage the partitin type 

fdisk /dev/sdb
t --to chnge type 
L -- to find hax code (82 for liux swap )

82 -- linux swap 

w -- write ad save chage 

partprobe -- save the chage 

pvcretae /dev/sdb1  --physical volume 

vgcreate volgroup /dev/sdb1  --volume group 

lvcreate -L 2G - swapenw volgroup --logical volume 

mkswap /dev/volgroup/swapnew  --make it swap 

          done            
free -m --check 
lsblk --check we will find swap is ot in use 

swapon /dev/mapper/volgroup-swapnew   --activating swapenw

lsblk --check

blkid /dev/mapper/volgroup-swapnew --to get uu id of our swap 

# to make this chage permaennt make change in fstab file 

vim/etc/fsatb 
go i last line past UUID 

UUID swap defaults 00 --etry made i fstab chage is permananet nnow 

________________## EXTED THE SWAP________________

swapoff /dev/dm-2(swap number )

lsblk --check if swap is off 

 lvextend -L XG /dev/Volgroup/swap1 --extennded the LV attached to swap 

 lvs --check 

 swapon /dev/mapper/volgroup-swapnew --swap is on now 

 lsblk -- check 


#suppose our data is using swap sapce for critical process but now swap is also full 
# now we do not have eough time to create new paertiton or space to create new swap 
# in that case we can create swap file and also if swap is absent in our machine we can also 
# cerate swap file 

_______________##Swap file ___________________

# ex 64mb file swap file 

#block size = 64 X 1024 = 65536

login through root 

dd if=/dev/zer0 of=/swapfile bs=1024 count=65535 

chmod 0600 /swapfile --change permission 

mkswap /swapfile --setign up swapfile


#this will on immedeate after next boot but we want it to done right away and use

swapon /swapfile

vi /etc/fstab
/swapfile swap swap defaults 0 0

free -m --check 
