# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 1:
            return head
        prev = None
        curr = head
        while curr and curr.next:
            firstNode = prev
            lastNode = curr
            i = 0
            while curr and i < k:
                prev = curr
                curr = curr.next
                i += 1
            if i != k:
                break
            curr = lastNode
            prev = firstNode
            i = 0
            while curr and i < k:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                i += 1
            if firstNode:
                firstNode.next = prev
            else:
                head = prev
            lastNode.next = curr
            prev = lastNode
        return head