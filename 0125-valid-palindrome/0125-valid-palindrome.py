class Solution:
    def remove_ascii_chars(self, s: str) -> List[str]:
        return list(filter(str.isalnum, s))

    def isPalindrome(self, s: str) -> bool:
        s_list = Solution.remove_ascii_chars(self, s.lower())

        left, right = 0, len(s_list) - 1

        while left <= right:
            if s_list[left] != s_list[right]:
                return False

            left += 1
            right -= 1

        return True