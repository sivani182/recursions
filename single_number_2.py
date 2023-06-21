arr=list(map(int,input().split()))
ans=0
for i in range(0,4):
    odd=0
    even=0
    for j in arr:
        if j&(1<<i)!=0:
            odd+=1
        else:
            even+=1
    
    if even%3==1:
        print("h")
        ans=ans|(1<<i)
        
print(ans)