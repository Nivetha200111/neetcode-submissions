class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        maxh = float("inf")
        maxa = 0
        while l < r:
            maxh = min(heights[r],heights[l])
            maxa = max(maxa,maxh*(r-l))
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return maxa