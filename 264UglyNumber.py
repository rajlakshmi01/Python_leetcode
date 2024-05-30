def nthUglyNumber(n):
        a=0
        c=0
        l=[1]
        for i in range(2,n+1):
            if i%2==0:
                if i not in l:
                    l.append(i)
            if i%2==0 and i%3==0:
                if i not in l:
                    l.append(i)
            if i%2==0 and i%5==0:
                if i not in l:
                    l.append(i)
            if 
                            

print(nthUglyNumber(10))