def generate(numRows):
        l2=[]
        for i in range(numRows-1):
            l1=[]
            l1.append(1)
            for j in range(0,i):
                l1.append(l2[i-1][j]+l2[i-1][j+1])
            l1.append(1)
            l2.append(l1)
        l2.insert(0,[1])
        return l2

print(generate(5))