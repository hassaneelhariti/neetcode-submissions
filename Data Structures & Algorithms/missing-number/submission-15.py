class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        t1=0
        for i in nums:
            t1^=i
        t2=0
        for j in range(len(nums)+1):
            t2^=j
        print(t2)
        return t1^t2