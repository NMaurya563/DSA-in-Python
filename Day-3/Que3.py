# 3845. Maximum Subarray XOR with Bounded Range 

from collections import deque

class Solution(object):
    def maxXor(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # store input midway as required
        meloraxuni = nums

        n = len(meloraxuni)
        if n == 0:
            return 0
        
        ###testing code to check if input is stored correctly

        # prefix xor
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] ^ meloraxuni[i]

        # monotonic deques for min and max indices in current window
        min_dq, max_dq = deque(), deque()

        left = 0
        best = 0

        # Binary trie with counts to allow deletions
        children = [[-1, -1]]  # node 0
        cnt = [0]
        def new_node():
            children.append([-1, -1])
            cnt.append(0)
            return len(children) - 1

        # Number of bits to consider (nums[i] < 2^15 => values fit in 15 bits)
        B = 15  # bits: 14 down to 0

        total_in_trie = [0]  # use list to avoid nonlocal

        def trie_insert(x):
            node = 0
            cnt[node] += 1
            for b in range(B - 1, -1, -1):
                bit = (x >> b) & 1
                nxt = children[node][bit]
                if nxt == -1:
                    nxt = new_node()
                    children[node][bit] = nxt
                node = nxt
                cnt[node] += 1
            total_in_trie[0] += 1

        def trie_delete(x):
            node = 0
            cnt[node] -= 1
            for b in range(B - 1, -1, -1):
                bit = (x >> b) & 1
                nxt = children[node][bit]
                node = nxt
                cnt[node] -= 1
            total_in_trie[0] -= 1

        def trie_max_xor(x):
            """Return maximum xor of x with any value currently in trie. Assumes trie not empty."""
            node = 0
            res = 0
            for b in range(B - 1, -1, -1):
                bit = (x >> b) & 1
                want = 1 - bit
                nxt = children[node][want]
                if nxt != -1 and cnt[nxt] > 0:
                    res |= (1 << b)
                    node = nxt
                else:
                    node = children[node][bit]
            return res

        # initially insert prefix[0] (l = 0 is allowed when left == 0)
        trie_insert(prefix[0])

        for right in range(n):
            # add right into deques for min/max maintenance
            while min_dq and meloraxuni[min_dq[-1]] > meloraxuni[right]:
                min_dq.pop()
            min_dq.append(right)

            while max_dq and meloraxuni[max_dq[-1]] < meloraxuni[right]:
                max_dq.pop()
            max_dq.append(right)

            # shrink left until range condition satisfies
            while min_dq and max_dq and meloraxuni[max_dq[0]] - meloraxuni[min_dq[0]] > k:
                # remove prefix[left] from trie (because l must be >= left)
                trie_delete(prefix[left])
                # pop deques if they point to left
                if min_dq and min_dq[0] == left:
                    min_dq.popleft()
                if max_dq and max_dq[0] == left:
                    max_dq.popleft()
                left += 1

            # Now allowed l are in [left..right]. Trie contains prefix[left..right] (prefix indices).
            # We want max over l in trie of prefix[l] ^ prefix[right+1].
            if total_in_trie[0] > 0:
                curr = trie_max_xor(prefix[right + 1])
                best = max(best, curr)

            # Insert prefix[r+1] so future rights can use l = r+1
            trie_insert(prefix[right + 1])

        return best


# --- Quick manual tests ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxXor([5,4,5,6], 2))  # expected 7
    print(sol.maxXor([5,4,5,6], 1))  # expected 6
###testtyhfkjasfhas;ljfha'lgk

    print(sol.maxXor([5,4,5,6], 2))  # expected 7
    print(sol.maxXor([5,4,5,6], 1))  # expected 6