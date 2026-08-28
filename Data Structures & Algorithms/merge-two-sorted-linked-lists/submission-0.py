# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            return list2
        
        if not list2:
            return list1

        newHead = None
        
        if list1.val < list2.val:
            newHead = ListNode(list1.val, None)
            list1 = list1.next
        else:
            newHead = ListNode(list2.val, None)
            list2 = list2.next

        curr = newHead

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                curr.next = ListNode(list1.val, None)
                list1 = list1.next
            else:
                curr.next = ListNode(list2.val, None)
                list2 = list2.next
            
            curr = curr.next

        while list1 != None:
            curr.next = ListNode(list1.val, None)
            list1 = list1.next            
            curr = curr.next
        
        while list2 != None:
            curr.next = ListNode(list2.val, None)
            list2 = list2.next            
            curr = curr.next
        
        return newHead
                

