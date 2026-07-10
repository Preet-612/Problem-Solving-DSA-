class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        arr = sorted((nums[i], i) for i in range(n))

        # pos[original_index] = position in sorted array
        pos = [0] * n
        for i, (_, idx) in enumerate(arr):
            pos[idx] = i

        values = [x for x, _ in arr]

        # Compute farthest reachable position in one edge
        reach = [0] * n
        j = 0
        for i in range(n):
            while j + 1 < n and values[j + 1] - values[i] <= maxDiff:
                j += 1
            reach[i] = j

        # Build connected components
        comp = [0] * n
        cid = 0
        comp[0] = 0
        for i in range(1, n):
            if values[i] - values[i - 1] > maxDiff:
                cid += 1
            comp[i] = cid

        # Binary lifting
        LOG = 18
        up = [[0] * n for _ in range(LOG)]
        up[0] = reach[:]

        for k in range(1, LOG):
            for i in range(n):
                up[k][i] = up[k - 1][up[k - 1][i]]

        ans = []

        for u, v in queries:
            l = pos[u]
            r = pos[v]

            if l > r:
                l, r = r, l

            # Different connected components
            if comp[l] != comp[r]:
                ans.append(-1)
                continue

            if l == r:
                ans.append(0)
                continue

            cur = l
            steps = 0

            # Binary lifting to find minimum jumps
            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < r:
                    cur = up[k][cur]
                    steps += 1 << k

            ans.append(steps + 1)

        return ans