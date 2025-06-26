class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2

            if nums[mid]==target:
                return True
            if nums[left]==nums[mid] and nums[right]==nums[mid]:
                left+=1
                right-=1
                continue

            if nums[left]<=nums[mid]:
                if nums[left]<=target and target <=nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            if nums[mid]<=nums[right]:
                if nums[mid]<=target and target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        return False


        