class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pr=1
        zero=nums.count(0)
        for i in nums:
            if i!=0:
                pr=pr*i
        
        res=[]
        for i in nums:
            if zero==0:
                res.append(pr//i)
            elif zero==1:
                if i==0 :
                    res.append(pr)
                else:
                    res.append(0)
            else :
                res=[0 for i in nums]
        return res
