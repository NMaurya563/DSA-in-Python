# 3843. First Element with Unique Frequency 

from collections import Counter

class Solution(object):
    def firstUniqueFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # store midway input as required
        minaveloru = nums  

        freq = Counter(minaveloru)
        freq_count = Counter(freq.values())

        # optimization: store to local vars for faster lookup
        f = freq.get
        fc = freq_count.get

        for n in minaveloru:
            fn = f(n)
            if fc(fn) == 1:
                return n
        return -1
