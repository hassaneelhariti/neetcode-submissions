class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        strs=""
        for i in range(len(s)):
            if ord(s[i])>=65 and ord(s[i])<=90:
                strs+=s[i].lower()
            elif ord(s[i])>=97 and ord(s[i])<=122:
                strs+=s[i]
            elif ord(s[i])>=48 and ord(s[i])<=57:
                strs+=s[i]
        if strs==strs[::-1]:
            return True
        else:
            return False