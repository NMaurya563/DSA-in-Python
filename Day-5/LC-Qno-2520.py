# 2520. Count the Digits That Divide a Number 

class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        temp = num
        c = 0

        while temp>0:
            r=temp%10
            if r!=0 and num%r==0:
                c+=1
            temp//=10
        return c