class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        # Invariants: the minimum is always between l and r (inclusive)
        while l < r:
            mid = (l + r) // 2
            # If mid is in the left sorted portion, pivot must be right
            if nums[mid] < nums[r]:
                r=mid
            else:
                # mid might be the minimum, so keep it in range
                l = mid+1
        return nums[l]
