class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        
        def permute(permutation):
            if len(permutation) == len(nums):
                permutations.append(permutation.copy())
                return
            
            for num in nums:
                if num not in permutation:
                    permutation.append(num)
                    permute(permutation)
                    permutation.pop()
                
        permute([])
        return permutations