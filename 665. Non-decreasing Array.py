class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # sum_val=(0 for i in range(len(nums)) if nums[i]<=nums[i+1])
        prev_val = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # sum_val+=1
                if prev_val > nums[i + 1]:
                    return False
            prev_val = nums[i]
        return True
temp=Solution()
ip=[1,5,4,6,7,10,8,9]
temp.checkPossibility(ip)