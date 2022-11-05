# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            curr = head

            while curr != None:
                next_temp = curr.next
                curr.next = prev

                prev = curr
                curr = next_temp
            return prev

        r_l1 = reverse(l1)
        r_l2 = reverse(l2)

        res_head = None

        carry = 0
        while r_l1 != None or r_l2 != None:
            num1 = 0
            num2 = 0

            if r_l1 != None:
                num1 = r_l1.val
                r_l1 = r_l1.next
            
            if r_l2 != None:
                num2 = r_l2.val
                r_l2 = r_l2.next

            carry, num = divmod(num1 + num2 + carry, 10)

            node = ListNode(num)
            if res_head == None:
                res_head = node
            else:
                temp = res_head
                res_head = node
                node.next = temp

        if carry != 0:
            node = ListNode
            temp = res_head
            res_head = node
            node.next = temp

        return res_head
