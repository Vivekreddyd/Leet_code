import math
area=4
# for l in range(1,area+1):
#             w=area/l
#             n=area%l
#             if(n==0 and l>=w):
#                 print (list([l,w]))
mid=int(area**(1/2))
print (mid)
mid = int(math.sqrt(area))
while mid>0:
    if(area%mid==0):
        print (list([int(area / mid),int(mid)]))
    mid-=1