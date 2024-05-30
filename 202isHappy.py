def isHappy(n):
    sum1=0
    while(n>0):
        a=n%10
        sum1+=pow(a,2)
        n=n//10
    if sum1==1:
        n=0
        return True
    else:
        n=sum1
        return isHappy(n)
        
print(isHappy(12))