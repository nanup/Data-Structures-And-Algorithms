class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #f(0, [])
        #f(1, [0])  f(1, [])
        #f(2, [0, 1]) f(2, [0]) f(2, [1]) f(2, [])
        
        powerSet = []
        nums.sort()
        
        def recurse(index, subset):
            powerSet.append(subset.copy())
            
            for i in range(index, len(nums)):
                if i != index and nums[i] == nums[i - 1]:
                    continue
                
                subset.append(nums[i])
                recurse(i + 1, subset)
                subset.pop()
            
        recurse(0, [])
        return powerSet