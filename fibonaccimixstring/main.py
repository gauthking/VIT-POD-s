s1 = input()
s2 = input()
n = int(input())
fs=s1
ss=s2
l = [fs,ss]
for i in range(n):
    s3 = ''
    for p in range(len(s1)):
        if p%2==0:
            s3+= chr(ord(fs[p])+1)
        else:
            s3+= chr(ord(ss[p])+1)
    s3 = list(s3)

    for j in range(len(s3)):
        if ord(s3[j])>122:
            s3.pop(j)
            s3.insert(j,'a')
            s4 = ''.join(s3)
            l.append(s4)
            fs = ss
            ss = s4
            break

    else:
        s4 = ''.join(s3)
        l.append(s4)
        fs = ss
        ss = s4
    
    
print(l[n-1])
print(l)