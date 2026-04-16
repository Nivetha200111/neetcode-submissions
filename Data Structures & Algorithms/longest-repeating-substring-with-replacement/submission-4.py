class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = {}
        l = 0
        maxf = 0
        res = 0

        for r, ch in enumerate(s):
            cnt[ch] = cnt.get(ch, 0) + 1
            maxf = max(maxf, cnt[ch])

            while (r - l + 1) - maxf > k:
                cnt[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
