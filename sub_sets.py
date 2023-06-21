l=[1,2]
k=[[]]
for i in range(0,len(l)):
    y=[]
   # t=len(k)
    for j in range(0,len(k)):
        t=k[j]
        t=t+[l[i]]
#        print(t)
        y.append(t)
    k+=y
print(k)

# l=[1,2,3,4]
# k=[[]]
# for i in l:
#    k+=[subset+[i] for subset in k]
# print(k)