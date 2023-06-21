def minimumCost(n, s, cost):
    # write your code here
    su=0
    i=0
    while(i<n):
        #print(s[i])
        if s[i]==s[i+1]:
            j=i+1
            p=[]
            p.append(cost[i])
            while True:
                if s[j]==s[i] and j<n-1:
                    #print(s[i])
                    p.append(cost[j])
                    j+=1
                if s[i]==s[j]:
                    p.append(cost[j])
                break
                # else:
                #    # p.append(cost[j])
                #     break
            i=j-1
            print(p)
            print("i is:",i)
            p.remove(max(p))

            su+=sum(p) 
            # if cost[i]<cost[i+1]:
            #     su+=cost[i]
            # else:
            #     su+=cost[i+1]
        #i=j
    return su

n=int(input())
s=input()
l=list(map(int,input().split()))
print(minimumCost(n,s,l))