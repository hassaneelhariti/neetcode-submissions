class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dics={}
        dictt={}
        for i in s:
            if i in dics: dics[i]+=1
            else : dics[i]=1
        
        for i in t:
            if i in dictt: dictt[i]+=1
            else : dictt[i]=1
         
        return dics==dictt