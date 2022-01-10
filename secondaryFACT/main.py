n = int(input())
prod = 1
cnt = 0
for i in range(1, n+1):
    prod *= i
    if prod == n:
        k = i
        if k % 2 == 0:
            prod1=1
            for j in range(1, k + 1):
                if j % 2 == 0:
                    prod1 *= j
            print(prod1)
        elif k % 2 != 0:
            prod1=1
            for p in range(1, k + 1):
                if p % 2 != 0:
                    prod1 *= p
            print(prod1)
    else:
        cnt+=1
        if cnt==n:
            print(-1)


