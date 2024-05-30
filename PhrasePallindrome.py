def isPalindrome(s: str):
    st=''
    l1=s.split(' ')
    for i in range(len(l1)):
        for j in range(len(l1[i])):
            if l1[i][j].isalpha():
                st+=l1[i][j].lower()
    st1=st[::-1]
    if st1==st:
        return True
    else:
        return False

print(isPalindrome("0P"))
