class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for indx,i in enumerate(nums):
            if target - i in nums and indx !=nums.index(target - i ):
                return sorted([nums.index(target - i ),indx])
            else :
                continue