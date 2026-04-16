class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        best = 0
        seen = set()
        for r,ch in enumerate(s):
            while ch in seen:
                seen.remove(s[l])
                l+=1
            seen.add(ch)
            best = max(best, r-l+1)
        return best