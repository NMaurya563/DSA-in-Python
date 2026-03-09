# LeetCode Qno. 120. Triangle

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0

        min_path = triangle[-1][:]
        for row in range(len(triangle)-2,-1,-1):
            for col in range(len(triangle[row])):
                min_path[col]=triangle[row][col]+min(min_path[col],min_path[col+1])

        return min_path[0]
        