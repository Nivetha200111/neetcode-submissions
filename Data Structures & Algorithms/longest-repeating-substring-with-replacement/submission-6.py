class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        mx = 0
        f = {}
        res = 0
        for r in range(len(s)):
            f[s[r]] = f.get(s[r],0)+1
            mx = max(mx,f[s[r]])
            while (r-l+1) - mx > k:
                f[s[l]]-=1
                l+=1
            res = max(res,r-l+1)
        return res