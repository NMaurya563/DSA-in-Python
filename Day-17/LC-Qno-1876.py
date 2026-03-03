# 1876. Substrings of Size Three with Distinct Characters

class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        ans = 0

        for i in range (n-2):
            if s[i]!=s[i+1] and s[i+1]!=s[i+2] and s[i+2]!=s[i]:
                ans+=1
        return ans
        