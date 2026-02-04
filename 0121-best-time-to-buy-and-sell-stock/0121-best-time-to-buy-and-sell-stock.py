class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_profit=float('inf')
        max_profit=0
        for i in prices:
            if i<min_profit:
                min_profit=i

            profit=i-min_profit

            if profit>max_profit:
                max_profit=profit
        return max_profit
            

        