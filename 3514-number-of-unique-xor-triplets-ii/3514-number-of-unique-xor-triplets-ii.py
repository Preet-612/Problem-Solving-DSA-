class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        M = 2048  # 2^11, since nums[i] <= 1500 < 2048, so any xor < 2048
        
        V = set(nums)
        A = [0] * M
        for v in V:
            A[v] = 1
        
        def fwht(a, invert=False):
            n = len(a)
            h = 1
            while h < n:
                for i in range(0, n, h * 2):
                    for j in range(i, i + h):
                        x, y = a[j], a[j + h]
                        a[j] = x + y
                        a[j + h] = x - y
                h *= 2
            if invert:
                for i in range(n):
                    a[i] //= n
        
        # Transform A once, reuse for both convolutions
        Ahat = A[:]
        fwht(Ahat)
        
        # Step 1: C = A (xor-conv) A  -> pairwise xors x^y
        C = [Ahat[i] * Ahat[i] for i in range(M)]
        fwht(C, invert=True)
        B = [1 if C[i] > 0 else 0 for i in range(M)]
        
        # Step 2: D = B (xor-conv) A -> triple xors x^y^z
        Bhat = B[:]
        fwht(Bhat)
        D = [Bhat[i] * Ahat[i] for i in range(M)]
        fwht(D, invert=True)
        
        return sum(1 for i in range(M) if D[i] > 0)