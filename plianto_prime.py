a=int(input())
b=int(input())
l=[]
for i in range(a,b):
    cnt=0
    if i==1:
        continue
    else:
        for j in range(2,(i//2)+1):
            if i%j==0:
                cnt+=1
        if cnt==0:
            l.append[i]
min_dist=0
max_dist=0
for p in range(0,len(l)):
    t=l[p+1]-l[p]
    