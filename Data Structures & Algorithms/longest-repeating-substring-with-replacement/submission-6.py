class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r=0,0
        count={}
        res=0
        
        while r<len(s):
            count[s[r]]=count.get(s[r],0)+1
            if r-l+1-max(count.values())<=k:
                res=max(res,r-l+1)
                r=r+1

            else:
                count[s[l]]=count[s[l]]-1
                
                l=l+1
                r=r+1
               
        print(count)
        return res