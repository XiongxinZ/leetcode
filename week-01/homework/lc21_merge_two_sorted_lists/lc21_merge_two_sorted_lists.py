# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2

        if l2 == None:
            return l1
        
        if l1.val > l2.val:
            head = l2
            l2.next = self.mergeTwoLists(l1, l2.next)
        else:
            head = l1
            l1.next = self.mergeTwoLists(l2, l1.next)
        
        return head