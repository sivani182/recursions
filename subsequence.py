
def func(i,a,li,ans):
    if i>=len(a):
        #ans.append(li.copy())
        t=sum(li)
        ans.append(t)
        return
    li.append(a[i])
    func(i+1,a,li,ans)
    li.pop()
    func(i+1,a,li,ans)
a=[9,7,5,4]
ans=[]
func(0,a,[],ans)
print(ans[::-1])