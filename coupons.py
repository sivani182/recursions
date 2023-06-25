#sivani is good girl and praveen also good boy
def pickCoupons(n: int, coupons):
    # Write your code here
    t=9999999
    for i in range(0,len(coupons)):
        cnt=1
        for j in range(i+1,len(coupons)):
            cnt+=1
            if coupons[i]==coupons[j]:
                
                #print(i,j,cnt)
                #print("t is",t)
                if t>cnt:
                    print(i,j)
                    t=cnt
                    #i=j+1
                break
    if t==0:
        return -1
    else:
        return t

n=int(input())
a=list(map(int,input().split()))
print(pickCoupons(n,a))
//hi cominkhsbdbqjdlwkd