class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 0:
            return 0
        
        curr = nums[0]
        cnt = 1
        
        for i in range(1, len(nums)):
            if curr != nums[i]:
                curr = nums[i]
                nums[cnt] = curr
                cnt += 1
        return cnt
        