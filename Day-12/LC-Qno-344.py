# 344. Reverse String

# Onbuilt function reverse() can be used to reverse the list in place.
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # return s.reverse()


# while swapping the elements, we can use a temporary variable to store the value of one element.

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i=0
        j=len(s)-1

        while i<j:
            temp=s[i]
            s[i]=s[j]
            s[j]=temp
            i+=1
            j-=1
        return s
        


        