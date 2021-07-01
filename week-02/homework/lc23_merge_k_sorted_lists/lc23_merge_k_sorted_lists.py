# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 分治合并
        # 最小问题是lc21合并两个有序链
        def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
            if l1 == None:
                return l2

            if l2 == None:
                return l1
            
            head = ListNode()
            tail = head
            ptr1 = l1
            ptr2 = l2
            while ptr1 != None and ptr2 != None:
                if ptr1.val < ptr2.val:
                    tail.next = ptr1
                    ptr1 = ptr1.next
                else:
                    tail.next = ptr2
                    ptr2 = ptr2.next
                
                tail = tail.next
            
            if ptr1 is None:
                tail.next = ptr2
            else:
                tail.next = ptr1
            
            return head.next
        
        # 二分法
        def merge(lists: List[ListNode], l: int, r: int) -> ListNode:
            if l == r:
                return lists[l]

            if l > r:
                return None
            
            mid = (l + r) >> 1
            return mergeTwoLists(merge(lists, l, mid), merge(lists, mid+1, r))
        
        return merge(lists, 0, len(lists) - 1)

# 时间复杂度：总感觉分析不太对
# 空间复杂度：O(log k)