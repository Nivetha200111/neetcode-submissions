class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for x in nums:
            count[x] = count.get(x,0) + 1
            sorted_items = sorted(count.items(), key=lambda x:x[1],reverse=True)
        return [num for num,_ in sorted_items[:k]]