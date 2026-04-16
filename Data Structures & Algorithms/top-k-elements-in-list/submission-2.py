class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n,0)+1
        
        buck = [[] for _ in range(len(nums)+1)]
        for num,f in freq.items():
            buck[f].append(num)
        
        res = []
        for i in range(len(buck)-1,0,-1):
            for num in buck[i]:
                res.append(num)
                if len(res)==k:
                    return res