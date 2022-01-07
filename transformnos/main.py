n = list(input())
n1 = sorted(n, reverse=True)
n2 = sorted(n)
f=0    
cnt = 0
while f==0:
    s = ""
    s1 = ""
    for i in range(len(n1)):
        if n1[i] == "0":
            s += "0"
        else:
            s += n1[i]
    for j in range(len(n2)):
        if n2[j] == "0":
            s1 += "0"
        else:
            s1 += n2[j]
    diff = abs(int(s) - int(s1))
    elif diff==0:
        print("No")
        f = 1
        continue
    if diff!=495:
        cnt+=1
        diff = str(diff)
        if len(list(diff))!=3:
            diff = '0'*(3-len(diff)) + diff
        n1 = sorted(list(diff),reverse=True)
        n2 = sorted(n1)
    elif str(diff) == '495':
        f = 1
        print(cnt)
        continue