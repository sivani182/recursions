a=int(input())
t=a//26
k=a%26
s=''
if t>=1:
    if a==26:
        print(chr(64+a))
    elif k==0:
        s=s+chr(64+t-1)
        s=s+chr((64+26))
        #print(str(chr(64+t-1),chr((64+26))))
        print(s)
    else:
        s=s+chr(64+t)
        s=s+chr(64+k)
        #print(str(chr(64+t),chr((64+k))))
        print(s)
else:
    print(chr(64+a))
# i=0
# for i in range(65,65+a):
#     i=i+1
# print(chr(i-1))
# if a>26:
#     for i in range(65,):
#         for j in range()