class Solution:
    def maximumLength(self, a: List[int], k: int) -> int:
        dp = [[0]*k for _ in range(k)]
        for v,q in product(a,range(k)):
            dp[q][v%k] = dp[v%k][q]+1

        return max(chain(*dp))