from typing import List
from collections import defaultdict

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node[WORD_KEY] = word

        def dfs(i: int, j: int, parent: dict) -> None:
            letter = board[i][j]
            currNode = parent[letter]
            
            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                found_words.append(word_match)
            
            board[i][j] = '#'
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] in currNode:
                    dfs(ni, nj, currNode)
            board[i][j] = letter
            
            if not currNode:
                parent.pop(letter)

        m, n = len(board), len(board[0])
        found_words = []
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(i, j, trie)
        
        return found_words