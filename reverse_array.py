def rev(i,j,l):
    if i>=j:
        return
    swap(i,j,l)
    rev(i+1,j-1,l)
    return l

def swap(i,j,l):
    l[i],l[j]=l[j],l[i]
    #print(l[i],l[j])
    return l


l=[1,2,3,4,5]
print(rev(0,4,l))