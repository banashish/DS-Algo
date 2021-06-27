class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        count = Counter(word)
        m, n = len(board), len(board[0])

        start = []

        for i in range(m):
            for j in range(n):
                count[board[i][j]] -= 1
                if board[i][j] == word[0]:
                    start.append((i, j))

        if max(count.values()) > 0:
            return False

        for i, j in start:
            ans = self.traverse(i, j, word, board, 0)
            if ans:
                return True
        else:
            return False

    def traverse(self, i, j, word, board, d):
        if d == len(word):
            return True

        if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == word[d]:
            board[i][j], temp = "", board[i][j]
            if self.traverse(i+1, j, word, board, d+1):
                return True
            if self.traverse(i, j+1, word, board, d+1):
                return True
            if self.traverse(i-1, j, word, board, d+1):
                return True
            if self.traverse(i, j-1, word, board, d+1):
                return True
            board[i][j] = temp
