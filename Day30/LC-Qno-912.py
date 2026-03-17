# 912. Sort an Array


"""Given an array of integers nums, sort the array in ascending order and return it.
You must solve the problem without using any built-in functions in O(nlog(n))
time complexity and with the smallest space complexity possible."""

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        minn = min(nums)
        maxx = max(nums)

        offset = -minn
        freq = [0] * (maxx - minn + 1)

        for num in nums:
            freq[num + offset] += 1

        result = []
        for i in range(len(freq)):
            while freq[i] > 0:
                result.append(i - offset)
                freq[i] -= 1

        return result
