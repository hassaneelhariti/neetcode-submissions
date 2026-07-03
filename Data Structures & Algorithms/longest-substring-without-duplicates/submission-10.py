class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        r=1
        l=0
        my_set=set()
        my_set.add(s[l])
        max_len = 1
        while r<len(s):
            length=len(my_set)
            if s[r] in my_set:
                my_set.remove(s[l])
                l+=1
            else:
                my_set.add(s[r])
                r+=1
                max_len = max(max_len, len(my_set))
        return max_len
        