class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
 
        ln = len(colors)

        indegree = [0] * ln

        # make graph from edges

        graph = defaultdict(list)

        for s, d in edges:

            # if cycle return -1

            if s==d:

                return -1

            graph[s].append(d)

            # Calculate indegree of each vertex

            indegree[d]+=1


        # add nodes  with indegree == 0

        dq = deque([node for node, degree in enumerate(indegree) if degree == 0])

        # dict of dict for saving counts of colors

        topo = defaultdict(lambda: defaultdict(int))

        # dict for saving max counts of collors

        res = defaultdict(int)

        # Kahn's Algorithm for Topological Sorting

        while dq:

            for _ in range(len(dq)):

                node = dq.popleft()

                # add color of node

                topo[node][colors[node]]+=1

                # search for maximum count 

                for color, val in topo[node].items():

                    res[color] = max(res[color], val)

                for next_node in graph[node]:

                    for color, val in topo[node].items():



                        topo[next_node][color] = max(topo[next_node][color], val)

                    indegree[next_node] -=1

                    if indegree[next_node] == 0:

                        dq.append(next_node)

        # if lenghts not equal than grap has cycle

        if len(topo) != ln:

            return -1


        return max(res.values())





               