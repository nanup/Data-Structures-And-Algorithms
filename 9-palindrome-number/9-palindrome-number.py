class Solution:
    #time: O(N)
    #space: O(N)
    def isPalindrome(self, x: int) -> bool:
        copy = x
        y = 0
        while x > 0:
            lastDigit = x % 10
            y = 10 * y + lastDigit
            x //= 10
        return copy == y