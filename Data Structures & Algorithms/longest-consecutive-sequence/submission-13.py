class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        count = 1
        leng = 0
        for num in numset:
            if num-1 not in numset:
                count=1
                while  num + count in numset:
                    count += 1
            leng = max(count, leng)
        return leng