class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
          return 1
        
        isNegative = False
        if n < 0:
          isNegative = True
          n *= -1
          
        prod = 1
        
        while n > 0:
          if n % 2 == 0:
            x *= x
            n //= 2
          else:
            prod *= x
            n -= 1
            
        if isNegative:
          return 1 / prod
        else:
          return prod