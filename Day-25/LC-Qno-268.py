# 268. Missing Number

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        sum1=n*(n+1)//2
        sum2=sum(nums)
        return sum1-sum2