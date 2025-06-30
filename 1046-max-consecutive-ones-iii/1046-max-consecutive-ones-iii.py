class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        left=0
        maxans=0
        zeros=0
        if len(nums)==0:
            return 0
        for right in range(left,len(nums)):
            if nums[right]==0:
                zeros+=1
            while zeros>k:
                if nums[left]==0:
                    zeros-=1
                left+=1
            maxans=max(maxans,right-left+1)
        return maxans