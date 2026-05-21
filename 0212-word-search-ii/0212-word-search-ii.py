class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # Trie Node
        trie = {}

        # Build Trie
        for word in words:
            node = trie
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node["#"] = word   # End of word marker

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            ch = board[r][c]

            if ch not in node:
                return

            nxt = node[ch]

            # Found a word
            word = nxt.pop("#", False)
            if word:
                result.append(word)

            # Mark visited
            board[r][c] = "*"

            # Explore 4 directions
            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < rows and
                    0 <= nc < cols and
                    board[nr][nc] != "*"):
                    dfs(nr, nc, nxt)

            # Restore cell
            board[r][c] = ch

            # Optional optimization: remove empty trie nodes
            if not nxt:
                node.pop(ch)

        # Start DFS from every cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie)

        return result