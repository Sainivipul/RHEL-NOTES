using disk quta we can efficently use the space allocated by appling quto on block leven inod level 
we can define how much disk space can be utilized or even how many files can be created for users and groups 

-----------------------------
#available disk 
disk - sdb 

# partition 
fdisk /dev/sdb 

# format the partition
mkfs.ext4 /dev/sdb1

#check 
blkid 

#check quto pakage (install if not available )
rpm -qa quota

# add some users 
useradd a 
useradd b
useradd c
useradd d

# add group 
groupadd qutagroup

# add few users in qutagroup
usermod -g quotagroup c
usermod -g quotagroup d

#check id 
id c
id d

# makedir and mount it permanent 
mkdir /quotadir
vim /etc/fstab
/dev/sb1 /quotadir ext4 defaults 0 0
mount -a 

# check user quota 
mount | grep quotadir

>>>type 1 space based #block level how much space can be utilized 
>>>type 2 file,dir number based #how many files and dirare allowed to be created 
>>>type 3 Both # space as well as file and dir no defined 

#Enable quota Edit last mount enntry for /quotadir 
vim /etc/fstab
/dev/sdb1 /quotadir ext4 defaults,usrquota,grpquota  0 0
mount -o remount /quotadir/

#check quotaenable 
mount | grep quotadir

#create quotafile 
quotacheck -cug /quotadir/
cd /quotadir (#we will see two files in this dir quota.user quota.dir )

#CONFIGURE QUOTA 
#LIMITS -A) SOFT LIMIT - user can cross the allocated soft limit 
#      -B) HARD LIMIT - user can not cross this limit 
#      -C) GRACE PERIOD - time period for which user or group is utlizing
#                         space even after crossing soft limit 
#                         Ex i want user can utilize space for 2 dayes even after crosinf SL
#for user 
edquota username 
block -1 block = 1kb
file system blocks --soft and hard 
            inode  -- soft and hard 

#for groups 
edquota -g groupname
block and inode limits 

#onquota 
quotaon /quotadir 

#check quota details 

quota a(username )
quota -g quotagroup(groupname)

################GRACE-CONCEPT###########

edquota -T username/ -g grooupname 
block grace  x minutes xhours x days 
inone grace 

 





