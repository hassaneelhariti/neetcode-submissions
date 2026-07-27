class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res,res2=0,0
        nums.sort()
        for i in nums:
            res^=i
        for i in range(len(nums)+1):
            res2^=i
        print(f"res1={res} res2={res2}")
        return res^res2