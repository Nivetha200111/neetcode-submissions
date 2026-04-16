class Solution:
    def longestPalindrome(self, s: str) -> str:
        idx = 0
        rlen = 0
        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and  r < len(s) and s[l] == s[r]:
                if r - l + 1 > rlen:
                    idx = l
                    rlen = r - l + 1
                l-=1
                r += 1
            l = i
            r = i+1
            while l >= 0 and  r < len(s) and s[l] == s[r]:
                if r - l + 1 > rlen:
                    idx = l
                    rlen = r - l + 1
                l-=1
                r += 1
        return s[idx:idx+rlen]