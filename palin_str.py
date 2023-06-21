def func(i,n,s):
    if i>=n/2:
        return True
    elif s[i]!=s[n-i-1]:
        return False
    return func(i+1,n,s)

a=input()
n=len(a)
print(func(0,n,a))
