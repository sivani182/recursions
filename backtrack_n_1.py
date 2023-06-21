def back(i,n):
    if i>n:
        return
    back(i+1,n)
    print(i)

n=int(input())
back(1,n)