def intToRoman(num):
    l1=['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
    l2=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
    st=''
    while(num>0):
        for item in l2[::-1]:
            if num//item!=0:
                a=num//item
                b=l2.index(item)
                k=l1[b]*a
                st+=k
                num-=num*a
        return st

print(intToRoman(25))