class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        def recurse(index, subset = []):
            result.append(subset.copy())
            for i in range(index, len(nums)):
                if i != index and nums[i] == nums[i - 1]:
                    continue
                    
                subset.append(nums[i])
                recurse(i + 1, subset)
                subset.pop()
        recurse(0)
        return result