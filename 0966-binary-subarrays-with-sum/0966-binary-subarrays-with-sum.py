class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ''' #bruteforce solution 
        count=0
        for i in range(len(nums)):
             sum=0
             for j in range(i,len(nums)):
                sum+=nums[j]
                if sum == goal:
                    count+=1
        return count '''

        count=0
        prefix_sum=0
        freq={0:1}
        for i in range (len(nums)):
            prefix_sum+=nums[i]
            count+=freq.get(prefix_sum-goal,0)
            freq[prefix_sum]=freq.get(prefix_sum,0)+1
        return count
            
        

        