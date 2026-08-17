class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]

        # Pointer/running-best for "left side <= right side" contribution, fixed i
        ptrA = list(range(n))
        bestA = [0] * n
        haveA = [False] * n

        # Pointer/running-best for "right side < left side" contribution, fixed j
        ptrB = list(range(n))
        bestB = [0] * n
        haveB = [False] * n

        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                total = pre[j + 1] - pre[i]

                # Advance left pointer (fixed i): totals grow monotonically with j,
                # so valid k's (where 2*sum(i,k) <= total) only accumulate.
                while ptrA[i] < j and 2 * (pre[ptrA[i] + 1] - pre[i]) <= total:
                    cand = dp[i][ptrA[i]] + (pre[ptrA[i] + 1] - pre[i])
                    if not haveA[i] or cand > bestA[i]:
                        bestA[i] = cand
                        haveA[i] = True
                    ptrA[i] += 1

                # Advance right pointer (fixed j), symmetric logic sweeping i leftward.
                while ptrB[j] > i and 2 * (pre[j + 1] - pre[ptrB[j]]) < total:
                    cand = dp[ptrB[j]][j] + (pre[j + 1] - pre[ptrB[j]])
                    if not haveB[j] or cand > bestB[j]:
                        bestB[j] = cand
                        haveB[j] = True
                    ptrB[j] -= 1

                best = 0
                if haveA[i]:
                    best = max(best, bestA[i])
                if haveB[j]:
                    best = max(best, bestB[j])

                # Explicitly check exact-equality split near the pointer boundary
                for k in (ptrA[i] - 1, ptrA[i]):
                    if i <= k < j:
                        left = pre[k + 1] - pre[i]
                        right = total - left
                        if left == right:
                            best = max(best, max(dp[i][k], dp[k + 1][j]) + left)

                dp[i][j] = best

        return dp[0][n - 1]

