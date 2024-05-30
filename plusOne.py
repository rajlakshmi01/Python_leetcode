def plusOne(digits):
    n=digits[-1]
    a=len(digits)-1
    b=len(digits)
    c=0
    if n!=9:
        digits[a]=n+1
    else:
        while(a>=0):
            if digits[a]==9:
                digits.pop(a)
                c+=1
                a-=1
            else:
                break
        if len(digits)>0:
            digits[len(digits)-1]+=1
            while(c>0):
                digits.append(0)
                c-=1
        else:
            digits.append(1)
            while(c>0):
                digits.append(0)
                c-=1
    return digits
print(plusOne([9,8,9]))