def myPow(x: float, n: int) :
        m=1
        if n>0:
            for i in range(n):
                m*=x
        elif n<0:
            for i in range(n):
                m/=x
        else:
            m=1
        return m

print(myPow(2.10,-3))