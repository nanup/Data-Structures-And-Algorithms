class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        permutation = [0] * n
        currentIndex = 0
        k = k - 1 #modifying for 0 based indexing
        
        factorial = 1
        numbers = []
        
        for i in range(1, n):
            factorial = factorial * i
            numbers.append(i)
        numbers.append(n)
        
        def permute(factorial, k, currentIndex):
            permutation[currentIndex] = str(numbers[k // factorial])
            del numbers[k // factorial]
                        
            if not len(numbers):
                return
            
            k = k % factorial
            currentIndex += 1
            factorial = factorial // len(numbers)
            
            permute(factorial, k, currentIndex)
            
        permute(factorial, k, 0)
        return "".join(permutation)