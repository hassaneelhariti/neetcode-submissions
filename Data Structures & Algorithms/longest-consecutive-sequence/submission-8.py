class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0  : return 0
        li=list(set(nums))
        li.sort()
        i=0
        a=li[i]
        res=0
        resli=[]
        while i<len(li) :
            
            if a == li[i]:
                res+=1
                a+=1
                i+=1
            else:
                
                a=li[i]
                res=0
            resli.append(res)
        return max(resli)
        