s3 = 'xyzb'
s3 = list(s3)
for j in range(len(s3)):
    if s3[j]=='z':
        s3.pop(j)
        s3.insert(j,'a')
        print(''.join(s3))