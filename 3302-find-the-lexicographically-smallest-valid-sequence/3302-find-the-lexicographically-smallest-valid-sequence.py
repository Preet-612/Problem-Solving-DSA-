class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)

        suf = [-1] * m
        j = m - 1

        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                suf[j] = i
                j -= 1

        if j >= 0:
            suf = suf
        ans = []
        j = 0
        used = False

        for i in range(n):
            if j == m:
                break

            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            elif not used:
                if j == m - 1 or (suf[j + 1] != -1 and suf[j + 1] > i):
                    ans.append(i)
                    j += 1
                    used = True

        if j == m:
            return ans

        return []