#RAID -- Redundent array of inexpensive  disk 
Raid is a technology used to inncreate the performance and relaibilty of data storage 
Raid system contains 2 or more drives to work togther ( disk /ssd )

raid levels 
Raid 0 -striping 
raid 1 - mirroring 
raid 5 - strippig and parity 
raid 6 - stripping with double parity
raid 10- combining ad stripping 

## RAID 0 - Stripping

two drives {half data in one and remaining in other }
ADVANTAGE --->
great performace both in read and write operations 

All storage capacity is used 

the technology is easy to implement 

disadvantage -->

No fault tolrence 
should not be used for critical operations 

## RAID 1- mirroring 

two mirror drive both saving same data blocks of both driving same identical data 
storage capacity halfed 
Advantage 
exillent read and write speed 
if one drive fails no need to rebuild they just have to be copied to the replacement drive 

Raid 1 uis very simple tech 

Disadvantage 

space geot half 
both disk gone then data is gonne 

## RAID 5
data and pairity calculation stores in diffrennnt blocks 

Advanntage -->
read data transitions are very fast while write data are sometiems slow
we still have access to data even if drive failes 
disadvanbtage -->
complex tech

#Raid 6 
data stored inn blocks and dual perity is used 

Advatage -->
good recovry of data 
read data transition  is fast and more secure 
disadvanbtage-->
write trasition is slow and less oerformance as compared to raid 5

 




