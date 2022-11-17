# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        isCyclic = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                isCyclic = True
                break
        if not isCyclic: return
        loopLength = 1
        next = slow.next
        while slow != next:
            next = next.next
            loopLength += 1
        slow, fast = head, head
        for _ in range(loopLength):
            fast = fast.next
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow