class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            prodx = 1
            prody = 1
            prod = 1
            for j in range(0,i):
                prodx*=nums[j]
            for k in range(i+1,len(nums)):
                prody*=nums[k]
            prod = prodx*prody
            res.append(prod)
        return res

                
                