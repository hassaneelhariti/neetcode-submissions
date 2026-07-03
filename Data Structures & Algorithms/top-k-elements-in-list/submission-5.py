class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        sorted_dict_dsc = sorted(c.items(), key=lambda item: item[1],reverse=True)
        return [item[0] for item in sorted_dict_dsc[:k]]
