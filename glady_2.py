def solve(Q, pairs, N, A):
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            found = False
            for k in range(Q):
                if ((A[i] == pairs[k][0] and A[j] == pairs[k][1]) or 
                    (A[i] == pairs[k][1] and A[j] == pairs[k][0])):
                    found = True
                    break
            if found:
                count += 1
    return count

T=int(input())
for _ in range(T):
    Q=int(input())
    pairs = [list(map(int,input().split())) for i in range(Q)]
    N=int(input())
    A=list(map(int,input().split()))
    out=solve(Q,pairs,N,A)
    print(out)
