class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        trust_score = [0] * (n + 1)

        for a, b in trust:
            trust_score[a] -= 1
            trust_score[b] += 1

        # Judge should have score n-1
        for i in range(1, n + 1):
            if trust_score[i] == n - 1:
                return i

        return -1