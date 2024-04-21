
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        adj_list = defaultdict(list)        

        for node1, node2 in edges:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)


        visited = set()
        def dfs(node):
            if node == destination:
                return True
            
            if node not in visited:
                visited.add(node)

                for neighbor in adj_list[node]:
                    result = dfs(neighbor)

                    if result:
                        return True

        return dfs(source)

