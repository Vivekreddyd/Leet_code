# class Solution(object):
#     def numberOfBoomerangs(self, points):
#         """
#         :type points: List[List[int]]
#         :rtype: int
#         """
points=[[3,6],[7,5],[3,5],[6,2],[9,1],[2,7],[0,9],[0,6],[2,6]]
boom_set_count=0
for i in points:
    temp={}
    for indx,j in enumerate(points):
        temp_val=abs(j[0]-i[0]+j[1]-i[1])
        # if(temp[temp_val]==[]):
        #     temp[temp_val]=[indx]
        # else:
        if(temp_val in temp):
            temp[temp_val]+=1
        else:
            temp[temp_val]=1
    for key,val in temp.items():
        if not key==0 and val>1:
            boom_set_count+=(val*(val-1))
print(boom_set_count)
# return boom_set_count# return boom_set_count
