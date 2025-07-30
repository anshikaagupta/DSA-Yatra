import heapq
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        heapq.heapify(nums) # first to make min heap
        round=0
        while nums:
            k=heapq.heappop(nums)
            if k==0:
                continue
            round+=1
            for i in range(len(nums)):
                nums[i]-=k
            heapq.heapify(nums)
        return round
            
        
        