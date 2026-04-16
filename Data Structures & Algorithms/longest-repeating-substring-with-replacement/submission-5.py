class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        i = 0
        j = 0
        maxc = 0 
        best = 0
        while j < len(s):
            count[s[j]] += 1
            maxc = max(maxc, count[s[j]])

            while (j-i+1)-maxc > k:
                count[s[i]]-=1
                i+=1
            best = max(maxc,(j-i+1))
            j+=1
        return best
        