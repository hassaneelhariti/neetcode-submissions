class Solution:
    def fun(self,res:List[int],i:int):
        res2=[]
        for l in res:
            res2.append(l+[i])
            res2.append(l)
        return res2
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        for i in nums:
            res=self.fun(res,i)
        return res