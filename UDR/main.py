n = int(input())
l1 = [i for i in range(1,n+1) if n%i==0]
l2 = []
for i in range(int(len(l1)//2)):
    l2.append((l1[i],l1[len(l1)-i-1]))
print(len(l2))
for j in l2:
    print(*list(j))