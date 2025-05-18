class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        mod = 10 ** 9 + 7
        state = []

        def DFS(pos, prev_color, mask):
            if pos == m:
                state.append(mask)
                return
            for color in range(3):
                if color != prev_color:
                    DFS(pos + 1, color, mask * 3 + color)
            
        DFS(0, -1, 0)
        s = len(state)
        matrix = [[] for _ in range(s)]
        for i, v1 in enumerate(state):
            for j, v2 in enumerate(state):
                x, y = v1, v2
                valid = True
                for _ in range(m):
                    if x % 3 == y % 3:
                        valid = False
                        break
                    x //= 3
                    y //= 3
                if valid:
                    matrix[i].append(j)
        dp = [1] * s
        for _ in range(n - 1):
            new_dp = [0] * s
            for i in range(s):
                if dp[i]:
                    for j in matrix[i]:
                        new_dp[j] = (new_dp[j] + dp[i]) % mod
            dp = new_dp
        return sum(dp) % mod