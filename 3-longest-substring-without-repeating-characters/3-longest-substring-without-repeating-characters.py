class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        dict = {}
        s = list(s)
        left, right = 0, 0
        while right < len(s):
            char = s[right]
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] += 1
            if dict[char] > 1:
                newChar = s[left]
                while dict[char] > 1:
                    dict[newChar] -= 1
                    left += 1
                    newChar = s[left]
            length = max(length, right - left + 1)
            right += 1
        return length
                