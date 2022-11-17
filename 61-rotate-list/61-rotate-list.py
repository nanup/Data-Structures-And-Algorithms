# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0: return head
        copy = head
        length = 0
        slow = head
        while slow:
            slow = slow.next
            length += 1
        k %= length
        if k == 0:
            return head
        i = length - k
        curr = head
        for _ in range(i - 1):
            curr = curr.next
            next = curr.next
        head = curr.next
        curr.next = None
        curr = head
        for _ in range(k - 1):
            curr = curr.next
        curr.next = copy
        return head