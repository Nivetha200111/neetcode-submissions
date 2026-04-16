class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r = len(prices)-1
        l = 0
        low = float('inf')
        maxstock = 0
        for p in prices:
            low = min(low,p)
            maxstock = max(maxstock,p-low)
        return maxstock
