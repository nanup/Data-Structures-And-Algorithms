class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        if len(prices) < 2:
            return profit
        
        buy, sell = 0, 0
        
        while sell < len(prices):
            currProfit = prices[sell] - prices[buy]
            
            if currProfit < 0:
                buy = sell
            
            if currProfit > profit:
                profit = currProfit
            
            sell += 1
            
        return profit