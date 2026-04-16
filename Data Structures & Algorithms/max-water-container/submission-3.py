class Solution:
    def maxArea(self, nums: List[int]) -> int:
        maxar = 0
        minheight = float("inf")
        l = 0
        r = len(nums)-1
        while l < r:
            minheight = min(nums[l],nums[r])
            maxar = max(maxar,(r-l)*minheight)
            if minheight == nums[l]:
                l+=1
            else:
                r-=1
        return maxar

            
            