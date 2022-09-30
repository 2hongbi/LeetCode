import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = collections.defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            hashmap[tuple(count)].append(s)
        
        return hashmap.values()