class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[-1*x for x in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            first=heapq.heappop(heap)
            second=heapq.heappop(heap)  
            if first != second:
                heapq.heappush(heap, first-second)
        if len(heap)==0:
            return 0
        return  -1*heap[0]  