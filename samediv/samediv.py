N = int(input())
l = [n for n in range(1,N+1) if N%n==0]
l2=[]
for i in range(len(l)):
    for j in range(i,len(l)):
        if l[i]<l[j]:
            if l[i]*l[j]==N:
                pair=(l[i],l[j])
                l2.append(pair)
if len(l2)==0:
    print(-1)
else:
    f=0
    for p in l2:
        l1=[n for n in range(1,p[0]+1) if p[0]%n==0]
        l3=[n for n in range(1,p[1]+1) if p[1]%n==0]
        if len(l1)==len(l3):
            f=1
        else:
            continue
    if f==1:
        print(1)
    elif f==0:
        print(0)
    