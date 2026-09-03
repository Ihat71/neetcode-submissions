class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        i, j = 0, 1
        
        max_profit = 0

        while j < len(prices):
            if prices[j] - prices[i] < 0:
                i=j
            else:
                if prices[j] - prices[i] >= max_profit:
                    max_profit = prices[j] - prices[i]
            j+=1
        print(i, j)
        return max_profit