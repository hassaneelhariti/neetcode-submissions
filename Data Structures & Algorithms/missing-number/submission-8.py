class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res1=0
        for i in nums:
            res1^=i
        res2=0
        for i in range(len(nums)+1):
            res2^=i
        
        return res1^res2