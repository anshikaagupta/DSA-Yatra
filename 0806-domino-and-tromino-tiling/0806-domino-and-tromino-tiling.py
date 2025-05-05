class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10**9 + 7
        
        def mul(a, b):
            x = [[0] * 4 for _ in range(4)]
            for i in range(4):
                for j in range(4):
                    if a[i][j]:
                        for k in range(4):
                            if b[j][k]:
                                x[i][k] = (x[i][k] + a[i][j] * b[j][k] % mod) % mod
            return x
        
        mat = [
            [0, 1, 0, 1],
            [1, 1, 0, 1],
            [0, 2, 0, 1],
            [0, 0, 1, 0]
        ]
        ans = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
        
        while n > 0:
            if n & 1:
                ans = mul(ans, mat)
            mat = mul(mat, mat)
            n >>= 1
        
        return ans[1][1]