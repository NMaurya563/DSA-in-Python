# 1281. Subtract the Product and Sum of Digits of an Integer 

class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp = n
        sum_ = 0
        product = 1

        while temp>0:
            r = temp%10
            temp//=10
            sum_+=r
            product*=r

        return product-sum_

        