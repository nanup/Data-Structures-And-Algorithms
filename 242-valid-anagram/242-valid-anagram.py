class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freqList = [0] * 26
        
        for char in s:
            freqList[ord(char) - ord("a")] += 1
            
        for char in t:
            if freqList[ord(char) - ord("a")] == 0:
                return False
            freqList[ord(char) - ord("a")] -= 1
        
        return True