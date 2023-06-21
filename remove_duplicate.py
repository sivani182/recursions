def findDuplicate(arr):
    # Write your code here

    # xor=0
    # for i in range(0,len(arr)):
    #     for j in range(i+1,len(arr)):
    #         t=arr[i]^arr[j]
    #         if t==0:
    #             return arr[i]
    ans=0
    for t in range(0,len(arr)):
        ans=ans^arr[t]
    print("xor is ",ans)
    for i in range(0,len(arr)):
        ans=ans^i
        print("ans is:",ans)
    return ans


arr=list(map(int,input().split()))
print(findDuplicate(arr))