class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []
        subsets.append([])
        for i in range(len(nums)):
            start = 0
            if i > 0 and nums[i] == nums[i - 1]:
                start = end
            end = len(subsets)
            for j in range(start, end):
                subset = list(subsets[j])
                subset.append(nums[i])
                subsets.append(subset)
        return subsets