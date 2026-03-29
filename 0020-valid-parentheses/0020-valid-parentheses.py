class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for char in s:
            if char in mapping:
                # If stack is empty or top doesn't match
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0