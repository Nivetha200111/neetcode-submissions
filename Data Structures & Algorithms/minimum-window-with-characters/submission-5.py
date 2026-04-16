class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        have = {}
        formed = 0
        required = len(need)
        l = 0
        best = float("inf")
        bL = 0
        for r in range(len(s)):
            have[s[r]] = have.get(s[r],0)+1
            if s[r] in need and have[s[r]] == need[s[r]]:
                formed += 1
            while formed == required:
                if r-l+1 < best:
                    best = r - l +1
                    bL = l
                have[s[l]]-=1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    formed -= 1
                l+=1
        return s[bL: bL+best] if best != float("inf") else ""