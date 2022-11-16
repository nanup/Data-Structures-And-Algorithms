# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        carry = 0
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            num = a + b + carry
            digit, carry = Solution.nextDigit(self, num)
            tail.next = ListNode(digit)
            tail = tail.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            tail.next = ListNode(carry)
        return dummy.next
        
        
    def nextDigit(self, num):
        digit = num % 10
        carry = num // 10
        return (digit, carry)
        