a=int(input())
l=list(map(int,input().split()))
t=min(l)
k=l.index(t)
#print(k)
maxi=-99999999
cnt=k+2
for i in range(k,len(l)):
    if maxi<l[i] and i>k:
        maxi=l[i]
        cnt+=1

if maxi==-99999999:
    print(0)
else:
    print(cnt)