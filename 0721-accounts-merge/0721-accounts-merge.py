class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)

        if pa == pb:
            return

        if self.rank[pa] < self.rank[pb]:
            self.parent[pa] = pb
        elif self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
        else:
            self.parent[pb] = pa
            self.rank[pa] += 1


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        n = len(accounts)
        dsu = DSU(n)

        email_to_index = {}

        # Merge account indices
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_index:
                    dsu.union(i, email_to_index[email])
                else:
                    email_to_index[email] = i

        # parent -> set(emails)
        groups = {}

        for email, idx in email_to_index.items():
            parent = dsu.find(idx)

            if parent not in groups:
                groups[parent] = set()

            groups[parent].add(email)

        ans = []

        for parent, emails in groups.items():
            ans.append([accounts[parent][0]] + sorted(emails))

        return ans
# class Solution:
#     def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        