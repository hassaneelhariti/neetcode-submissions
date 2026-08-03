class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)
        range_set =  set(list(range(len(nums)+1)))
        final = range_set-nums_set
        return list(final)[0]