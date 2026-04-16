class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodl = 1
        prodr = 1
        res = [1]*len(nums)
        for i in range(len(nums)):
            j = len(nums) - 1 - i
            res[i]*=prodl
            res[j]*=prodr
            prodl = prodl*nums[i]
            prodr = prodr*nums[j]
            
        return res