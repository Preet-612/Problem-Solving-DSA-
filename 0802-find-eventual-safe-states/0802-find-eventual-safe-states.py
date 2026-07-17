class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        n = len(graph)
        visited = [False]*n
        pathvis = [False]*n
        check = [0]*n

        def dfs(node):
            visited[node] = True
            pathvis[node] = True
            # check[node] = 0
            for nei in graph[node]:
                if not visited[nei]:
                    if dfs(nei):
                        return True
                elif pathvis[nei]:
                    return True
            pathvis[node] = False
            check[node] = 1
            return False

        
        for i in range(n):
            if not visited[i]:
                dfs(i)
        ans = []          
        for i in range(n):
            if check[i] == 1:
                ans.append(i)
        return ans
