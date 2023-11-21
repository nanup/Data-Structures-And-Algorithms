class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_position = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[last_position-1]:
                nums[last_position] = nums[i]
                last_position += 1

        return last_position