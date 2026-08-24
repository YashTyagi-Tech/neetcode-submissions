class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice=prices[0]
        max_profit=0
        for price in prices:
            minPrice=min(price,minPrice)
            profit=price-minPrice
            max_profit=max(profit,max_profit)
        return max_profit
        