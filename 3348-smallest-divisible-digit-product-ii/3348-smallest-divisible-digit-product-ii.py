class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        need = [0, 0, 0, 0]

        for i, p in enumerate([2, 3, 5, 7]):
            while t % p == 0:
                need[i] += 1
                t //= p

        if t != 1:
            return "-1"

        factors = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [2, 0, 0, 0],
            [0, 0, 1, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 1],
            [3, 0, 0, 0],
            [0, 2, 0, 0]
        ]

        a, b = need[0], need[1]
        INF = 10**9

        dp = [[INF] * (b + 1) for _ in range(a + 1)]
        dp[0][0] = 0

        for x in range(a + 1):
            for y in range(b + 1):
                if x == 0 and y == 0:
                    continue

                for d in [2, 3, 4, 6, 8, 9]:
                    na = max(0, x - factors[d][0])
                    nb = max(0, y - factors[d][1])
                    dp[x][y] = min(dp[x][y], dp[na][nb] + 1)

        def min_digits(req):
            return dp[req[0]][req[1]] + req[2] + req[3]

        def possible(req, length):
            return min_digits(req) <= length

        def build(req, length):
            ans = []

            for _ in range(length):
                remaining = length - len(ans) - 1

                for d in range(1, 10):
                    f = factors[d]

                    new_req = [
                        max(0, req[0] - f[0]),
                        max(0, req[1] - f[1]),
                        max(0, req[2] - f[2]),
                        max(0, req[3] - f[3])
                    ]

                    if possible(new_req, remaining):
                        ans.append(str(d))
                        req = new_req
                        break

            return ''.join(ans)

        n = len(num)

        prefix = [[0] * 4 for _ in range(n + 1)]
        valid_prefix = [True] * (n + 1)

        for i in range(n):
            d = int(num[i])

            for j in range(4):
                prefix[i + 1][j] = prefix[i][j] + factors[d][j]

            valid_prefix[i + 1] = valid_prefix[i] and d != 0

        if valid_prefix[n]:
            ok = True

            for j in range(4):
                if prefix[n][j] < need[j]:
                    ok = False
                    break

            if ok:
                return num

        for i in range(n - 1, -1, -1):
            if not valid_prefix[i]:
                continue

            cur = int(num[i])

            for d in range(cur + 1, 10):
                f = factors[d]

                have = [
                    prefix[i][0] + f[0],
                    prefix[i][1] + f[1],
                    prefix[i][2] + f[2],
                    prefix[i][3] + f[3]
                ]

                req = [
                    max(0, need[0] - have[0]),
                    max(0, need[1] - have[1]),
                    max(0, need[2] - have[2]),
                    max(0, need[3] - have[3])
                ]

                length = n - i - 1

                if possible(req, length):
                    return num[:i] + str(d) + build(req, length)

        length = max(n + 1, min_digits(need))

        return build(need[:], length)