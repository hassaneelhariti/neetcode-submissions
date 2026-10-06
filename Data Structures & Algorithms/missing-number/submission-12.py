class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numset=set(nums)

        rangeset=set(list(range(len(nums)+1)))

        final=rangeset-numset
        return list(final)[0]