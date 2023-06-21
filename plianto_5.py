def title(s):
    result=0
    for b in range(len(s)):
        result*=26
        result+=ord(s[b])-ord('A')+1
    return result
#t=int(input())
print(title('CDA'))
