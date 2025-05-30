class Solution:
    def shortestPaths(self, edges: List[int], src: int) -> List[int]:
        n = len(edges)
        dist = [float('inf')] * n
        dist[src] = 0
        q = deque()
        q.append((src, 0))

        while q:
            node, d = q.popleft()
            if edges[node] != -1 and dist[edges[node]] > d + 1:
                dist[edges[node]] = d + 1
                q.append((edges[node], dist[edges[node]]))
        return dist

    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        Spath1 = self.shortestPaths(edges, node1)
        Spath2 = self.shortestPaths(edges, node2)

        ansNode = -1
        preMax = float('inf')

        for i in range(len(edges)):
            pMax = max(Spath1[i], Spath2[i])
            if Spath1[i] != float('inf') and Spath2[i] != float('inf') and pMax < preMax:
                preMax = pMax
                ansNode = i

        return ansNode