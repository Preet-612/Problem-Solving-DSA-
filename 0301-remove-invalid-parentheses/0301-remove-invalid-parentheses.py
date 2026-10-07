from collections import deque

class Solution:
    def removeInvalidParentheses(self, s):
        def valid(x):
            count = 0

            for ch in x:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        q = deque([s])
        visited = {s}
        ans = []

        while q:
            size = len(q)
            found = False

            for _ in range(size):
                curr = q.popleft()

                if valid(curr):
                    ans.append(curr)
                    found = True

                if found:
                    continue

                for i in range(len(curr)):
                    if curr[i] not in '()':
                        continue

                    nxt = curr[:i] + curr[i + 1:]

                    if nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)

            if found:
                return ans

        return [""]