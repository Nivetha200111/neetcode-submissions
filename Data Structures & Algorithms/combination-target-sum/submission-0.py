class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i,curr,total): #i -> pointer #curr -> current combination # total for curr combination
            if total == target:
                res.append(curr.copy()) #copy because other variables are also added in the loop
                return
            if i >= len(nums) or total > target:
                return

            # nums[i] is included to curr combinatopm
            curr.append(nums[i])
            dfs(i,curr,total+nums[i])
            #to clean up , curr combination values are added
            curr.pop()
            dfs(i+1,curr,total) #decision tree to branch
        dfs(0,[],0)
        return res
