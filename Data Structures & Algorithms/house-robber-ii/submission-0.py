class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def circular(arr):
            one = 0
            two = 0
            for x in arr:
                two,one = one,max(two+x,one)
            return one
        return max(circular(nums[:-1]),circular(nums[1:]))