class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        if nums[-1] != len(nums):
            return len(nums)
        if nums[0] != 0:
            return 0
        
        for i in range(1, len(nums)):
            expected = nums[i - 1] + 1
            if expected != nums[i]:
                return expected
        return -1