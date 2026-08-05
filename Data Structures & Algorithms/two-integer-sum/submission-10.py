class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            if target-num in nums and i!=nums.index(target-num):
                return sorted([i,nums.index(target-num)])
            else: 
                continue
