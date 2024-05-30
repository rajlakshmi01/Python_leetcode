def removeStars(s):
        st=''
        for item in s:
            if item!="*":
                st+=item
            else:
                st=st[:-1]
        return st
print(removeStars("leet**cod*e"))