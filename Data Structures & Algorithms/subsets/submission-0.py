class Solution:
    def fun(self,i: int , res: List[int]):
        res2=[]
        for l in res:
            res2.append(l+[i])
            res2.append(l)
        return res2
        res.append()
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        for i in nums:
            res=self.fun(i,res)
        return res