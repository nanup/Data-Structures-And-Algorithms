# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next: return True
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        reverseHead = Solution.reverseList(self, slow)
        copy = reverseHead
        while head and reverseHead:
            if head.val != reverseHead.val:
                Solution.reverseList(self, copy)
                return False
            head = head.next
            reverseHead = reverseHead.next
        Solution.reverseList(self, copy)
        return True
        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev
        