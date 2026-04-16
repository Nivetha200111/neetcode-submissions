class Solution:
    def search(self, arr: List[int], target: int) -> int:
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = l + (r - l) // 2;
            if target == arr[mid]:
                return mid
            if target < arr[mid]:
                r = mid -1
               
            if target > arr[mid]:
                l = mid + 1

            
        return -1