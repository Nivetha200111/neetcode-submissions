class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in dictt:
                return [dictt[comp], i]
            if nums[i] not in dictt:
                dictt[nums[i]] = i
        return [-1,-1]
