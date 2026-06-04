class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev1 = 0  # dp[i-1]

        prev2 = 0  # dp[i-2]



        for num in nums:

            temp = max(prev1, prev2 + num)

            prev2 = prev1

            prev1 = temp



        return prev1