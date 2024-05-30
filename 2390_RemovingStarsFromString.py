def removeStars(s):
        st=''
        l1=[]
        l2=[]
        for item in s:
            l1.append(item)
        for i in range(len(l1)):
            if l1[i]=="*":
                l2.pop(len(l2)-1)
            else:
                l2.append(l1[i])
        for item in l2:
            st+=item
        return st
                

print(removeStars("leet**cod*e"))