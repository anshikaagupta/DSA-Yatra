class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        n=len(nums)
        right=n-1
        
        while (left<=right):
            mid = (right+left)//2
            if(nums[mid]==target):
                return mid
            if (nums[mid]>target):
                right=mid-1
            else:
                left=mid+1
        return left
        