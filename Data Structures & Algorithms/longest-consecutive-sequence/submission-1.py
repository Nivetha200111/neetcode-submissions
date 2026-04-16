class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = sorted(set(nums))
        count = 1
        if not nums:
            return 0
        l = 1
        for i in range(0,len(sett)-1):
             
            if sett[i+1] - sett[i] == 1:
                count += 1
            else:
                l = max(l,count)
                count = 1
        return max(l,count)