def back(n):
    if n<1:
        return
    back(n-1)
    print(n)

n=int(input())
back(n)