class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = [(num, idx) for idx, num in enumerate(nums)]
        

        num.sort(key=lambda x:x[0])
        n=len(nums)
        
        left,right=0,n-1
        while left<right:
            cursum=num[left][0]+num[right][0]
            if cursum==target:
                return [num[left][1], num[right][1]]

            elif cursum<target: 
                left+=1
            else:
                right-=1
        return [-1,-1]