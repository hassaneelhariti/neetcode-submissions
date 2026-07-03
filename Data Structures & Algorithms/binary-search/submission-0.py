from math import floor
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        mid=floor(len(nums)/2)
        if nums[mid]==target :
            return mid
        elif nums[mid]<target:
            result=self.search(nums[mid+1:],target)
            return result+mid+1 if result !=-1 else -1
        else :
            return self.search(nums[:mid], target)