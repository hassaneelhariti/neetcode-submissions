
import string
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        l,r=0,0
        count = dict.fromkeys(string.ascii_uppercase, 0)
        while r<len(s):
            count[s[r]]+=1
            if r-l+1-max(count.values())<=k :
                
                
                res=max(res,r-l+1)
                
            else:
                count[s[l]]-=1
                l+=1
            r+=1
        return res
            
