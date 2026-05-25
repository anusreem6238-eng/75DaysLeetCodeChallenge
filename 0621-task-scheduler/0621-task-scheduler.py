class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        freq = [0] * 26
        
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        
        # Maximum frequency
        max_freq = max(freq)
        
        # Count how many tasks have maximum frequency
        max_count = freq.count(max_freq)
        
        # Calculate minimum intervals needed
        intervals = (max_freq - 1) * (n + 1) + max_count
        
        # Result is maximum of total tasks or calculated intervals
        return max(len(tasks), intervals)