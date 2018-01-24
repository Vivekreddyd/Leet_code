nums=[-1,2,1,-4]
target=1
nums.sort()
result=nums[0]+nums[1]+nums[2]
for i in range(len(nums)-2):
    j,k=i+1,len(nums)-1
    while j<k:
        sum_val=nums[i]+nums[j]+nums[k]
        if sum_val==target:
            print(sum_val)
        if sum_val<target:
            j+=1
        elif sum_val > target:
            k-=1
print(result)