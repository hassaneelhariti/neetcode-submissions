class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=[]
        maxi=[]
        for i in range(len(s)):
            print(res)
            if s[i] not in res :
                res.append(s[i])
                
            else:
                maxi.append(len(res))
                res=res[res.index(s[i])+1:]
                print(res)
                res.append(s[i])
        maxi.append(len(res))
        return max(maxi)
