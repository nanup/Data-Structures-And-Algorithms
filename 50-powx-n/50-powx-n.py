class Solution:
    def myPow(self, x: float, n: int) -> float:
        prod = 1
        if n == 0: return prod
        isNeg = False
        if n < 0:
            n *= -1
            isNeg = True
        while n > 0:
            if n % 2:
                prod *= x
                n -= 1
            else:
                x = x * x
                n /= 2
        if isNeg: return 1 / prod
        return prod