n = input()
s1 = list(map(int,list(n[::])))
s2 = list(map(int,list(n[::-1])))
sum1=0
sum2=0
for i in range(0,len(s1),2):
    sum1+= s1[i]
for j in range(0,len(s2),2):
    sum2+= s2[j]
print(abs(sum1,sum2))


