def repeatedSubstringPattern(s):
    if len(s)>3 and len(s)%2==0:
        a=len(s)//2
        if s[:a]==s[a:]:
            return True
    elif len(s)<=1:
        return False
    else:
        c=0
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                c+=0
        if c==len(s)-1:
            return True
    return False

print(repeatedSubstringPattern("bb"))
