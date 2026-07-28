class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        l,r=0,len(s1)-1

        count1=Counter(s1)
        count2=Counter(s2[:len(s1)])
        
        print(count1)
        if count1==count2:
                return True
        while r<len(s2)-1:
            
            r+=1
            count2[s2[r]] = count2.get(s2[r], 0) + 1
            count2[s2[l]] -= 1
            if count2[s2[l]] == 0:
                del count2[s2[l]]
            l+=1
            if count1==count2:
                return True
        return False


            
        