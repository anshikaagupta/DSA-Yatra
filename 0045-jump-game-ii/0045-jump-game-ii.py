class Solution:
    def jump(self, nums: List[int]) -> int:
        max_index=0
        curr=0
        jumps=0
        for i in range(len(nums)-1):
            max_index=max(max_index, i+nums[i])
            if i==curr:
                jumps+=1
                curr=max_index

            
        return jumps
        
        