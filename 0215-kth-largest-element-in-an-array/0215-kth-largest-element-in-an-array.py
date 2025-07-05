import heapq
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq=[]
        n=len(nums)
        for i in nums:
            heapq.heappush(pq, -i)
        for _ in range (k-1):
            heapq.heappop(pq)
        return -pq[0]

       