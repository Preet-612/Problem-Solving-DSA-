class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp = sorted(arr)

        rank = {}
        r = 1

        for num in temp:
            if num not in rank:
                rank[num] = r
                r += 1

        res = []

        for num in arr:
            res.append(rank[num])

        return res