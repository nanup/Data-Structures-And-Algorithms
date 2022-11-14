class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            num = nums[i]
            while num - 1 != i:
                if nums[num - 1] == num:
                    return num
                nums[i], nums[num - 1] = nums[num - 1], nums[i]
                num = nums[i]