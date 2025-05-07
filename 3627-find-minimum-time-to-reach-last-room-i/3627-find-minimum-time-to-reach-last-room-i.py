class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime) - 1, len(moveTime[0]) - 1
        min_heap = [(0, 0, 0)] # sec, n, m
        visited = set()

        while min_heap:
            cur_sec, cur_n, cur_m = heappop(min_heap)
            if (cur_n, cur_m) in visited:
                continue
            if cur_n == n and cur_m == m:
                return cur_sec
            moveTime[cur_n][cur_m] = cur_sec
            visited.add((cur_n, cur_m))
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_n, new_m = cur_n + x, cur_m + y
                if 0 <= new_n <= n and 0 <= new_m <= m:
                    heappush(min_heap, (max(cur_sec + 1, moveTime[new_n][new_m] + 1), new_n, new_m))