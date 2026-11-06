class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda a: a[1])

        arr = sorted([(q, i) for i, q in enumerate(queries)])

        cnt = {}
        ans = [0] * len(queries)

        left = 0
        right = 0
        active = 0

        for q, idx in arr:
            start = q - x

            while right < len(logs) and logs[right][1] <= q:
                s = logs[right][0]

                cnt[s] = cnt.get(s, 0) + 1

                if cnt[s] == 1:
                    active += 1

                right += 1

            while left < right and logs[left][1] < start:
                s = logs[left][0]

                cnt[s] -= 1

                if cnt[s] == 0:
                    active -= 1

                left += 1

            ans[idx] = n - active

        return ans