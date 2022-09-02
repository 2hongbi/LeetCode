class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        missing = len(nums)
        
        for i in range(len(nums)):
            missing = missing ^ i ^ nums[i]
            
        return missing
    
            