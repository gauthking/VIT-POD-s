s= input()
c = [s[len(s)-i :] + s[0:len(s)-i] for i in range(len(s)-1,-1,-1) ]
print(len(set(c)))
