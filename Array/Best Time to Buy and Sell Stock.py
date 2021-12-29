class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices.reverse()
        max_profit=0
        for i in range(len(prices)):       
            for j in range(i+1,len(prices)):
                max_profit=max(max_profit,prices[i]-prices[j])
        return max_profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        min_price=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]
            else:
                max_profit=max(prices[i]-min_price,max_profit)
        return max_profit
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit,lowest_price=0,float('inf')
        for price in prices:
            lowest_price=min(price,lowest_price)
            profit=max(price-lowest_price,profit)
        return profit