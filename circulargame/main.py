n = int(input())
l =[int(input()) for i in range(n)]
l1 = []
for i in range(1,len(l)-1):
    k = l[i]
    k1 = l[i-1]
    k2 = l[i+1]    
    if k1<k<k2:
        l1.append(i+1)
if l[-1]<l[0]<l[1]:
    l1.append(1)
if l[-2]<l[-1]<l[0]:
    l1.append(len(l))

if len(l1)==0:
    print("None")
else: 
    for j in l1:
        print(j)