class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictt ={}
        for i in range(len(nums)):
            if nums[i] not in dictt:
                dictt[nums[i]] = 0
            dictt[nums[i]] += 1
        sorted_items = sorted(dictt.items(), key=lambda x:x[1], reverse=True)

        return [item[0] for item in sorted_items[:k]]