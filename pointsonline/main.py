a = int(input())
b = int(input())
c = int(input())
n = int(input())
l1 = []
for i in range(0,n+3):
    if i%2!=0:
        x = i
        y = (-c-a*x)/b
        print('%.2f'%y)