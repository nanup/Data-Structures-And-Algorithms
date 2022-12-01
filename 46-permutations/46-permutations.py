from collections import deque
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        permutations = deque()
        permutations.append([])
        
        for num in nums:
            for _ in range(len(permutations)):
                oldPermutation = permutations.popleft()
                
                for j in range(len(oldPermutation) + 1):
                    newPermutation = list(oldPermutation)
                    newPermutation.insert(j, num)
                    
                    if len(newPermutation) == len(nums):
                        result.append(newPermutation)
                    else:
                        permutations.append(newPermutation)
                        
        return result