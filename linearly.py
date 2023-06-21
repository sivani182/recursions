c=0
def func(n):
    global c
    if c==n:
        return
    c+=1
    print(c)
    func(n)

n=int(input())
func(n)