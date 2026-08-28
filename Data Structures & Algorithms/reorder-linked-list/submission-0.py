# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        secondHalf = slow.next
        prev  = None
        
        while secondHalf:
            tempNext = secondHalf.next
            secondHalf.next = prev
            prev = secondHalf
            secondHalf = tempNext

        secondHalf = prev

        slow.next = None

        curr = head

        while curr and secondHalf:
            sNext = secondHalf.next
            nextNode = curr.next

            curr.next = secondHalf
            curr.next.next = nextNode
            curr = nextNode
            secondHalf = sNext

        
