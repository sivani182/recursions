def firstrepeat(digitPattern):
    d={}
    t=str(digitPattern)
    l=list(t)
    for i in l:
        if i in d:
            return i
        d[i]=1
    return -1
n=int(input())
print(firstrepeat(n))