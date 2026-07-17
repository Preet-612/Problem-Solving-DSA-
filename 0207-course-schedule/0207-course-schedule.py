class Solution:
    def canFinish(self, V: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*V
        adj = [[] for i in range(V)]
        for u,v in prerequisites:
            adj[v].append(u)

        for i in range(V):
            for nei in adj[i]:
                indegree[nei] += 1
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        ans = 0
        while q:
            node = q.popleft()
            ans += 1

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return ans == V
               
             

