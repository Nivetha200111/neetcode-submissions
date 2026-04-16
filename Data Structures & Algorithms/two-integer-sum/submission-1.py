class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt = {}
        for i,x in enumerate(nums):
            comp = target - x
            if comp in dictt:
                return [dictt[comp],i]
            dictt[x] = i
        