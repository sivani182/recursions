#10 10 20 30 10 20 30 10 20 10 30 20 30
n=int(input())
offc_loc=list(map(int,input().split()))
m=int(input())
bill_amt=list(map(int,input().split()))
t=sum(bill_amt)
print(t)
k=t//n
total=t-(k*n)
#print(total)
l=[]
for i in range(0,n):
    l.append(k)
if total!=0:
    l[-1]=l[-1]+total

min_dif=0
hello=[[]]
for i in range(0,len(bill_amt)):
    y=[]
   # t=len(k)
    for j in range(0,len(hello)):
        t=hello[j]
        t=t+[bill_amt[i]]
#        print(t)
        y.append(t)
    
    hello+=y
bill_amt.sort()
freq = {}
for item in bill_amt:
    if (item in freq):
        freq[item] += 1
    else:
        freq[item] = 1
print(freq)
print(bill_amt)
pk=[]
for h in range(0,n):
    for i in range(0,len(hello)):
        si=sum(hello[i])
        if (len(hello[i])==offc_loc[h]):
            if l[h]-10<si<l[h]+10:
                for v in hello[i]:
                    freq[v]!=0
                # if hello[i] in pk:
                #     print("hi")
                #     continue
                # else:
                #     for r in hello[i]:
                #         pk.append(r)
                #     print(hello[i])
                break

#print(len(hello[[4]]))

print(pk)
#print(hello)
#print(l)

