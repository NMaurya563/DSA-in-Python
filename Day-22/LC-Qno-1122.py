# 1122. Relative Sort Array 

class Solution(object):
    def relativeSortArray(self, arr1, arr2):

        counts = [0] * 1001
        for num in arr1:
            counts[num] += 1
            
        res = []
        
        for num in arr2:
            while counts[num] > 0:
                res.append(num)
                counts[num] -= 1
                
        for num in range(len(counts)):
            while counts[num] > 0:
                res.append(num)
                counts[num] -= 1
                
        return res