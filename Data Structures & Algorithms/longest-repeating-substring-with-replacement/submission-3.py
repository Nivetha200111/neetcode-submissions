class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = {}
        l = 0
        maxf = 0
        best = 0

        for r, ch in enumerate(s):
            cnt[ch] = cnt.get(ch, 0) + 1     
            maxf = max(maxf, cnt[ch])         
            while (r-l+1) - maxf > k:
                cnt[s[l]] -= 1
                l+=1
            best = max(best, r-l+1)
        return best
        
        