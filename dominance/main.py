n = int(input())
m = int(input())
l1 = [i for i in range(1,n) if n%i==0 and i!=1]
l2 = [j for j in range(1,m) if m%j==0 and j!=1]
if sum(l1)==sum(l2):
    print("No dominance")
elif sum(l1)!=sum(l2):
    if sum(l1)>sum(l2):
        print(n)
    elif sum(l2)>sum(l1):
        print(m)