class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        visited = set()

        def dfs(city):
            for i in range(len(isConnected[city])):
                if i not in visited and isConnected[city][i] == 1:
                    visited.add(i)
                    dfs(i)

        for i in range(len(isConnected)):
            if i not in visited:
                provinces += 1
                visited.add(i)
                dfs(i)

        return provinces