"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return
        node = head
        while node:
            next = node.next
            node.next = ListNode(node.val)
            node.next.next = next
            node = node.next.next
        node = head
        while node and node:
            if not node.random:
                node.next.random = None
            else:
                node.next.random = node.random.next
            node = node.next.next
        dummy = ListNode()
        dummy.next = head.next
        mid = dummy.next
        slow, fast = head, head.next.next
        while slow and mid and fast:
            slow.next = fast
            mid.next = fast.next
            mid = mid.next
            slow = slow.next
            fast = fast.next.next
        return dummy.next