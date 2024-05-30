def compressWord(word, k):
    l1=[]
    for i in range(len(word)):
        l1.append(word[i])
        n=len(l1)

    
    while(n>0):
        if  k in range(n):
            if l1[k]==l1[k-1]==l1[k+1]:
                l1.pop(k)
                l1.pop(k-1)
                n-=3
            elif l1[k-1]  
            elif l1[k]==l1[k-1]:
                l1.pop(k)
                l1.pop(k-1)
                n=-2
            elif l1[k]==l1[k+1]:
                l1.pop(k)
                l1.pop(k+1)
    for item in l1:
        st+=item
    return st

print(compressWord('abbcccb',3))



