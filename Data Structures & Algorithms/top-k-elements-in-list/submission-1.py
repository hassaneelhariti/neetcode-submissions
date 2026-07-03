class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictio={}
        dictio={n: nums.count(n) for n in nums}
        
        
        return sorted(dictio, key=dictio.get, reverse=True)[:k]
        