class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = float("inf")
        maxp = 0
        for p in prices:
            minp = min(p,minp)
            maxp = max(p-minp,maxp)
        return maxp