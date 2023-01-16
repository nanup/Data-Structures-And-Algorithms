class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 0
        profit = 0
        while right < len(prices):
            currProfit = prices[right] - prices[left]
            if currProfit < 0:
                left = right
            if currProfit > profit:
                profit = currProfit
            right += 1
            
        return profit