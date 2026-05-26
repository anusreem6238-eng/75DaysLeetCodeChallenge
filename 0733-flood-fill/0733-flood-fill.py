class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        rows, cols = len(image), len(image[0])
        original = image[sr][sc]

        # If the color is already the same, no need to process
        if original == color:
            return image

        def dfs(r, c):
            # Check boundaries
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            # Only fill cells with the original color
            if image[r][c] != original:
                return

            # Change color
            image[r][c] = color

            # Visit neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)

        return image