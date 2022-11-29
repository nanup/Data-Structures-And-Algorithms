class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        # to quickly terminate the recursion
        
        uniqueCombinations = []
        
        def recurse(index, target, currentCombination):
            if target == 0:
                uniqueCombinations.append(currentCombination.copy())
                return
            
            if index >= len(candidates):
                return
            
            candidate = candidates[index]
            
            if target < candidate:
                return
            
            currentCombination.append(candidate)
            recurse(index, target - candidate, currentCombination)
            currentCombination.pop()
            recurse(index + 1, target, currentCombination)
        
        recurse(0, target, [])
        return uniqueCombinations