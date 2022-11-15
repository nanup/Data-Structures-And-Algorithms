class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(nums):
            newNum = target - num
            if newNum not in dict:
                dict[num] = i
            else:
                return [i, dict[newNum]]