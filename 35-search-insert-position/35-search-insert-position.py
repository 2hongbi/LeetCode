class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = 0
        
        while index < len(nums):
            if target <= nums[index]:
                break
            index += 1
        return index
        