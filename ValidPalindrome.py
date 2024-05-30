def validPalindrome( s: str):
        st1=s[::-1]
        if s==st1:
            return True
        else:
            c=0
            a=len(s)
            for i in range(a):
                if s[i]==st1[i]:
                    c+=1
                elif s[i]==st1[a-i-1] and st1[i]==s[a-i-1]:
                    c+=1
            if c==len(s):
                return True
            else:
                return False
print(validPalindrome("cbbcc"))
