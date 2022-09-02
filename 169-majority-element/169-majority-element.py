class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority_count = int(len(nums) / 2)
    
        hashmap = {}
        
        for num in nums:
            if hashmap.get(num) != None:
                hashmap[num] = hashmap[num] + 1
            else:
                hashmap[num] = 1
            
            if hashmap[num] > majority_count:
                return num
        return -1