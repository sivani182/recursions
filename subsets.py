# arr = [3, 2, 4]
# n = 3

# for num in range(0, 2**n):
#     arr2 = []
#     t = 0
#     for bit in range(0, n):
#         if num & (1 << bit):
#             arr2.append(arr[bit])
#             t += 1
#     for j in range(0, t):
#         print(arr2[j], end=",")
#     print()
print(list(lambda x:x%2==0,[1,2,3,4]))