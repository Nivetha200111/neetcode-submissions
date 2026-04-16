class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sett = set(nums)
        
        ans = 0
        for x in sett:
            if x - 1 not in sett:
                mlen =1
                y = x
                while y + 1 in sett:
                    y+=1
                    mlen += 1
                ans = max(ans,mlen)
        return ans
