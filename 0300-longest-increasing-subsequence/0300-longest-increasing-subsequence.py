class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import bisect
        
        sub = []
        for num in nums:
            # Find the index where num should be placed
            i = bisect.bisect_left(sub, num)
            if i == len(sub):
                sub.append(num)  # Extend the subsequence
            else:
                sub[i] = num  # Replace to keep subsequence optimal
        return len(sub)