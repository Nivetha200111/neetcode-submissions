class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictt = {}
        for num in nums:
            if num not in dictt:
                dictt[num] = 0
            dictt[num] += 1
        # for i in range(len(nums)):
        #     if nums[i] not in dictt:
        #         dictt[nums[i]] =0
        #     dictt[nums[i]] +=1
        # sorted_items = sorted(dictt.items(), key=lambda x:x[1],reverse=True)
        # return [item[0] for item in sorted_items[:k]]
        freq = [[] for _ in range(len(nums) + 1)]
        for num, count in dictt.items():
            freq[count].append(num)
            
        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
