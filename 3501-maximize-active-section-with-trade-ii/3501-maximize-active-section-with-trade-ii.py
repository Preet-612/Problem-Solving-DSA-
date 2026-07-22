from dataclasses import dataclass
from itertools import pairwise


@dataclass
class Group:
    start: int
    length: int


class SparseTable:
    def __init__(self, nums):
        self.n = len(nums)
        self.st = [[0] * max(1, self.n) for _ in range(self.n.bit_length() + 1)]

        if self.n == 0:
            return

        self.st[0] = nums[:]

        for k in range(1, self.n.bit_length() + 1):
            length = 1 << k
            half = length >> 1
            for i in range(self.n - length + 1):
                self.st[k][i] = max(
                    self.st[k - 1][i],
                    self.st[k - 1][i + half]
                )

    def query(self, l, r):
        if l > r:
            return 0
        k = (r - l + 1).bit_length() - 1
        return max(
            self.st[k][l],
            self.st[k][r - (1 << k) + 1]
        )


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: list[list[int]]) -> list[int]:
        ones = s.count("1")

        zeroGroups, zeroGroupIndex = self.getZeroGroups(s)

        if not zeroGroups:
            return [ones] * len(queries)

        merge = self.getZeroMergeLengths(zeroGroups)
        st = SparseTable(merge)

        ans = []

        for l, r in queries:

            left = (
                -1
                if zeroGroupIndex[l] == -1
                else zeroGroups[zeroGroupIndex[l]].length
                - (l - zeroGroups[zeroGroupIndex[l]].start)
            )

            right = (
                -1
                if zeroGroupIndex[r] == -1
                else r - zeroGroups[zeroGroupIndex[r]].start + 1
            )

            start = zeroGroupIndex[l] + 1
            end = zeroGroupIndex[r] if s[r] == "1" else zeroGroupIndex[r] - 1

            best = ones

            if (
                s[l] == "0"
                and s[r] == "0"
                and zeroGroupIndex[l] + 1 == zeroGroupIndex[r]
            ):
                best = max(best, ones + left + right)

            elif start <= end - 1:
                best = max(best, ones + st.query(start, end - 1))

            if (
                s[l] == "0"
                and zeroGroupIndex[l] + 1
                <= (zeroGroupIndex[r] if s[r] == "1" else zeroGroupIndex[r] - 1)
            ):
                best = max(
                    best,
                    ones
                    + left
                    + zeroGroups[zeroGroupIndex[l] + 1].length,
                )

            if (
                s[r] == "0"
                and zeroGroupIndex[l] < zeroGroupIndex[r] - 1
            ):
                best = max(
                    best,
                    ones
                    + right
                    + zeroGroups[zeroGroupIndex[r] - 1].length,
                )

            ans.append(best)

        return ans

    def getZeroGroups(self, s):
        groups = []
        idx = []

        for i, ch in enumerate(s):
            if ch == "0":
                if i > 0 and s[i - 1] == "0":
                    groups[-1].length += 1
                else:
                    groups.append(Group(i, 1))
            idx.append(len(groups) - 1)

        return groups, idx

    def getZeroMergeLengths(self, groups):
        return [a.length + b.length for a, b in pairwise(groups)]