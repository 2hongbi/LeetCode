# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        node_set = set()

        while curr != None:
            if curr in node_set:
                return True
            
            node_set.add(curr)
            curr = curr.next
            
        return False
