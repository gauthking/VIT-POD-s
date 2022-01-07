n = int(input())
f = 0
l1 = []
if 0<n<10000000:
    s = str(n)
    l = [t for t in range(len(list(s)),0,-1)]
    l3 = [s[0:i] for i in range(1,len(list(s))+1)]
    for p in l3:
        for j in sorted(l,reverse=True):
            if int(p)%j==0:
                if j not in l1:
                    l1.append(j)
                    break
              
if l1==l:
    print("Yes")
else:
    print("No")