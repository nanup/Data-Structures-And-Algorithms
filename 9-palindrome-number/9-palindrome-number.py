class Solution:
    def isPalindrome(self, x: int) -> bool:
        copy = x
        x = abs(x)
        y = 0
        while x > 0:
            lastDigit = x % 10
            y = 10 * y + lastDigit
            x //= 10
        return copy == y