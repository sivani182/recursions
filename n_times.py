
def func(c,n):
    if n<=0:
        
        return 
    c+=1
    func(c,n-1)
    print(n)

n=int(input())
c=0
func(c,n)