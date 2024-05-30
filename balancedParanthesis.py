def isValid(s):
    i=0
    c=-1
    l1=[]
    a=(len(s)%2)
    if a!=0:
        return False

    while(i!=len(s)):
        if s[i]=="(":
            l1.append("(")
            i+=1
            c+=1
        elif s[i]==")":
            i+=1
            l1.append(")")
            c+=1
            if l1[c-1]=="(":
                l1.pop(c)
                l1.pop(c-1)
                c-=2
        elif s[i]=="[":
            l1.append("[")
            i+=1
            c+=1
        elif s[i]=="]":
            i+=1
            l1.append("]")
            c+=1
            if l1[c-1]=="[" :
                l1.pop(c)
                l1.pop(c-1)
                c-=2
        elif s[i]=="{":
            l1.append("{")
            i+=1
            c+=1
        elif s[i]=="}":
            i+=1
            l1.append("}")
            c+=1
            if l1[c-1]=="{" :
                l1.pop(c)
                l1.pop(c-1)
                c-=2
                    
    if c==-1:
        return True
    else:
        return False
print(isValid("[([]])"))