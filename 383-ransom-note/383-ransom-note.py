class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = {}
        for char in magazine:
            if not char in dict: dict[char] = 0
            dict[char] += 1
            
            
        for char in ransomNote:
            if char not in dict:
                return False
            else:
                if dict[char] == 0:
                    return False
                else:
                    dict[char] -= 1
                    
        return True
            