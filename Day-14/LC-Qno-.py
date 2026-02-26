# Two Sum

# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        dict1 = {}

        for i in range(n):
            rem = target -nums[i]
            if rem in dict1:
                return [dict1[rem],i]
            else:
                dict1[nums[i]] = i
        