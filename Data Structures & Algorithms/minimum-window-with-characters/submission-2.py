class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return t
        if len(t) > len(s):
            return ""
        tcount = {}
        for char in t:
            tcount[char] = tcount.get(char, 0) + 1
        w_count = {}
        l = 0
        r = 0
        ans = (float("inf"),0,0)
        f = 0
        req = len(tcount)
        while r < len(s):
            w_count[s[r]] = w_count.get(s[r],0)+1
            ch = s[r]
            if ch in tcount and w_count[ch] == tcount[ch]:
                f += 1
            r+=1
            while f == req:
                ans = min(ans,(r-l,l,r))
                w_count[s[l]] -= 1
                left = s[l]
                if left in tcount and w_count[left] == tcount[left] - 1:
                    f -= 1
                l+=1
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]]
                



