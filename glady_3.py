import math
def min_time(n, work):

    # # Sort the work array in non-increasing order
    # work.sort(reverse=True)
    
    # # Calculate the maximum amount of work
    # max_work = work[0]
    # for i in range(1, n):
    #     max_work += work[i]
    
    # # Binary search for the minimum time
    # left, right = max_work // n, max_work
    # while left < right:
    #     mid = (left + right) // 2
    #     curr_time, curr_workers = 0, 1
    #     for w in work:
    #         if curr_time + w > mid:
    #             curr_time = 0
    #             curr_workers += 1
    #         curr_time += w
    #     if curr_workers > n:
    #         left = mid + 1
    #     else:
    #         right = mid
    
    # return left
    # left = 1
    # right = 10 ** 9
    # while left < right:
    #     mid = (left + right) // 2
    #     total_time = 0
    #     for i in range(n):
    #         total_time += (work[i] + mid - 1) // mid
    #     if total_time <= mid:
    #         right = mid
    #     else:
    #         left = mid + 1
    # return left * n
    left, right = 1, max(work)
    while left < right:
        mid = (left + right) // 2
        days = sum(math.ceil(w / mid) for w in work)
        if days <= n:
            right = mid
        else:
            left = mid + 1
    return left * max(work)
N=int(input())
work=list(map(int,input().split()))
out=min_time(N,work)

print(out)
