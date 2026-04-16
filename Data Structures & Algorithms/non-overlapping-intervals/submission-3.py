class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1])
        res = 0
        pe = intervals[0][1]
        for i in range(1,len(intervals)):
            if pe > intervals[i][0]:

                res+=1
            else:
                pe = intervals[i][1]
        return res