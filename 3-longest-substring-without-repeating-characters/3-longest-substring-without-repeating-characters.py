class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charDict = {}
        
        maxLength, windowStart = 0, 0
        
        for windowEnd in range(len(s)):
          char = s[windowEnd]
          
          charDict[char] = charDict.get(char, 0) + 1
          
          while charDict[char] > 1:
            newChar = s[windowStart]
            windowStart += 1
            charDict[newChar] -= 1
            
            if charDict[newChar] == 0:
              del charDict[newChar]
              
          maxLength = max(maxLength, windowEnd - windowStart + 1)
          
        return maxLength