def addBinary(a: str, b: str):
        m=0
        n=0
        j=0
        l1=[]
        st=''
        p=len(a)
        q=len(b)
        for i in range(len(a)):
            m+=pow(2,p-1)*int(a[i])
            p-=1
            if p==0:
                break
        for i in range(len(b)):
            n+=pow(2,q-1)*int(b[i])
            q-=1
            if q==0:
                break
        k=m+n
        while(k>=1):
            j=k%2
            l1.append(j)
            k=k//2
            
        l2=l1[::-1]
        for item in l2:
            st+=str(item)
        return st

print(addBinary("1010","1011"))