class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_num = nums[0]
        last_position = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[last_position-1]:
                pass
            else:
                last_num = nums[i]
                nums[i], nums[last_position] = nums[last_position], nums[i]
                last_position += 1

        return last_position