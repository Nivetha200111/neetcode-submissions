class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        # for i in range(len(nums)):
        #     prodx = 1
        #     prody = 1
        #     prod = 1
        #     for j in range(0,i):
        #         prodx*=nums[j]
        #     for k in range(i+1,len(nums)):
        #         prody*=nums[k]
        #     prod = prodx*prody
        #     res.append(prod)
        # return res
        i = 0
        pre = []
        prodx = 1
        while i < len(nums):
            pre.append(prodx)
            prodx=prodx*nums[i]
            i+=1
        j = len(nums)-1
        post = [1]*len(nums)
        prody = 1
        while j >= 0:
            post[j] = prody
            prody=prody*nums[j]
            j-=1
        for i in range(len(nums)):
            res.append((pre[i]*post[i]))
        return res


                
                