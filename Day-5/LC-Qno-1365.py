# 1365. How Many Numbers Are Smaller Than the Current Number 

# Brute Force Approach:

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in nums:
            c = 0
            for j in nums:
                if j<i:
                    c+=1
            ans.append(c)
        return ans