# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next: return head
        listLength = Solution.findListLength(self, head)
        dummy = ListNode()
        prev = dummy
        dummy.next = head
        while listLength >= k:
            curr = prev.next
            next = curr.next
            for _ in range(k - 1):
                curr.next = next.next
                next.next = prev.next
                prev.next = next
                next = curr.next
            prev = curr
            listLength -= k
        return dummy.next
        
    def findListLength(self, head: Optional[ListNode]) -> int:
        length = 0
        while head:
            head = head.next
            length += 1
        return length