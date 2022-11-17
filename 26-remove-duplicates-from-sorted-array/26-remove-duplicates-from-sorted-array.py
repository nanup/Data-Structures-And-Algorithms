class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        num = nums[0]
        for i in range(len(nums)):
            if nums[i] != num:
                nums[index] = nums[i]
                index += 1
                num = nums[i]
        return index
                