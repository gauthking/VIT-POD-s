s, N = list(map(int,input().split()))
l =[]
win = 0
if s>0 and N>0:
    for i in range(N):
        try:
            xi,yi=list(map(int,input().split()))
            l.append(xi)
        except EOFError as e:
            print(e)
        if xi>=0 and yi>=0:
            if s>xi:
                s+= yi
                win+=1
            else:
                print("NO")
      

l1 = l[-1]
if win==N:
    print("YES")