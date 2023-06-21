# # d={'ab':91,'bwe':'247',34:3,68:'as','485':'sdb'}
# # print(d.pop('ab'))
# # print(d)
# def mod(l):
#     l=[8,9]
# l=[2,4,1,3]
# mod(1)
# print(l)

# arr=[1,5,6,8,4,2]
# n=6
# i=0
# if arr[0]>=arr[1]:
#     print(0)
# if arr[n-1]>=arr[n-2]:
#     print(n-1)
# for i in range(1,n-1):
#     if arr[i]>=arr[i-1] and arr[i]>=arr[i+1]:
#         print(i)
from typing import List

def is_prime(n: int) -> bool:
    """Check if n is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def distinct_prime_factors(n: int) -> int:
    """Count the number of distinct prime factors of n."""
    count = 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if is_prime(i):
                count += 1
            while n % i == 0:
                n //= i
    if n > 1:
        count += 1
    return count

def can_reach(i1: int, j1: int, i2: int, j2: int, p: int, grid: List[List[int]]) -> bool:
    """Check if there is a path from (i1, j1) to (i2, j2) with elements having p distinct prime factors."""
    n, m = len(grid), len(grid[0])
    visited = [[False] * m for _ in range(n)]
    stack = [(i1-1, j1-1)]
    while stack:
        i, j = stack.pop()
        if i == i2-1 and j == j2-1:
            return True
        if not (0 <= i < n and 0 <= j < m) or visited[i][j] or grid[i][j] <= 0 or grid[i][j] == 1 or distinct_prime_factors(grid[i][j]) != p:
            continue
        visited[i][j] = True
        stack.append((i-1, j))
        stack.append((i+1, j))
        stack.append((i, j-1))
        stack.append((i, j+1))
    return False

def solve(N: int, M: int, grid: List[List[int]], Q: int, queries: List[List[int]]) -> List[str]:
    """Compute the answers to the queries."""
    ans = []
    for i in range(Q):
        i1, j1, i2, j2, p = queries[i]
        if can_reach(i1, j1, i2, j2, p, grid):
            ans.append("Yes")
        else:
            ans.append("No")
    return ans

# Get input from the user
N, M, Q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
queries = [list(map(int, input().split())) for _ in range(Q)]

# Call the solve function and print the results
ans = solve(N, M, grid, Q, queries)
for a in ans:
    print(a)
