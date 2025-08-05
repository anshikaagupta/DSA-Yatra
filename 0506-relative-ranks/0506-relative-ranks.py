class Solution:
    def findRelativeRanks(self, scores: List[int]) -> List[str]:
        heap=[-s for s in scores]
        heapq.heapify(heap)
        ans=[]
        rank={}
        r=0
        for _ in scores:
            r+=1
            rank[heapq.heappop(heap)]=r
        for x in scores:
            if rank[-x]==1:
                ans.append("Gold Medal")
            elif rank[-x]==2:
                ans.append("Silver Medal")
            elif rank[-x]==3:
                ans.append("Bronze Medal")
            else:
                ans.append(str(rank[-x]))
        return ans
        