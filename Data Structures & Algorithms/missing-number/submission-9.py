class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res1=0
        res2=0
        for i in range(len(nums)+1):
            res1^=i
        for i in nums:
            res2^=i
        return res1^res2