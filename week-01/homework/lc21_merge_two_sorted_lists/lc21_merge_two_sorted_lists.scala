/**
 * Definition for singly-linked list.
 * class ListNode(_x: Int = 0, _next: ListNode = null) {
 *   var next: ListNode = _next
 *   var x: Int = _x
 * }
 */
object Solution {
    def mergeTwoLists(l1: ListNode, l2: ListNode): ListNode = {
        if (l1 == null) l2 else l1

        var head: ListNode = new ListNode()
        var temp: ListNode = null
        var pointer = head
        var h1 = l1
        var h2 = l2
        while(h1 != null && h2 != null) {
            if (h1.x < h2.x) {
                temp = h1
                h1 = h1.next
            } else {
                temp = h2
                h2 = h2.next
            }
            // 断链
            temp.next = null
            pointer.next = temp
            pointer = pointer.next
        }
        // l2节点遍历完了
        if (h1 != null) {
            pointer.next = h1
        }
        // l1节点遍历完了
        if (h2 != null) {
            pointer.next = h2
        }
        head.next
    }
}