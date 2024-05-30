from collections import Counter
def funcDrop(x,y):
    a=Counter(x)
    b=Counter(y)
    m=max(a.values())
    n=max(b.values())
    k=max(m,n)
    return k

print(funcDrop([2,3,2,4,2],[2,2,6,5,8]))
