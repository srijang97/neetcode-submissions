# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if l1.val == 0:
            return l2
        elif l2.val == 0:
            return l1


        dummy = ListNode(0)
        curr = dummy

        carry = 0

        while l1 and l2:

            sum = l1.val + l2.val + carry

            digit = sum%10
            carry = sum //10

            curr.next = ListNode(digit)

            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        while l1:

            sum = l1.val + carry
            digit = sum%10
            carry = sum //10

            curr.next = ListNode(digit)
            curr = curr.next
            l1 = l1.next

        while l2:

            sum = l2.val + carry
            digit = sum%10
            carry = sum //10

            curr.next = ListNode(digit)
            curr = curr.next
            l2 = l2.next

        if carry > 0:
            curr.next = ListNode(carry)
            
        return dummy.next






        
        