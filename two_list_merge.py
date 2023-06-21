a=list(map(int,input().split()))
b=list(map(int,input().split()))
#c,d=int(input())
a.sort()
b.sort()
n=len(a)
m=len(b)
i=j=0
l=[]
while(i<n and j<m):
    if a[i]<b[j]:
        l.append(a[i])
        i+=1
    else:
        l.append(b[j])
        j+=1
while(i<n):
    l.append(a[i])
    i+=1
while(j<m):
    l.append(b[j])
    j+=1

print(l)
