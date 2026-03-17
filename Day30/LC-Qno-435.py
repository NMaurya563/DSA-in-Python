# 435. Non-overlapping Intervals  

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key = lambda x: x[1])
        n = len(intervals)

        prev = 0
        count = 1

        for i in range(1,n):
            if intervals[i][0]>=intervals[prev][1]:
                count+=1
                prev = i

        return n - count

                  
        