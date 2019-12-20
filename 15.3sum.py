class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    if nums[l] == nums[l+1]:
                        l += 1
                    elif nums[r] == nums[r-1]:
                        r -= 1
                l, r = l+1, r-1


threeSum = Solution()
threeSum.threeSum([-1,0,1,2,-1,-4])