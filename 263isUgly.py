import math
def isUgly(n):
        if n<0:
            n*=-1
        a=[1,2,3,5]
        l=[]
        l2=[]
        k=n
        if k<=5 and k in a:
            return True
        else:
            for i in (a[1:]):
                if k%i==0:
                    while(k%i==0 and k>0):
                        if i not in l:
                            l.append(i)
                        k=k//i
                        if k==1:
                            return True
                if i ==a[-1] and k%i!=0:
                    return False
                else:
                    continue
        if (len(l)>0 and (set(l).issubset(set(a)))):
            return True
        else:
            return False

print(isUgly(14))
