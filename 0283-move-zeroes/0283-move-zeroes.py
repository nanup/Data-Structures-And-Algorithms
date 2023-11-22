class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        last = 0

        for i in range(len(nums)):
            num = nums[i]
            
            if num: 
                nums[i], nums[last] = nums[last], nums[i]
                last += 1