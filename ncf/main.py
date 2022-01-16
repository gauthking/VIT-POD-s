u = int(input())
t = int(input())
if u>0 and t>0:
    l = [[i,j] for i in range(t,u+1) for j in range(i,u+1) ]
    c = 0
    for p in l:
        if p[1]!=1 and p[1]>p[0] and p[1]!=p[0]:
            div  = p[0]/p[1]
            fac1 = []
            fac2 = []
            for s in range(1,p[0]+1):
                if p[0]%s==0:
                    fac1.append(s)
            for r in range(1,p[1]+1):
                if p[1]%r==0:
                    fac2.append(s)
            comm = list(set(fac1)&set(fac2))
            comm1 = list(comm)
            if 0.2<=div<=0.6:
                if len(comm)==1 and comm1[0]==1:
                    c+=1
print(c)