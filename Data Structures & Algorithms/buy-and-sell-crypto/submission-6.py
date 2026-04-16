class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        minpr = float("inf")
        for price in prices:
            prof = price - minpr
            maxp = max(maxp, prof)
            minpr = min(minpr,price)
        return maxp