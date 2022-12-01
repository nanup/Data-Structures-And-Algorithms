class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        permutation = []
        k = k - 1 #modifying for 0 based indexing
        
        factorial = 1
        numbers = []
        
        for i in range(1, n):
            factorial = factorial * i
            numbers.append(i)
        numbers.append(n)
        
        def permute(factorial, k):
            permutation.append(str(numbers[k // factorial]))
            del numbers[k // factorial]
                        
            if not len(numbers):
                return
            
            k = k % factorial
            factorial = factorial // len(numbers)
            
            permute(factorial, k)
            
        permute(factorial, k)
        return "".join(permutation)