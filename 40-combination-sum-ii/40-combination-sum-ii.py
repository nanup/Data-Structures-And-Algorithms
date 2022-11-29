class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 1, 1, 2, 5, 6, 7, 10
        candidates.sort()
        uniqueCombinations = []
        
        def recurse(index, target, combination):
            if target == 0:
                uniqueCombinations.append(combination.copy())
                return
            
            if index >= len(candidates):
                return
            
            if target < candidates[index]:
                return
            
            for i in range(index, len(candidates)):
                if i != index and candidates[i] == candidates[i - 1]:
                    continue
                    
                combination.append(candidates[i])
                recurse(i + 1, target - candidates[i], combination)
                combination.pop()
                
        recurse(0, target, [])
        return uniqueCombinations