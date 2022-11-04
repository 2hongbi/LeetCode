# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1_str = ""
        num2_str = ""

        l1_curr = l1
        l2_curr = l2

        while l1_curr != None:
            num1_str = num1_str + str(l1_curr.val)
            l1_curr = l1_curr.next

        while l2_curr != None:
            num2_str = num2_str + str(l2_curr.val)
            l2_curr = l2_curr.next

        res_num = int(num1_str) + int(num2_str)

        # dummy node
        head = ListNode(-1)
        curr = head
        for num_ch in str(res_num):
            curr.next = ListNode(int(num_ch))
            curr = curr.next

        curr.next = None
        return head.next
