class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        sum_val = nums[0]
        for num in nums[1:]:
            sum_val = ~(sum_val ^ num)
        if sum_val==0:
            return True
        else:
            return False

temp=Solution()
val=[1,2,5]
temp.containsDuplicate(val)