class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic={}
        maxl=0
        l,r=0,0
        while r<=len(s)-1:
            if s[r] not in dic:
                dic[s[r]]=1
                r+=1
                maxl=max(maxl,r-l)
            else:
                
                del dic[s[l]]
                l+=1
        return maxl