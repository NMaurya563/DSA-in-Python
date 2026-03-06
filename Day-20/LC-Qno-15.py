# 15. 3Sum

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        n = len(nums)
        
        for i in range(n - 2):
            # Pruning 1: If the smallest possible sum is > 0, stop entirely
            if nums[i] + nums[i+1] + nums[i+2] > 0:
                break
            
            # Pruning 2: If the current num + the two largest is < 0, 
            # this 'i' can't form a triplet; move to the next 'i'
            if nums[i] + nums[n-2] + nums[n-1] < 0:
                continue
            
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left, right = i + 1, n - 1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                
                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                        
        return res