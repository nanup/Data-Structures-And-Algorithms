class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        s = s.replace(" ", "")
        table = s.maketrans("", "", string.punctuation)
        s = s.translate(table)
        
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
            
        return True