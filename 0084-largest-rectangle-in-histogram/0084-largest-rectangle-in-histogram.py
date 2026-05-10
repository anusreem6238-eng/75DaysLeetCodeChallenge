class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []   # stores indices
        max_area = 0
        
        # Add a zero height to process remaining bars
        heights.append(0)
        
        for i in range(len(heights)):
            
            # If current bar is smaller, calculate area
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                
                # Width calculation
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                
                max_area = max(max_area, h * width)
            
            stack.append(i)
        
        return max_area
