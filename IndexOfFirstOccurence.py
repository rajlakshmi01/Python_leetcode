def strStr(haystack, needle):
        st=haystack.replace(needle,"0")
        for i in range(len(st)):
            if st[i]=='0':
                return i
        return -1
print(strStr("hello",'ll'))