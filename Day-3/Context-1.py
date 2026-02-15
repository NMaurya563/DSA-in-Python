# 3842. Toggle Light Bulbs 

class Solution(object):
    def toggleLightBulbs(self, bulbs):
        """
        :type bulbs: List[int]
        :rtype: List[int]
        """
        on_bulbs = set()
        for b in bulbs:
            # Using symmetric_difference_update for toggling efficiently
            on_bulbs.symmetric_difference_update([b])
        return sorted(on_bulbs)