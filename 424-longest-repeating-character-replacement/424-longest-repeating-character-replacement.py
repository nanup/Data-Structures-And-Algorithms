class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charDict = {}
        repeatCount = 0
        maxLength, windowStart = 0, 0
        
        for windowEnd in range(len(s)):
          char = s[windowEnd]
          
          charDict[char] = charDict.get(char, 0) + 1
          
          repeatCount = max(repeatCount, charDict[char])
          
          if (windowEnd - windowStart + 1 - repeatCount) > k:
            newChar = s[windowStart]
            windowStart += 1
            charDict[newChar] -= 1
              
          maxLength = max(maxLength, windowEnd - windowStart + 1)
          
        return maxLength
          