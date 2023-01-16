class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        
        for i in range(len(nums)):
            num = nums[i]
            
            if num in dict:
                return [i, dict[num]]
            dict[target - num] = i