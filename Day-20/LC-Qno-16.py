# 16. 3Sum Closest

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')
        
        for i in range(n - 2):
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            
            min_sum = nums[i] + nums[i+1] + nums[i+2]
            if min_sum > target:
               
                if abs(min_sum - target) < abs(closest_sum - target):
                    closest_sum = min_sum
                
                break 
            
           
            max_sum = nums[i] + nums[n-2] + nums[n-1]
            if max_sum < target:
                
                if abs(max_sum - target) < abs(closest_sum - target):
                    closest_sum = max_sum
                continue

            
            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == target:
                    return target
                
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                if current_sum < target:
                    left += 1
                    
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                else:
                    right -= 1
                    
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
        return closest_sum