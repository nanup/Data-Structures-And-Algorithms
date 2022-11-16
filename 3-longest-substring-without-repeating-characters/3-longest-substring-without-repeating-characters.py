class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        
        left, right, longest = 0, 0, 1
        
        if len(s) < 1: return 0
        
        while right < len(s):
            if s[right] in seen:
                left = max(left, seen[s[right]] + 1)
                
            longest = max(longest, right - left + 1)
            
            seen[s[right]] = right
            
            right += 1
                 
        return longest
                