class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        # Continue until one or no stones remain
        while len(stones) > 1:
            y = -heapq.heappop(stones)  # heaviest
            x = -heapq.heappop(stones)  # second heaviest

            # If they are not equal, push the difference
            if y != x:
                heapq.heappush(stones, -(y - x))

        # Return remaining stone or 0
        return -stones[0] if stones else 0