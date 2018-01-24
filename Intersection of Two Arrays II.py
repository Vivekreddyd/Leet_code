nums1=[1,2,3]
nums2=[4,2,6]

if not nums1 or not nums2:
    print(None)
s1=set(nums1)
s2=set(nums2)
ret_val= s1.intersection(s2)
print(ret_val)