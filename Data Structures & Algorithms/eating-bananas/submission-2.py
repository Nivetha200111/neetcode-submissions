class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <=r: #traversing k from 1 to max(piles)
            k = (l+r)//2
            hrs = 0
            for p in piles: #traversing piles to find total hrs
                hrs += math.ceil(p/k)
            if hrs <= h:
                res = min(res,k)
                r = k-1
            else:
                l=k+1
        return res