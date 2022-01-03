w = input()
l = list(w[0:8])
l1 = w[9:]
hr = w[0]+w[1]
min = w[3]+w[4]
sec = w[6]+w[7]
if l1 == 'P.M':
    if 0 < int(hr) < 12:
        hr = int(hr) + 12
        if 8 <= int(hr) <= 15 and 0 <= int(min) <= 59 and 1 <= int(sec) <= 59:
            if int(hr) == 8 and int(min) == 0 and int(sec) == 0:
                print('08:00:00 midmorning')
            else:
                hr = abs(int(hr)-8)
                if len(list(str(hr))) == 2:
                    print(str(hr)+':'+min+':'+sec + ' '+'B.M')
                else:
                    print('0'+str(hr)+':'+min+':'+sec + ' '+'B.M')
        elif 16 <= int(hr) <= 23 and 0 <= int(min) <= 59 and 1 <= int(sec) <= 59:
            if hr == 16 and min == 0 and sec == 0:
                print('08:00:00 midevening')
            else:
                hr = abs(int(hr)-16)
                if len(list(str(hr))) == 2:
                    print(str(hr)+':'+min+':'+sec + ' '+'C.M')
                else:
                    print('0'+str(hr)+':'+min+':'+sec + ' '+'C.M')

    elif int(hr) == 12:
        hr = abs(int(hr)-8)
        if len(list(str(hr))) == 2:
            print(str(hr)+':'+min+':'+sec + ' '+'B.M')
        else:
            print('0'+str(hr)+':'+min+':'+sec + ' '+'B.M')
    elif int(hr) == 12 and int(min) == 0 and int(sec) == 0:
        print('08:00:00 midnight')
    elif int(hr) == 0 and int(min) == 0 and int(sec) == 0:
        print('08:00:00 midnight')
    elif int(hr) > 12:
        if 8 <= int(hr) <= 15 and 0 <= int(min) <= 59 and 1 <= int(sec) <= 59:
            hr = abs(int(hr)-8)
            if len(list(str(hr))) == 2:
                print(str(hr)+':'+min+':'+sec + ' '+'B.M')
            else:
                print('0'+str(hr)+':'+min+':'+sec + ' '+'B.M')
        elif 16 <= int(hr) <= 23 and 0 <= int(min) <= 59 and 1 <= int(sec) <= 59:
            if hr == 16 and min == 0 and sec == 0:
                print('08:00:00 midevening')
            else:
                hr = abs(int(hr)-16)
                if len(list(str(hr))) == 2:
                    print(str(hr)+':'+min+':'+sec + ' '+'C.M')
                else:
                    print('0'+str(hr)+':'+min+':'+sec + ' '+'C.M')
    elif 0 <= int(hr) <= 7 and 0 <= int(min) <= 59 and 1 <= int(sec) <= 59:
        print(str(hr)+':'+min+':'+sec + ' '+'A.M')

if l1 == 'A.M':
    if 0 <= int(hr) <= 7 and 0 <= int(min) <= 59 and 1 <= int(sec) <= 59:
        print(str(hr)+':'+min+':'+sec + ' '+'A.M')
    elif 8 <= int(hr) <= 15 and 0 <= int(min) <= 59 and 1 <= int(sec) <= 59:
            hr = abs(int(hr)-8)
            if len(list(str(hr))) == 2:
                print(str(hr)+':'+min+':'+sec + ' '+'B.M')
            else:
                print('0'+str(hr)+':'+min+':'+sec + ' '+'B.M')
    elif int(hr) == 0 and int(min) == 0 and int(sec) == 0:
        print('08:00:00 midnight')
        
    elif int(hr) == 8 and int(min) == 0 and int(sec) ==0 :
        print('08:00:00 midmorning')


if l1 == 'midnight':
    if int(hr) == 0 and int(min) == 0 and int(sec) == 0:
        print('08:00:00 midnight')
    elif int(hr) == 12 and int(min) == 0 and int(sec) == 0:
        print('08:00:00 midnight')
