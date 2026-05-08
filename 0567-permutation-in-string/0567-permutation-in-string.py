class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False

        need = [0] * 26
        window = [0] * 26

        # Count characters in s1
        for ch in s1:
            need[ord(ch) - ord('a')] += 1

        left = 0

        for right in range(len(s2)):
            # Add current character to window
            window[ord(s2[right]) - ord('a')] += 1

            # Keep window size equal to len(s1)
            if right - left + 1 > len(s1):
                window[ord(s2[left]) - ord('a')] -= 1
                left += 1

            # Compare frequency arrays
            if window == need:
                return True

        return False