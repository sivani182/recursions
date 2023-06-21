
def isPowerOfTwo(n):
    # Write your code here
    a=2
    cnt=0
    t=0
    for i in range(0,32):
        t=a<<i
        print(t)
        if t==n:
            cnt=1
            return True
        elif t>a:
            break
    if cnt==0:
        return False
n=int(input())
print(isPowerOfTwo(n))