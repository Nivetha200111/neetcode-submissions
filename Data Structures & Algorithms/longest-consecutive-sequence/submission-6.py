class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        streak = 1
        best = 1
        nums.sort()
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        i = 0
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1] + 1:
                streak += 1
            else:
                best = max(best, streak)
                streak = 1
      
        return max(best, streak)