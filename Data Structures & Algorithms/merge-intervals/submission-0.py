class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]
        for i in range(1,len(intervals)):
            ps, pe = res[-1]
            cs,ce = intervals[i]

            if cs <= pe:
                res[-1][1] = max(pe,ce)
            else:
                res.append([cs,ce])
        return res
