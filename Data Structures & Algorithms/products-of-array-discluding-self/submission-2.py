class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        res = []
        while i < len(nums):
            j = 0
            prodl = 1
            prodr = 1
            while j < i:
                prodl = prodl*(nums[j])
                j+=1
            k = i+1
            while k < len(nums):
                prodr = prodr*(nums[k])
                k+=1
            res.append(prodr*prodl)
            i+=1
        return res

            

            
