w = input()
n = int(input())
l = []
k = len(list(w))-1
while k != -1:
    for i in range(1, len(list(w))+1):
        l.append(w[k:i])
    k -= 1
l1 = []
for j in l:
    if j != '':
        l1.append(j)
l2 = []
arr = ['a','e','i','o','u','A','E','I','O','U']
for s in l1:
    count = 0
    for t in s:
        if t in arr:
            count+=1
    if count==n:
        l2.append(s)

print(len(l2))    