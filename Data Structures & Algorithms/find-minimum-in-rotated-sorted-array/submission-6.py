class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        mini=nums[r]
        while l<=r:
            n=l+(r-l)//2
            if nums[n]>=nums[l] and nums[l]>nums[r]:
                l=n+1
            else: 
                r=n-1
            
            mini=min(mini,nums[n])

        return mini
