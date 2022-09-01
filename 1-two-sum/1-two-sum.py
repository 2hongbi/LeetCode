class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashtable_dict = {}
        
        for i in range(0, len(nums)):
            value = target - nums[i]
            
            if hashtable_dict.get(value) is not None and hashtable_dict[value] != i:
                return sorted([i, hashtable_dict[value]])
            
            hashtable_dict[nums[i]] = i
            
        return [-1, -1]