# 1431. Kids With the Greatest Number of Candies  

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        maxCandies = max(candies)
        ans = []

        for i in candies:
            if (i+extraCandies)>=maxCandies:
                ans.append(True)
            else:
                ans.append(False)
        return ans


        