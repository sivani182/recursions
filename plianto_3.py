n=int(input())
s=int(input())
t=9
val=0
for i in range(0,n-1):
    t=(t*10)+9
#print(t)
for j in range(t,-1,-1):
    #print(j)
    p=j
    su=0
    while(p>0):
        x=p%10
        su=su+x
        p=p//10
    #print(su)
    if su==s:
        val=j
        break
if val==0:
    print("Not valid")
else:
    print(val)        
