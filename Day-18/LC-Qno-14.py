# 14. Longest Common Prefix

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        prefix = strs[0]   # take first word
        
        for word in strs[1:]:
            
            while word.find(prefix) != 0:
                prefix = prefix[:-1]   # remove last character
                
                if prefix == "":
                    return ""
        
        return prefix
        