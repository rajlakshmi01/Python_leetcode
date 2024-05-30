from collections import Counter
def firstNonrepeat(str):
    a=Counter(str)
    for item in a:
        b=a.get(item)
        if b==1:
            return item
            break
        else:
            continue

print(firstNonrepeat("geeksforgeeks"))
 